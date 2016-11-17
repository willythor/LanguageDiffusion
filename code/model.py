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
        self.language = {}
        self.interacting = False
    
    def step(self):
        self.move()
        if random.choice([True, False]):
            discovery = random.choice(self.objects)
            if discovery in self.language:
                self.interact(discovery)
            else:
                self.language[discovery] = {self.word_gen(): 1}
                self.interact(discovery)

    def interact(self, discovery):

        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        if len(cellmates) > 1:
            self.interacting = True

            peer = random.choice(cellmates)
            peer.interacting = True

            self_word = max(self.language[discovery], key = self.language[discovery].get)

            if discovery in peer.language:

                peer_word = max(peer.language[discovery], key = peer.language[discovery].get)

                if self_word in peer.language[discovery]:
                    peer.language[discovery][self_word] += 1

                elif peer_word in self.language[discovery]:
                    self.language[discovery][peer_word] += 1

            else: 
                peer.language[discovery] = {max(self.language[discovery], key = self.language[discovery].get): 1}
                peer_word = self_word

            # print('peer: ' + discovery + " = " + max(peer.language[discovery], key = peer.language[discovery].get))
            # print('instigator ' + discovery + " = " + max(self.language[discovery], key = self.language[discovery].get))

            #update master list in model
            #if object not in master list, add it
            if discovery in self.model.language:
                #if peer or self word in master language, increment it, else add it
                if peer_word in self.model.language[discovery]:
                    self.model.language[discovery][peer_word] += 1
                elif peer_word not in self.model.language[discovery]:
                    self.model.language[discovery][peer_word] = 1

                if self_word in self.model.language[discovery]:
                     self.model.language[discovery][self_word] += 1
                elif self_word not in self.model.language[discovery]: 1

            #if word not in master list, add self_word twice because it's now shared by the two agents in this interaction
            else:
                self.model.language[discovery] = {self_word: 2}


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

class LanguageObject(Agent):
    """An object that an agent identifies"""
    def __init__(self):
        self.name = "banana"

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
        self.language = {}



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
