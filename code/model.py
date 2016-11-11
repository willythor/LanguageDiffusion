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
    
    def step(self):
        pass

    def move(self):
        neighbors = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        new_position = random.choice(neighbors)
        self.model.grid.move_agent(self, new_position)

class EnglishAgent(LanguageAgent):
    """An agent speaking English"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id,model)
        language = 'English'

class FrenchAgent(LanguageAgent):
    """An agent speaking French"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id,model)
        language = 'French'

class LanguageModel(Model):
    """A model simulating the language diffusion"""
    def __init__(self, engN, frN, width, height):
        """
            engN: Number of EnglishAgent to create
            frN: Number of FrenchAgent to create
        """
        self.num_english = engN
        self.num_french = frN
        self.num_agents = engN + frN
        #Grid third parameters - Boolean for wrapping around
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        #Create agents
        #Add english agents to upper left corner and french agents to lower right corner
        for i in range(self.num_english):
            a = EnglishAgent(i,self)
            self.schedule.add(a)
            x = random.randrange(self.grid.width//2)
            y = random.randrange(self.grid.height//2)
            self.grid.place_agent(a, (x,y))
        for i in range(self.num_french):
            a = FrenchAgent(self.num_english+i,self)
            self.schedule.add(a)
            x = random.randrange(self.grid.width//2,self.grid.width)
            y = random.randrange(self.grid.height//2,self.grid.height)
            self.grid.place_agent(a, (x,y))
        
    def step(self):
        """Advance the model by one step"""
        self.schedule.step()

if __name__ == '__main__':
    example_model = LanguageModel(10,10,20,20)
    example_model.step()

    agent_counts = np.zeros((example_model.grid.width, example_model.grid.height))
    for cell in example_model.grid.coord_iter():
        cell_content, x, y = cell
        agent_count = len(cell_content)
        agent_counts[x][y] = agent_count
    plt.imshow(agent_counts, interpolation='nearest')
    plt.colorbar()
    plt.show()
