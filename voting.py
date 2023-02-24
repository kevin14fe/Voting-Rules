import openpyxl
import copy
from collections import Counter
from collections import defaultdict


# Implementation of several voting rules - Dictatorship, Plurality, Veto, Borda, Harmonic and Single Transferable Vote (STV). In a voting setting, we have a set of agents n and a set of m alternatives. 
# Every agent has a preference ordering a > b which means that the agent prefers alternative 'a' to alternative 'b'.
# A preference profile is a set of n preference orderings, one for every agent.



def generatePreferences(values):

  """The generatePreferences function inputs a 2D list of values corresponding to a worksheet and returns a dictionary of preferences, where the keys are 
  the indices of the agents and the values are lists of alternatives sorted in decreasing order of preference."""

  # Read the values from the worksheet(values) into a 2D list.
  values_list = []
  for row in values.rows:
      values_list.append([cell.value for cell in row])
  
  # Get the number of rows (agents) and columns (alternatives) in the 2D list.
  num_agents = len(values_list)
  num_alternatives = len(values_list[0])
  
  # Initialize the preferences dictionary.
  preferences = {}
  
  # Iterate through the agents.
  for i in range(num_agents):

    # Get the valuations of the alternatives for this agent.
    valuations = values_list[i]
    
    # Sort the alternatives based on their valuations.
    sorted_alternatives = [alternative+1 for _, alternative in sorted(zip(valuations, range(num_alternatives)), reverse=True)]
    
    # Store the sorted list of alternatives in the preferences dictionary.
    preferences[i+1] = sorted_alternatives

  # Eeturns the preferences dictionary.
  return preferences





def dictatorship(preferenceProfile, agent):

    """The dictatorship function inputs a dictionary of preference profiles and an integer representing an agent, and 
    returns the first alternative (also known as the top choice) in the ranking of the specified agent."""

    # Checks if the agent is an integer, and if not, it raises a TypeError indicating that the agent must be an integer. 
    if not isinstance(agent, int):
        raise TypeError("Agent must be an integer")

    # Checks if the agent is in the preference profile, and if not, it raises a ValueError indicating that the agent was not found in the preference profile.
    if agent not in preferenceProfile:
        raise ValueError("Agent not found in preference profile")

    # Returns the first alternative in the ranking of the specified agent by accessing the first element in the list stored at the key agent in the preference profile dictionary.
    return preferenceProfile[agent][0]





def scoringRule(preferences, score_vector, tieBreak):

    """The scoringRule function inputs a dictionary of preferences, a score vector, and a tie-break method, and returns the index of the winning alternative 
    based on the preferences and score vector."""

    # Initialize the preferences dictionary and winner list.
    score_dict = {}
    winner = list()   
    
    # Check if score vector of length m , i.e., equal to the number of alternatives, i.e., a list of length m containing positive floating numbers. 
    alt_len = len(preferences[list(preferences.keys())[0]])
    if len(score_vector) != alt_len:
        print("Incorrect input")
        return False


    # Iterates through the keys (i.e., indices) in the preferences dictionary, and for each key, it creates a temporary dictionary called temp_dict that maps the alternatives 
    #to their scores in the score vector. The score vector is sorted in decreasing order so that the alternatives with the highest scores come first.
    for key in preferences.keys():
        temp_dict = dict(zip(preferences[key], sorted(score_vector, reverse=True)))

        # Updates the score_dict by adding the scores for each alternative. It does this by iterating through the key-value pairs in the temporary dictionary, and for each 
        # pair, it adds the value (i.e., the score) to the current value in the score_dict for the key (i.e., the alternative). If the key (i.e., alternative) is not in the score_dict, it 
        # sets the value to the score.
        for key, values in temp_dict.items(): 
            score_dict[key] = score_dict.get(key, 0) + values
 

    # Identify the winning alternatives.
    max_val = max(score_dict.items(), key=lambda x:x[1])
    for key, values in score_dict.items():
        if values == max_val[1]:
            winner.append(key)

    # Apply the tie-breaking rule.
    return tie_breaking(preferences, tieBreak, winner)





def plurality(preferences, tie_break):

    """The plurality function inputs a dictionary of preferences and a tie-break method, and returns the index of the winning alternative based on the Plurality rule."""

    # Compute the number of times each alternative appears in first place.
    first_place_counts = Counter([ranking[0] for ranking in preferences.values()])
    
    # Identify the possible winning alternatives.
    max_count = max(first_place_counts.values())
    winners = [a for a, count in first_place_counts.items() if count == max_count]
    
    # If there is a tie, apply the tie-breaking rule.
    return tie_breaking(preferences, tie_break, winners)





