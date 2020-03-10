# -*- coding: utf-8 -*-
from optparse import OptionParser
import trainer as tr

class App:
    def __init__(self):
        self.processInput()
        trainer = tr.Trainer(self.epsilon, self.algorithm, self.min_epsilon, self.episodes, self.max_steps, self.alpha, self.gamma)
        bestPolicy = trainer.StartTraining()
        trainer.GenerateOutput()
        print("Best policy learned: ", bestPolicy)
        input("Press enter to see what the agent learned")
        for _ in range(1000):
            trainer.test()
        
    
    
    def processInput(self):
        # By default, it is greedy. Siempre va a generar la salida de matplotlib
        # -e value => Epsilon-greedy (recommended: 0.7)
        # -d initialEpsilon minEpsilon => Epsilon-descendant-greedy (recommended: 1 0.005)
        # -m episodes => Max num episodes (recommended: 50000)
        # -s max_num_steps_per_episode => Max num steps per episode (int<200)
        # -a value => Alpha
        # -g value => Gamma
        try:
            parser = OptionParser()
            parser.add_option('-e')
            parser.add_option('-d')
            parser.add_option('-m')
            parser.add_option('-s')
            parser.add_option('-a')
            parser.add_option('-g')
            (options, args) = parser.parse_args()
            options = vars(options)
            print(options)
            # Processing algorithm type
            if options['e'] != None:
                self.epsilon = float(options['e'])
                self.algorithm = 'EpsilonGreedy'
                self.min_epsilon = None
            elif options['d'] != None:
                
                self.epsilon = float((options['d'].split(','))[0])
                self.min_epsilon = float((options['d'].split(','))[1])
                self.algorithm = 'EpsilonDescendantGreedy'
            else:
                self.epsilon = 0
                self.algorithm = 'Greedy'
                self.min_epsilon = None
                
            if options['m'] != None:
                self.episodes = int(options['m'])
            else:
                self.episodes = 50000
                
            if options['s'] != None and int(options['s'])<200:
                self.max_steps = int(options['s'])
            else:
                self.max_steps = 200
                
            if options['a'] != None:
                self.alpha = float(options['a'])
            else:
                self.alpha = 0.05
                
            if options['g'] != None:
                self.gamma = float(options['g'])
            else:
                self.gamma = 0.95
        except:
            print("Something went wrong parsing your input, please check it out")
           

if __name__ == "__main__":
    App()