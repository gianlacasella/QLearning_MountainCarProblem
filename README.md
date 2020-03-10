# QReinforcementLearning_MountainCarProblem

## Using QLearning on the MountainCar-v0 environment of OpenAI

A program that **solves Statics Truss Problems, made with a mix of C# (used for GUI) and Python (used to solve the problems and graphing the result: Scipy and Matplotlib)**. With this program, you will be able to **save the problem solution graph and the nodes, connections and forces** in a very high resolution.

Program view (solved problem)|  Full size view (solved problem)
:---------------------------:|:--------------------------------:
![](img/sts12.JPG)           |  ![](img/sts13.JPG)

As you can see in the previous images, once solved, **the program generates a truss plot. Over each bar/connection that forms
the truss prints the net force that is applied over it, and the colors indicates if they are on compression or on traction**:

* **Red**: compression
* **Purple-like**: between compression and traction
* **Blue**: traction

Also, **in the console log the program generates a solution vector, which includes all the bars/connections and the
reactions over the truss supports**.

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
