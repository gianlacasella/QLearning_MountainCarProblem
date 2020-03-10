# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as pt

ALL_DATA_DICT = {}

filenames = ["output_greedy_algorithm.txt", "output_greedy_,3_algorithm.txt",
             "output_greedy_,7_algorithm.txt", "output_greedy_descendant_algorithm.txt"]

for filename in filenames:
    file = open("./outputs/"+filename)
    fileSplitted = []
    for line in file:
        splitted = line.split(',')
        i=0
        for element in splitted:
            splitted[i] = float(element.strip())
            i+=1
        fileSplitted.append(splitted)
    episodes = []
    totalRewards = []
    bestRewards = []
    epsilons = []
    for ep in fileSplitted:
        episodes.append(ep[0])
        totalRewards.append(ep[1])
        bestRewards.append(ep[2])
        epsilons.append(ep[3])
    ALL_DATA_DICT[filename] = {'episodes':episodes, 'total':totalRewards,'best':bestRewards,'epsilons':epsilons}
    
fig=pt.figure()
fig.suptitle('Best rewards vs Iterations of 4 different Epsilon use')
ax=fig.add_subplot(111)
ax.set_xlabel('Iterations')
ax.set_ylabel('Best reward')
X=np.arange(0,50000)
pt.plot(X,ALL_DATA_DICT["output_greedy_descendant_algorithm.txt"]['best'], color="blue", label="Epsilon Greedy Descendant (from 1 to 0.005)")
pt.plot(X,ALL_DATA_DICT["output_greedy_algorithm.txt"]['best'], color="red", label="Greedy")
pt.plot(X,ALL_DATA_DICT["output_greedy_,3_algorithm.txt"]['best'], color="green", label="Epsilon Greedy (.3)")
pt.plot(X,ALL_DATA_DICT["output_greedy_,7_algorithm.txt"]['best'], color="yellow", label="Epsilon Greedy(.7)")
pt.legend(loc="upper left")
pt.ylim(-210, -30)
pt.savefig('./outputs/4plots.jpg',dpi=500)

k=0
for i in ALL_DATA_DICT["output_greedy_descendant_algorithm.txt"]['epsilons']:
    if i<0.005:
        minimum=k
        break
    k+=1

k=0
for i in ALL_DATA_DICT["output_greedy_descendant_algorithm.txt"]['epsilons']:
    if i<0.5:
        half=k
        break
    k+=1

fig.clf()
fig.suptitle('Rewards vs Iterations of the Greedy Descendant Algorithm')
ax=fig.add_subplot(111)
ax.set_xlabel('Iterations')
ax.set_ylabel('Rewards')
X=np.arange(0,50000)
pt.plot(X,ALL_DATA_DICT["output_greedy_descendant_algorithm.txt"]['total'], color="blue", label="Reward")
pt.plot(X,ALL_DATA_DICT["output_greedy_descendant_algorithm.txt"]['best'], color="red", label="Best reward")
pt.axvline(minimum, color="yellow", label="Epsilon is minimum (0.005 by default)")
pt.legend(loc="upper left")
pt.ylim(-200, -40)
pt.savefig('./outputs/greedyDescendant.jpg',dpi=500)



fig.clf()
fig.suptitle('Rewards vs Iterations of the Greedy Descendant Algorithm')
ax=fig.add_subplot(111)
ax.set_xlabel('Iterations')
ax.set_ylabel('Rewards')
X=np.arange(0,50000)
pt.plot(X,ALL_DATA_DICT["output_greedy_descendant_algorithm.txt"]['best'], color="blue", label="Best reward")
pt.axvline(half, color="red", label="Epsilon is 0.5")
pt.axvline(minimum, color="yellow", label="Epsilon is minimum (0.005 by default)")
pt.legend(loc="upper left")
pt.ylim(-200, -40)
pt.savefig('./outputs/greedyDescendantEpsilon.jpg',dpi=500)
