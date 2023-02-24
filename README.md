# Voting-Rules

In this code several voting rules have been implemented. In a voting setting, we have a set of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>n</mi>
</math> agents and a set of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>m</mi>
</math> alternatives. Every agent has a preference ordering <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mo>&#x227B;<!-- ≻ --></mo>
</math> where <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x03B1;<!-- α --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B2;<!-- β --></mi>
</math> means that the agent prefers alternative <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x03B1;<!-- α --></mi>
</math> to alternative <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x03B2;<!-- β --></mi>
</math>. A preference profile is a set of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>n</mi>
</math> preference orderings, one for every agent.

For example, if we have a voting setting with 4 agents and 4 alternatives, one possible preference profile could be the following:<br>
Agent 1: <math xmlns="http://www.w3.org/1998/Math/MathML"> 
  <mi>&#x03B1;<!-- α --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B2;<!-- β --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B4;<!-- δ --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B3;<!-- γ --></mi>
</math> <br>
Agent 2: <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x03B1;<!-- α --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B2;<!-- β --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B4;<!-- δ --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B3;<!-- γ --></mi>
</math> <br>
Agent 3: <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x03B3;<!-- γ --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B2;<!-- β --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B1;<!-- α --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B4;<!-- δ --></mi>
</math> <br>
Agent 4: <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x03B2;<!-- β --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B1;<!-- α --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B4;<!-- δ --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B3;<!-- γ --></mi>
</math> <br>


A voting rule is a function that takes as input the preferences of a set of agents and outputs a winning alternative.


<strong>Voting Rules:</strong> <br>

Dictatorship: <br>
An agent is selected, and the winner is the alternative that this agent ranks first. For example, if the preference ordering of the selected agent is <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x03B1;<!-- α --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B3;<!-- γ --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B2;<!-- β --></mi>
  <mo>&#x227B;<!-- ≻ --></mo>
  <mi>&#x03B4;<!-- δ --></mi>
</math>, then the winner is alternative <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x03B1;<!-- α --></mi>
</math>. <br>

Plurality:<br>
The winner is the alternative that appears the most times in the first position of the agents' preference orderings. In the case of a tie, use a tie-breaking rule to select a single winner.

Veto:<br>
Every agent assigns 0 points to the alternative that they rank in the last place of their preference orderings, and 1 point to every other alternative. The winner is the alternative with the most number of points. In the case of a tie, use a tie-breaking rule to select a single winner.

Borda:<br>
Every agent assigns a score of 0 to the their least-preferred alternative (the one at the bottom of the preference ranking), a score of 1 to the second least-preferred alternative, ... , and a score of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>m</mi>
  <mo>&#x2212;<!-- − --></mo>
  <mn>1</mn>
</math> to their favourite alternative. In other words, the alternative ranked at position <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>j</mi>
</math> receives a score of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>m</mi>
  <mo>&#x2212;<!-- − --></mo>
  <mi>j</mi>
</math>. The winner is the alternative with the highest score. In the case of a tie, use a tie-breaking rule to select a single winner.

Harmonic:<br>
Every agent assigns a score of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mn>1</mn>/
    <mi>m</mi>
  </mfrac>
</math> to the their least-preferred alternative (the one at the bottom of the preference ranking), a score of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mn>1</mn>/
    <mrow>
      <mi>m</mi>
      <mo>&#x2212;<!-- − --></mo>
      <mn>1</mn>
    </mrow>
  </mfrac>
</math> to the second least-preferred alternative, ... , and a score of 1 to their favourite alternative. In other words, the alternative ranked at position <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>j</mi>
</math> receives a score of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mn>1</mn>/
    <mi>j</mi>
  </mfrac>
</math>. The winner is the alternative with the highest score. In the case of a tie, use a tie-breaking rule to select a single winner.

Single Transferable Vote (STV): <br>
The voting rule works in rounds. In each round, the alternatives that appear the least frequently in the first position of agents' rankings are removed, and the process is repeated. When the final set of alternatives is removed (one or possibly more), then this last set is the set of possible winners. If there are more than one, a tie-breaking rule is used to select a single winner.


Tie-Breaking Rules: <br>

Following are the three tie-breaking rules, the alternatives are represented by integers.

    max: Among the possible winning alternatives, select the one with the highest number.
    min: Among the possible winning alternatives, select the one with the lowest number.
    agent i: Among the possible winning alternatives, select the one that agent ranks the highest in his/her preference ordering. 
