# -*- coding: utf-8 -*-
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
    

