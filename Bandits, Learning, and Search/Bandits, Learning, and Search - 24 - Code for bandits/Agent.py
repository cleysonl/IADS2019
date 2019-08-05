# ------------------------------------------
# Tom Vodopivec
#
# IADS Analytics & Data Science Summer School 2019
# Course: Bandits, Learning, and Search
# 2019-08-05
#
# ------------------------------------------

from enum import Enum, auto
import random

class banditPolicy(Enum):
	RANDOM = auto()
	#EGREEDY = auto()

# The Multi-Armed-Bandit (MAB) solver structure
class Agent() :

    selectedBanditAlgorithm = None
    numArms = None

    # initialization
    def __init__(self,
        selectedBanditAlgorithm=banditPolicy.RANDOM,
        param=0,
        init_arms=0,) :
        self.param = param
        self.selectedBanditAlgorithm = selectedBanditAlgorithm
        self.reset(init_arms)
		
    # reset memory structures (preparation for new testcase)
    def reset(self, numArms) :
        self.numArms = numArms
		# < ADD HERE OWN CODE >

    # select an arm from available stats
    def selectAction(self) :
        if   self.selectedBanditAlgorithm == banditPolicy.RANDOM:   selected_arm = random.randint(0, self.numArms - 1)	
		# elif
		# < ADD HERE OWN CODE >
		
        return selected_arm


    # update knowledge
    def updateKnowledge(self, arm_id, reward) :
		# < ADD HERE OWN CODE >

        pass
