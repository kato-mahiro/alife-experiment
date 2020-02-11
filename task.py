import random

class Task_without_accident:
    def __init__(self):
        self.rewards = [0.0, 0.3, 1.0]
        random.shuffle(self.rewards)

    def get_reward(self, no:int) -> float:
        return self.rewards[no]

"""
class Task_with_accident:
    def __init__(self):
        self.rewards = [0.0, 0.3, 1.0]
        random.shuffle(self.rewards)
        self.accident_generation_timings=[]
        new_accident_timing = random.randint(11,100)
"""
