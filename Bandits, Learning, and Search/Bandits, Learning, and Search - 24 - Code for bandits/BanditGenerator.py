# ------------------------------------------
# Tom Vodopivec
#
# IADS Analytics & Data Science Summer School 2019
# Course: Bandits, Learning, and Search
# 2019-08-05
#
# ------------------------------------------

import random

# Generator of a single one-armed bandit
class BanditGenerator() :
    intervals = None
    probabilities = None

    # single pull - returns 0 or 1 regarding the pull number and generators
    # internal probability
    def pull(self,p) :
        for i in range(len(self.intervals) - 1, -1, -1) :
            if p >= self.intervals[i] :
                if random.random() < self.probabilities[i] :
                    return 1.0
                else :
                    return 0.0

    # returns the exact internal probability at a specified pull number
    def prob(self,p) :
        for i in range(len(self.intervals) - 1, -1, -1) :
            if p >= self.intervals[i] :
                return self.probabilities[i]

    # calculates the maximal achieveable reward in a given ammount of pulls
    def calcFullReward(self, max_pulls) :
        fullReward = 0.0
        endInterval = max_pulls
        for i in range(len(self.intervals) - 1, -1, -1) :
            if(endInterval >= self.intervals[i]) :
                fullReward += self.probabilities[i] * (endInterval - self.intervals[i])
            endInterval = self.intervals[i]
        return fullReward

# A multi-armed bandit test case
# may be bound to an online-server by specifying the URL or to an internal
# bandit generator
class BanditTestCase() :
    
    ID = -1

    onlineUrl = None

    numBandits = None
    maxPulls = None
    maximumReward = None
    randomReward = None

    bandits = []

    # if URL is given at init, then the test case requests data from the given
    # online server
    def __init__(self, url=None) :
        self.onlineUrl = url

    # pull a specified one-armed bandit
    def pullBandit(self,bandit_id,pull_id) :
        if (self.onlineUrl is None) :
            reward = self.bandits[bandit_id].pull(pull_id)
        else :
            reward = -1 #getMachineResponse(url,bandit_id,pull_id)
        return reward

    # pull a specified one-armed bandit
    def probBandit(self,bandit_id,pull_id) :
        if (self.onlineUrl is None) :
            reward = self.bandits[bandit_id].prob(pull_id)
        else :
            print('BanditTestCase(): probBandit(): ERROR, CANNOT GET PROBABILITY OF URL_BANDIT')
        return reward

    # inquire about the number of bandits in the test case
    def getNumBandits(self) :
        if (self.onlineUrl is None) :
            return self.numBandits
        else :
            #self.numBandits = getNumMachines(url)
            return -1 

    # inquire about the total number of pulls in the test case
    def getMaxPulls(self) :
        if (self.onlineUrl is None) :
            return self.maxPulls
        else :
            #self.maxPulls = getNumPulls(url)
            return -1

    # calculate maximum achievable reward for the test case
    def calcMaxReward(self) :
        if not (self.onlineUrl is None) :
            return -1

        all_intervals = []
        for b in range(self.numBandits) :
            all_intervals += self.bandits[b].intervals
        all_intervals = sorted(set(all_intervals))
        all_intervals = all_intervals + [self.maxPulls]

        self.maximumReward = 0.0
        for i in range(len(all_intervals) - 1) :
            best_reward = 0.0
            for b in range(self.numBandits) :
                prob = self.bandits[b].prob(all_intervals[i])
                if(prob > best_reward) :
                    best_reward = prob
            self.maximumReward += best_reward * (all_intervals[i + 1] - all_intervals[i])

        return self.maximumReward

    # calculate random-policy reward for the test case
    def calcRandomReward(self) :
        if not (self.onlineUrl is None) :
            return -1

        self.randomReward = 0.0
        for b in range(self.numBandits) :
            self.randomReward += self.bandits[b].calcFullReward(self.maxPulls)
        self.randomReward /= self.numBandits

        return self.randomReward

# A batch of multi-armed bandit scenarios
class BanditTestBatch() :

    list = None
    num = None
    sumMaxRewards = None
    sumRandomRewards = None

    infoNumOutputLines = 4

    # initialize and calculate the maximum achievable reward and random-policy
    # reward for the test batch
    def __init__(self, allCases, indices) :
        self.list = [ allCases[i] for i in indices ]
        self.num = len(indices)

        # compute maximal possible sum of rewards and random policy performance
        self.sumMaxRewards = 0.0
        self.sumRandomRewards = 0.0
        for c in range(0, self.num) :
            self.sumMaxRewards += self.list[c].maximumReward
            self.sumRandomRewards += self.list[c].randomReward

    def info(self) :
        print('BanditTestBatch: casesIDs: ')
        for i in range(self.num) :
            print('%d ' % self.list[i].ID)
        print('')
        print('BanditTestBatch: numCases: %d' % self.num)
        print('BanditTestBatch: optimal reward: %.1f' % self.sumMaxRewards)
        print('BanditTestBatch: random reward: %.1f' % self.sumRandomRewards)



#-- do not change this procedure --#
def generateBandits(all_cases, suppress_output = 0) :

    #user select which cases to generate
    generate_cases = [ all_cases[i] for i in range(len(all_cases)) ]   # all cases
    #generate_cases = [ all_cases[i] for i in (0,1,2) ] # example for an
                                                                         #arbitrary
                                                                                                                                             #set
                                                                                                                                             #of
                                                                                                                                             #cases

    #-- automatic generation --#

    total_num_cases = len(generate_cases)
    
    if(not suppress_output) :
        print('generateBandits(): generating %d specified cases ... ' % total_num_cases),

    cases = [BanditTestCase() for count in range(total_num_cases)]
    for c in range(total_num_cases) :
        cases[c].ID = c
        cases[c].numBandits = generate_cases[c][0]
        cases[c].maxPulls = generate_cases[c][1]
        if cases[c].numBandits != len(generate_cases[c][2]) :
            print('ERROR: generateBandits(): case %d : number of bandits does not match number of specified intervals' % c)
        elif cases[c].numBandits != len(generate_cases[c][3]) :
            print('ERROR: generateBandits(): case %d : number of bandits does not match number of specified probabilities' % c)

        cases[c].bandits = [BanditGenerator() for count in range(cases[c].numBandits)]
        for b in range(cases[c].numBandits) :
            cases[c].bandits[b].intervals = generate_cases[c][2][b]
            cases[c].bandits[b].probabilities = generate_cases[c][3][b]
            if len(cases[c].bandits[b].intervals) != len(cases[c].bandits[b].probabilities) :
                print('ERROR: generateBandits(): case %d bandit %d : number of intervals and probabilities does not match' % (c, b))
        
        cases[c].calcMaxReward()
        cases[c].calcRandomReward()

    if(not suppress_output) :
        print('generateBandits(): DONE\n')

    return cases
