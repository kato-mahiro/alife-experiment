import random
from setting import *
from modneat.modneat import agents
from task import Task_without_accident

agents = agents.Agents('ExHebbianNetwork',POPULATION_SIZE,True,input_num=8,output_num=3, connection_num_lower_limit=20,connection_num_upper_limit=100)

for gen in range(GENERATION_NUM):
    task = Task_without_accident()
    print('ベスト選択肢:', task.rewards.index(max(task.rewards)))
    for pop in range(POPULATION_SIZE):
        agents[pop].fitness = task.dotask(agents[pop])

    print('Gen:', gen)
    print('max fitness:', agents.max_fitness)
    print('average fitness:', agents.average_fitness)
    print(agents[random.randint(0, POPULATION_SIZE-1)].history)
    print('---')

    agents = agents.evolution_mgg(task=task.dotask,elite_num=2, mutate_prob=0.05, sigma=0.1)

    if(gen%100==0):
        agents[0].show_network()
