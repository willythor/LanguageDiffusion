from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
import numpy as np
import matplotlib.pyplot as plt

class LanguageAgent(Agent):
    """An agent speaking a certain language"""
    def __init__(self,unique_id, model):
        super().__init__(unique_id,model)
        self.objects = ["banana", "apple", "pear", "orange"]
        self.consanants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        self.vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
        
        #dict containing all the agent's known objects
        #where the value of each object is another dict containing all the ways the agent knows to say that object (i.e., the word for that object)
        #the value of each known word is the number of times the agent has been exposed to that word in an interaction
        self.language = {}

        #True when an agent is interacting with another agent
        self.interacting = False
    
    def step(self):
        self.move()

        #50 percent chance of agent discovering an object 
        if random.choice([True, False]):

            discovery = random.choice(self.objects)

            #if the agent has already discovered this object, then attempt to interact with a cellmate
            if discovery in self.language:
                self.interact(discovery)

            #if agent has not discovered object, add it to language dict and then attempt to interact with a cellmate
            else:
                self.language[discovery] = {self.word_gen(): 1}
                self.interact(discovery)

    def interact(self, discovery):

        #all the agents in the agents cell
        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        if len(cellmates) > 1:
        
            self.interacting = True
            peer = random.choice(cellmates)
            peer.interacting = True

            #from the agent's language dict, selects the most popular word for the discovered object
            self_word = max(self.language[discovery], key = self.language[discovery].get)

            if discovery in peer.language:

                #selects the peer's most popular word choice for the discovered object
                peer_word = max(peer.language[discovery], key = peer.language[discovery].get)

                #if the agents possess each other's words, then increment the popularity of those words
                if self_word in peer.language[discovery]:
                    peer.language[discovery][self_word] += 1

                if peer_word in self.language[discovery]:
                    self.language[discovery][peer_word] += 1

                #if the agents don't possess each other's words, then add them to each other's language
                if self_word not in peer.language[discovery]:
                    peer.language[discovery][self_word] = 1

                if peer_word not in self.language[discovery]:
                    self.language[discovery][peer_word] = 1

            else: 
                #if peer doesn't know this object, add it to peer's langauge
                peer.language[discovery] = {max(self.language[discovery], key = self.language[discovery].get): 1}
                peer_word = self_word


            #update global languages dict in model
            #if object not in global languages dict, add it
            if discovery in self.model.global_languages:
                #if peer or self word in master language, increment it, else add it
                if peer_word in self.model.global_languages[discovery]:
                    self.model.global_languages[discovery][peer_word] += 1
                elif peer_word not in self.model.global_languages[discovery]:
                    self.model.global_languages[discovery][peer_word] = 1

                if self_word in self.model.global_languages[discovery]:
                    self.model.global_languages[discovery][self_word] += 1
                elif self_word not in self.model.global_languages[discovery]: 1

            #if word not in master list, add self_word twice because it's now shared by the two agents in this interaction
            else:
                self.model.global_languages[discovery] = {self_word: 2}


    def word_gen(self):        
        l1 = random.choice(self.consanants)
        l2 = random.choice(self.vowels)
        l3 = random.choice(self.consanants)
        return l1+l2+l3
            
    def move(self):
        neighbors = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        new_position = random.choice(neighbors)
        self.model.grid.move_agent(self, new_position)
        self.interacting = False

class LanguageModel(Model):
    """A model simulating the language diffusion"""

    def __init__(self, N, width, height):
        """
            engN: Number of EnglishAgent to create
            frN: Number of FrenchAgent to create
        """

        self.num_agents = N
        #Grid third parameters - Boolean for wrapping around
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        #dict containing all the globally known objects
        #where the value of each object is another dict containing all the currently used words for that object
        #the value of each word is the number of agents who use that word
        self.global_languages = {}



        #Create agents
        #Add agents
        for i in range(self.num_agents):
            a = LanguageAgent(i,self)
            self.schedule.add(a)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x,y))


        # #how to collect data!???
        # self.datacollector = DataCollector(
        # model_reporters={"Gini": compute_gini})
        
    def step(self):
        """Advance the model by one step"""
        print(self.language)
        self.schedule.step()




if __name__ == '__main__':
    example_model = LanguageModel(10,20,20)
    #example_model.step()

    for i in range(5):

        agent_counts = np.zeros((example_model.grid.width, example_model.grid.height))
        for cell in example_model.grid.coord_iter():
            cell_content, x, y = cell
            if not cell_content:
                agent_counts[x][y] = 1
            #agent_count = len(cell_content)
            #agent_counts[x][y] = agent_count
        plt.imshow(agent_counts, interpolation='nearest')
        plt.colorbar()
        plt.show()
        example_model.step()
