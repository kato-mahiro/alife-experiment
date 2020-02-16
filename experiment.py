import random
from operator import attrgetter
import copy
import sys

from setting import *
from modneat.modneat import agents
from task import Task_without_accident
from task import Task_with_accident

agents = agents.Agents('ExHebbianNetwork',POPULATION_SIZE,False,input_num=8,output_num=3, connection_num_lower_limit=40,connection_num_upper_limit=100)
is_accident = True

for gen in range(GENERATION_NUM):
    print('===')
    print('Gen:', gen)

    if is_accident == False:
        task = Task_without_accident()
    else:
        task = Task_with_accident()

    for pop in range(POPULATION_SIZE):
        agents[pop].fitness = task.dotask(agents[pop])

    print('max fitness:', agents.max_fitness)
    print('average fitness:', agents.average_fitness)
    print('minimum fitness: ', agents.min_fitness)

    if(agents.average_fitness > 52.0):
        is_accident = True

    agents.sort(key=attrgetter('fitness'), reverse =True)
    print(agents[0].histories[0])
    print(agents[0].histories[1])
    print(agents[0].histories[2])
    print(agents[0].histories[3])
    print(agents[0].histories[4])
    print(agents[0].histories[5])


    agents = agents.evolution_mgg(task=task.dotask,elite_num=2, mutate_prob=0.05, sigma=0.1)

name = sys.argv[1] + '.pickle'
agents.save_agents(name)
