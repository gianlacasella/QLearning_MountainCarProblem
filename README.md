# QReinforcementLearning_MountainCarProblem

## Using QLearning on the OpenAI's MountainCar-v0 environment

On this project, I trained an AI Agent with **Model-free Reinforcement Learning (QLearning)** on the OpenAI's [MountainCar-v0](https://gym.openai.com/envs/MountainCar-v0/) environment.
<br><br>The main goal is to drive up the mountain on the right; however, **the car's engine is not strong enough to scale the mountain in a single pass**. Therefore, the only way to succeed is to drive back and forth to build up momentum.

<p align="center">
  <img src="img/MountainCarGif.gif">
</p>

In order to make the Agent succeed, I used Markov Processes and the Bellman Equation to make the state-action pairs quality update:

<p align="center">
  <img src="img/equation.svg">
</p>


## My results

The environment gives a living reward of -1 on each step the Agent makes, and has a maximum of 200 steps per episode. Thats why,
at the training beginning the Best Rewards are -200. I tried to compare Greedy, ε-Greedy and ε-Greedy-Descendant algorithms.

The parameters used to make the comparison are:
* 50000 episodes
* Learning rate 0.05
* Discount factor 0.95
* On the Greedy, obviously ε=0
* On the ε-Greedy I used two values of ε: 0.3 and 0.7
* On the ε-Greedy-Descendant:
	1. Starting ε: 1
	2. Minimum ε: 0.005
	3. ε Decay (for each step): 3ε/10000000

Algorithms comparation         |  The best one (ε-Greedy-Descendant)
:-----------------------------:|:----------------------------------:
![](outputs/4plots.jpg)        |  ![](outputs/greedyDescendant.jpg)

As can be seen in the previous images, the ε-Greedy-Descendant algorithm was the best as expected:

<p align="center">
  <img src="img/Table.JPG">
</p>

On the following picture can be seen the ε-Greedy-Descendant algorithm exploration and exploitation phases and
the ε value

<p align="center">
  <img src="outputs/greedyDescendantEpsilon.jpg" width="700px" height="500px">
</p>


## Prerequisites
* Python 3.5
* Matplotlib
* Numpy
* OpenAI's Gym

## Getting started

Clone this repository, open the Terminal/Command Prompt inside it. The parameters for the execution are:
```
		
		# -e value => Selects ε-Greedy with ε=value
        # -d init min => Selects Epsilon-Descendant-Greedy with  ε=init and min_ε=min
        If neither of the previous two parameters are given, the training will be done with the Greedy algorithm
        # -m ep => Sets the number of episodes (Default: 50000)
        # -s steps => Sets the max number of steps per episode (Default:200 and should be smaller than 201)
        # -a value => Sets Alpha value
        # -g value => Sets Gamma value
```



## What I learned

* Markov Processes and Bellman Equation
* QLearn Algorithm 
* QLearn Algorithm optimization with Greedy, ε-Greedy and ε-Greedy-Descendant variations
* To use Gym by OpenAI
* Multidimensional arrays with Numpy

## Authors

* **Gianfranco Lacasella** - *Initial work* - [glacasellaUANDES](https://github.com/glacasellaUANDES)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE- see the [LICENSE.md](LICENSE.md) file for details
