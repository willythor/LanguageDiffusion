from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid
import random
import numpy as np
import matplotlib.pyplot as plt

class LanguageAgent(Agent):
    """An agent speaking a certain language"""
    def __init__(self,unique_id, model):
        super().__init__(unique_id,model)
    
    def step(self):
        self.move()

    def move(self):
        neighbors = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        new_position = random.choice(neighbors)
        if self.model.grid.is_cell_empty():
            self.model.grid.move_agent(self, new_position)

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
        self.grid = SingleGrid(width, height, True)
        self.schedule = RandomActivation(self)

        #Create agents
        #Add english agents to upper left corner and french agents to lower right corner
        for i in range(self.num_agents):
            a = LanguageAgent(i,self)
            self.schedule.add(a)
            x, y = self.grid.find_empty()
            self.grid.place_agent(a, (x,y))
        
    def step(self):
        """Advance the model by one step"""
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
