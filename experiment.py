import random
from operator import attrgetter
import copy
import sys

from setting import *
from modneat.modneat import agents
from accident_task import Task_without_accident
#from accident_task import Task_with_accident

agents = agents.Agents('ExHebbianNetwork',
                        POPULATION_SIZE,
                        is_automatic_change = False,
                        input_num=8,
                        output_num=3,
                        normal_num_upper_limit = 20,
                        modulation_num_upper_limit = 10,
                        neuron_num_upper_limit = 20,
                        connection_num_lower_limit=10,
                        connection_num_upper_limit=100
                    )
is_accident = False

for gen in range(GENERATION_NUM):
    print('===')
    print('Gen:', gen)

    if is_accident == False:
        task = Task_without_accident()
    else:
        task = Task_with_accident()
    
    for pop in range(POPULATION_SIZE):
        task.change_rule()
        agents[pop].fitness = task.test_agent(agents[pop])

    print('max fitness:', agents.max_fitness)
    print('average fitness:', agents.average_fitness)
    print('minimum fitness: ', agents.min_fitness)

    if(agents.max_fitness >= 8.1):
        print('Successfully evolved')
        agents.sort(key=attrgetter('fitness'), reverse =True)
        task.test_agent(agents[0],True)
        agents[0].show_network()
        sys.exit()

    agents.sort(key=attrgetter('fitness'), reverse =True)
    task.test_agent(agents[0], True)
    agents = agents.evolution_mgg(task=task.test_agent,elite_num=2, mutate_prob=0.05, sigma=0.1)

name = sys.argv[1] + '.pickle'
agents.save_agents(name)
