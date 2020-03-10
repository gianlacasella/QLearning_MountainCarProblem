# QReinforcementLearning_MountainCarProblem

## Using QLearning on the OpenAI's MountainCar-v0 environment

On this project, I trained an AI Agent with **Model-free Reinforcement Learning (QLearning)** on the OpenAI's [MountainCar-v0](https://gym.openai.com/envs/MountainCar-v0/) environment.
<br>The goal is to drive up the mountain on the right; however, **the car's engine is not strong enough to scale the mountain in a single pass**. Therefore, the only way to succeed is to drive back and forth to build up momentum.

<p align="center">
  <img src="img/MountainCarGif.gif">
</p>

In order to make the Agent succeed, I used Markov Processes and the Bellman Equation to make the pairs (state, action) quality update:

<p align="center">
  <img src="img/equation.svg">
</p>


## My results




## Prerequisites
* Python 3.5
* Matplotlib
* Numpy
* Gym

## Getting started



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
