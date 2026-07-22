from agent import Agent

class Medium(Agent):
    def print(self):
        print("opinion: %.3f" % self.opinion)