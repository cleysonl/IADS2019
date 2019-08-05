# ------------------------------------------
# Tom Vodopivec
#
# IADS Analytics & Data Science Summer School 2019
# Course: Bandits, Learning, and Search
# 2019-08-05
#
# ------------------------------------------

from Agent import *
from BanditGenerator import *

def evaluateSingleCase(solver,                 # the MABsolver object (it incorporates algorithms for solving
                                               # the non-stohastic multi-armed
                                                                             # bandit
                                                                                                           # problem)
    case,                   # a multi-armed bandit problem
    suppress_output=0,    # enable/disable print output
    oracleProbablity=0    # gather bandits probability instead of -> can only be used on
                          # BanditGenerator() classes, so NOT on ONLINE (url)
                                                # scenarios
    ) :

    #init solver
    solver.reset(case.numBandits)

    #init stats
    total_reward = 0.0
    solver.max_pulls = case.maxPulls
    #compute single case evaluation
    for p in range(case.maxPulls) :
        selected_bandit = solver.selectAction()         #apply selection policy

        #get reward
        if(oracleProbablity == 0) :
            reward = case.pullBandit(selected_bandit, p)    # returns value 0 or 1
        else :
            reward = case.probBandit(selected_bandit, p)    # returns probability in the interval [0 , 1]


        solver.updateKnowledge(selected_bandit, reward)       #update solver stats
        total_reward += reward                          #sum of collected reward

    #output stats
    if not suppress_output:
        solver.infoStats()
        print('Total reward: ' + str(total_reward) + ' optimal reward: ' + str(case.maximumReward))

    return total_reward

def evaluate(solver,                 # the MABsolver object (it incorporates algorithms for solving
                                          # the non-stohastic multi-armed
                                                                   # bandit
                                                                                       # problem)
    batch,                  # batch of testing scenarios
    repeats,                # number of evaluative repeats
    suppress_output=0,    # enable/disable print output
    ) :

    metrics_labels = ['Sum rewards',
    'Regret',
    'Optimality [%]',
    'Random-normalized optimality [%]']

    metrics_shortLabels = ['   SumRew',
    '   Regret',
    '   Opt[%]',
    ' RNopt[%]']

    metrics_out_format = ['  %7.2f',
    '  %7.2f',
    '  %7.2f',
    '  %7.2f']

    #init performance metrics
    num_metrics = 2
        #0 - sum of rewards
        #1 - regret
        #2 - optimality factor (sum of rewards divided by maximum possible
        #reward) in %
        #3 - Random-normalized optimality in %

    metrics = [[0.0 for x in range(batch.num)] for x in range(num_metrics)]
    avg_metrics = [0.0 for x in range(num_metrics)]
    new_avg_metrics = [0.0 for x in range(num_metrics)]
    new_metrics = [0.0 for x in range(num_metrics)]

    #user output
    if not suppress_output :
        print('evaluate():')
        batch.info()
        print('Total repeats: %d' % repeats)
        print('')
        print('Batch performance                ',end="")
        print('By-case performance as: %s' % metrics_labels[0])
        print('')
        print('repeats ',end="")
        for i in range(num_metrics):
            print('%s' % metrics_shortLabels[i],end="")
        print('     ',end="")
        for c in range(batch.num) :
            print('   case%02d' % (c + 1),end="")
        print('')
        print('')

    #evaluate all cases
    for r in range(repeats) :

        #reset averaged (through cases) metrics
        for i in range(num_metrics):
            new_avg_metrics[i] = 0.0

        for c in range(0,batch.num) :
            #execute bandit game (case)
            new_result = evaluateSingleCase(solver, batch.list[c], 1, 0)

            #-- DEFINE HERE CUSTOM METRICS --#
            new_metrics[0] = new_result
            new_metrics[1] = (batch.list[c].maximumReward - new_result)
            #new_metrics[2] = new_result / batch.list[c].maximumReward * 100.0
            #new_metrics[3] = (new_result - batch.list[c].randomReward) /
            #(batch.list[c].maximumReward - batch.list[c].randomReward) * 100.0

            #update results by different metrics
            for i in range(num_metrics):
                metrics[i][c] +=  (1.0 / (r + 1.0)) * (new_metrics[i] - metrics[i][c])
                new_avg_metrics[i] += new_metrics[i]

        #calculate overall performance
        #new_avg_metrics[2] /= batch.num
        #new_avg_metrics[3] /= batch.num
        for i in range(num_metrics):
            avg_metrics[i]  += (1.0 / (r + 1.0)) * (new_avg_metrics[i] - avg_metrics[i])

        #user ouput
        if not suppress_output :
            print('%7d ' % (r + 1),end="")
            for i in range(num_metrics):
                print(metrics_out_format[i] % (avg_metrics[i]),end="")
            print('     ',end="")
            for c in range(batch.num) :
                print(metrics_out_format[0] % metrics[0][c],end="")
            print('')

    if not suppress_output :
        print('')
        print('evaluate(): DONE')
        print('')

    #returns
    #   measurements averaged over all cases
    #   measurements for each case individually
    return (avg_metrics, metrics)

