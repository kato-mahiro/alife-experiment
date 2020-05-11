import random
from enum import IntEnum

from setting import *

class Rule(IntEnum):
    I   = 1
    II  = 2
    III = 3
    IV  = 4
    V   = 5
    VI  = 6

class Task_without_accident:
    def __init__(self, rule=None):
        if(rule == None):
            self.rule = Rule(random.randint(1,6))
        else:
            self.rule = rule

    def change_rule(self, rule=None):
        if(rule == None):
            self.rule = Rule(random.randint(1,6))
        else:
            self.rule = rule

    def get_reward(self, action: int, is_accident:bool = False) -> float:
        if(self.rule == Rule.I):
            reward_vec = [1.0, 0.3, 0.0]
        elif(self.rule == Rule.II):
            reward_vec = [1.0, 0.0, 0.3]
        elif(self.rule == Rule.III):
            reward_vec = [0.3, 1.0, 0.0]
        elif(self.rule == Rule.IV):
            reward_vec = [0.0, 1.0, 0.3]
        elif(self.rule == Rule.V):
            reward_vec = [0.3, 0.0, 1.0]
        elif(self.rule == Rule.VI):
            reward_vec = [0.0, 0.3, 1.0]
        if(is_accident):
            reward_vec = [0.0 if i == 1.0 else i for i in reward_vec]

        return reward_vec[ action ]

    def execute_task(self, agent) -> float:
        total_reward = 0
        agent.history = ''

        for i in range(STEP_NUM):
            #question phase
            input_vector = [1,0,0]
            tmp_output = agent.get_output_with_update(input_vector)
            output_vec = [0,0,0]
            action_id = tmp_output.index(max(tmp_output))
            output_vec[action_id] = 1
            previous_output = output_vec
            reward = self.get_reward(action = action_id, is_accident = False) 
            total_reward += reward

            if(reward == 1.0):
                agent.history += 'o'
                feedback_input = 1.0
            elif(reward == 0.3):
                agent.history += 'c'
                feedback_input = 0.0
            elif(reward == 0.0):
                agent.history += 'x'
                feedback_input = 0.0

            #feedback phase
            feedback_vector=[0,1,feedback_input]
            tmp_output = agent.get_output_with_update(feedback_vector)

        return total_reward

    def test_agent(self, agent, show_log = False):
        mean_reward = 0.0

        self.rule = Rule.I
        agent.reset()
        mean_reward += self.execute_task(agent)
        if(show_log):
            print('I: ',agent.history)

        self.rule = Rule.II
        agent.reset()
        mean_reward += self.execute_task(agent)
        if(show_log):
            print('II: ',agent.history)

        self.rule = Rule.III
        agent.reset()
        mean_reward += self.execute_task(agent)
        if(show_log):
            print('III: ',agent.history)

        self.rule = Rule.IV
        agent.reset()
        mean_reward += self.execute_task(agent)
        if(show_log):
            print('IV: ',agent.history)

        self.rule = Rule.V
        agent.reset()
        mean_reward += self.execute_task(agent)
        if(show_log):
            print('V: ',agent.history)

        self.rule = Rule.VI
        agent.reset()
        mean_reward += self.execute_task(agent)
        if(show_log):
            print('VI: ',agent.history)
        
        if(mean_reward != 0.0): mean_reward /= 6.0
        return mean_reward

if __name__=='__main__':
    t = Task_without_accident()
    print(t.rule)
    reward = t.get_reward(1)
    print(reward)
    reward = t.get_reward(1,True)
    print(reward)
