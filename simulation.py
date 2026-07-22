from person import Person
from medium import Medium
from log import Log
from configuration import Configuration
import random
from datetime import datetime

class Simulation:
    persons_list: list[Person] #gives type hint: lets python know what this is suppose to be set to (when first creating this instance, python doesn't know the type yet)
    media_list: list[Medium]

    def __init__(self, persons: int, media: int, edges: int):
        self.persons_list = []
        self.media_list = []
        self.persons = persons
        self.edges = edges
        self.media = media
        self.log = Log() #creates Log instance

    def print(self): #calls print method for each agent on Agent class
        print("simulation persons:")
        for person in self.persons_list: #not i because not index but whole agent
            person.print()
        print("")
        print("simulation media:")
        for media in self.media_list:
            media.print()
        print("")

    def get_random_person(self):
        return random.choice(self.persons_list) #morwe direct than random.randint
    
    def run(self, times: int):
        count = 0
        for time in range(times):
            person1 = self.get_random_person()
            person2 = person1.get_random_neighbour()

            person1.communicate(person2)

            count += 1 #count up if person1 communicated with person 2

            for person in self.persons_list: #media consumption
                if abs(person.opinion - person.medium.opinion) < person.horizon:
                    person.communicate(person.medium)

                    count += 1 #count up if person communicated with media
    
        self.log.write(str(count) + " successful communication instances")

    def generate_edges(self):

        person1 = self.get_random_person()
        person2 = self.get_random_person()

        while person1 == person2:
            person2 = self.get_random_person()

        person1.add_neighbour(person2)
        person2.add_neighbour(person1)

    def setup(self):
        for i in range(self.persons): #generate agents
            self.persons_list.append(Person())

        self.log.write("Generated " + str(len(self.persons_list)) + " new agents") #Log already opens the file and adds timestamps

        for i in range(self.media): #generate media
            self.media_list.append(Medium())
        
        self.log.write("Generated " + str(len(self.media_list)) + " new media")

        for person in self.persons_list: #assign medium to person
            person.set_medium(random.choice(self.media_list))

        for i in range(self.edges): #generate edges
            self.generate_edges()

    def get_log(self): #self.log is created once in __init__ and get_log() gives other parts of the code access to that object when needed
        return self.log