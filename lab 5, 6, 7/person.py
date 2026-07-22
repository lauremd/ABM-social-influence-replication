from agent import Agent
from medium import Medium
import random

class Person(Agent):
    def __init__(self):
        super().__init__() #set opinion
        self.convergence = random.uniform(0,2)
        self.repulsion = random.uniform(self.convergence, 2) 
        self.horizon = random.uniform(0, 2)
        self.medium = None
    
    def set_medium(self, medium: Medium): #setter, assigns medium to person
        self.medium = medium

    def print(self):
        print("opinion: %.3f; convergence: %.3f; repulsion: %.3f" % (self.opinion, self.convergence, self.repulsion))

    def communicate(self, other: Agent):
        influence_coefficient = self.calculate_mu(other)
        abs_diff = abs(self.opinion - other.opinion)
        if abs_diff <= self.convergence:
            self.opinion = self.opinion + influence_coefficient * (other.opinion- self.opinion)
        elif abs_diff > self.repulsion:
            self.opinion = self.opinion - influence_coefficient * (other.opinion - self.opinion) * (1-abs(self.opinion))