import random
from operator import attrgetter
import copy
import sys

from setting import *
from modneat.modneat import agents
from task import Task_without_accident
from task import Task_with_accident

agents = agents.read_agents('result/5.pickle')
agent = agents[0]
agent.show_network()
task = Task_with_accident()

for i in range(20):
    agent.fitness = task.dotask(agent)
    print(agent.fitness)
    #print(agent.histories[0])
    #print(agent.histories[1])
    print(agent.histories[2])
    print(agent.histories[3])
    #print(agent.histories[4])
    #print(agent.histories[5])
    print("---")
