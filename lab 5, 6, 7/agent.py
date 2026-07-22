import random
import math

class Agent:
    neighbours: list[Agent]
    
    def __init__(self):
        self.opinion = random.uniform(-1,1)
        self.neighbours = []

    def calculate_mu(self, other: Agent):
        mu = 0.5 * math.tanh(len(other.neighbours) / (20 * (other.opinion - self.opinion) ** 2))
        return mu
    
    def add_neighbour(self, other: Agent):
        self.neighbours.append(other)
    
    def get_random_neighbour(self):
        neighbour = random.choice(self.neighbours)
        return neighbour 
    

# No methods to address duplicates (i.e., the same person being added twice to neighbour list)
# No methods to check if a person is already in a neighbours listpe