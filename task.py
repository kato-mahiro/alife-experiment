import random
from setting import *

class Task_without_accident:
    def __init__(self):
        self.rewards = [0.0, 0.3, 1.0]
        random.shuffle(self.rewards)

    def get_reward(self, no:int) -> float:
        return self.rewards[no]

    def dotask(self,agent):
        total_reward = 0
        agent.history = ''
        for step in range(STEP_NUM):

            """
            if(step % 50 == 0):
                pre_rewards = self.rewards[:]
                while( self.rewards.index(max(self.rewards)) == pre_rewards.index(max(pre_rewards)) ):
                    random.shuffle(self.rewards)
            """
            #question phase
            input_vector = [1,0,0,0,0,0,0,0]
            output = agent.get_output_with_update(input_vector)
            output_vec = [0,0,0]
            output_vec[output.index(max(output))] = 1
            previous_output = output_vec
            reward = self.rewards[ output_vec.index(max(output_vec)) ]
            total_reward += reward

            if(reward == 0.0):
                agent.history += 'x'
                feedback = [1,0,0]
            elif(reward == 0.3):
                agent.history += 'c'
                feedback = [0,1,0]
            elif(reward == 1.0):
                feedback = [0,0,1]
                agent.history += 'o'

            #feedback phase
            feedback_vector=[0,1]
            feedback_vector += previous_output
            feedback_vector += feedback
            output = agent.get_output_with_update(feedback_vector)

        return total_reward

"""
class Task_with_accident:
    def __init__(self):
        self.rewards = [0.0, 0.3, 1.0]
        random.shuffle(self.rewards)
        self.accident_generation_timings=[]
        new_accident_timing = random.randint(11,100)
"""