def veto(preferences, tie_break):

    """The veto function inputs a dictionary of preferences and a tie-break method, and returns the index of the winning alternative based on the Veto rule."""

    # Initialize a dictionary to store the points for each alternative.
    points = {}

    # Iterates through the keys (i.e., indices) and values (i.e., rankings) in the preferences dictionary, and for each alternative in the ranking, it increments its points by 1 if 
    # it is not the last alternative in the ranking. This means that every alternative except the last one in the ranking gets 1 point.
    for agent, pref in preferences.items():
        for i, alt in enumerate(pref):
            if alt not in points:
                points[alt] = 0
            if i != len(pref) - 1:  # Give 1 point to every alternative except the last one.
                points[alt] += 1

    # Find the maximum number of points.
    max_points = max(points.values())

    # Find the alternatives with the maximum number of points.
    winners = [alt for alt, pt in points.items() if pt == max_points]

    if len(winners) == 1:
        return winners[0]  # Return the only winner.

    # If there is a tie, apply the tie-breaking rule.
    return tie_breaking(preferences, tie_break, winners)





def borda (preferences, tieBreak):

    """The borda function inputs a dictionary of preferences and a tie-break method, and returns the index of the winning alternative based on the Borda rule."""

    # Dictionary to store scores for each alternative.
    scores = {} 
    
    for i in preferences:                           # For each agent
        ranking = preferences[i]                    # get their preference ranking
        for j in range(len(ranking)):               # for each alternative in their ranking
            alt = ranking[j]                        # get the alternative
            if alt in scores:                       # if the alternative has already been scored
                scores[alt] += len(ranking)-j-1     # add the score to the existing score
            else:                                   # if the alternative has not been scored
                scores[alt] = len(ranking)-j-1      # create a new entry for the alternative with the score.


    # Find the maximum score and the alternatives with the maximum score.
    maxScore = max(scores.values())
    winners = [k for k, v in scores.items() if v == maxScore]

    # Apply tie-breaking rule.
    return tie_breaking(preferences, tieBreak, winners)





def harmonic(preferences, tie_break):
    
    """The harmonic function inputs a dictionary of preferences and a tie-break method, and returns the index of the winning alternative based on the Harmonic rule."""

    # Compute the score of each alternative.
    scores = defaultdict(int)
    for agent, ranking in preferences.items():
        for i, alternative in enumerate(ranking):
            scores[alternative] += 1 / (i + 1)
    
    # Identify the possible winning alternatives.
    max_score = max(scores.values())
    winners = [a for a, s in scores.items() if s == max_score]
    
    # Apply the tie-breaking rule.
    return tie_breaking(preferences, tie_break, winners)


    


def STV(preferences, tieBreak):

    """The STV function inputs a dictionary of preferences and a tie-break method, and returns 
    the index of the winning alternative based on the preferences using the Single Transferable Vote (STV) voting system."""

    temp_dict = copy.deepcopy(preferences)

    # Starts with an infinite loop, and at each iteration, it computes the frequency (i.e., number of occurrences) of each 
    # alternative in the first position of the rankings in the preferences dictionary. It stores these frequencies in a dictionary called frequency.
    while True:
        frequency = dict.fromkeys(temp_dict[1], 0)
        for values in  temp_dict.values():
            frequency[values[0]] += 1

        # the lowest value is calculated and appended to the least list.
        least = list()
        min_value = min(frequency.values())
        for key, values in frequency.items():
            if values == min_value:
                least.append(key)
        
        # If there is a tie (i.e., if there is more than one alternative in the least list), it calls the tie_breaking function to apply the tie-break method and returns the result.
        if len(least) == len(temp_dict[1]):
            return tie_breaking(preferences, tieBreak, least)

        # If there is no tie (i.e., if there is only one alternative in the least list), it removes the least frequent alternative from the preferences dictionary and repeats the 
        # process until there is a tie.
        else:
            for item in least:
                frequency.pop(item, None)
            for values in temp_dict.values():
                for item in least:
                    values.remove(item)





def rangeVoting(values, tieBreak):

    """The rangeVoting function inputs a list of values and a tie-break method, and returns the index of the winning alternative based on the Range Voting rule."""

    # Initialize a dictionary to store the sums for each alternative.
    sums = {}

    # Iterate through the worksheet and sum the values for each alternative.
    for row in values:
        for i in range(1, len(row)+1):
            if i in sums:
                sums[i] += row[i-1].value
            else:
                sums[i] = row[i-1].value

    # Determine the alternative(s) with the maximum sum of valuations.
    max_val = max(sums.values())
    max_keys = [k for k, v in sums.items() if v == max_val]

    # Use the tie-breaking option to distinguish between the possible winners
    if len(max_keys) == 1:
        # If there is no tie, return the alternative with the maximum sum of valuations.
        return max_keys[0]
    else:
        # Call the tie_breaking function.
        preferences = generatePreferences(values)
        return tie_breaking(preferences, tieBreak, max_keys)





def tie_breaking(preferences, tieBreak, winner):

    """The tie_breaking function inputs a dictionary of preferences, a tie-break method, and a list of winners (i.e., alternatives that have tied), and returns 
    the index of the winning alternative based on the tie-break method specified."""

    # Returns the maximum element in the winner list.
    if tieBreak == 'max':
        return max(winner)

    # Returns the minimum element in the winner list. 
    elif tieBreak == 'min':
        return min(winner)

    # Tie-break method is an integer representing the index of an agent, and the function returns the highest-ranked alternative in the ranking of the specified agent that is also a winner.
    else:
        if tieBreak in preferences.keys():
            for values in preferences[tieBreak]:
                if values in winner:
                    return values