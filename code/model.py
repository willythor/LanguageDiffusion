from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
import numpy as np
import matplotlib.pyplot as plt
from mesa.datacollection import DataCollector
from itertools import count
graph = []
import time

class LanguageAgent(Agent):
    """An agent speaking a certain language"""
    def __init__(self,unique_id,model,discovery,movement):
        super().__init__(unique_id,model)
        self.objects = ["banana"]
        self.consanants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        self.vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
        self.wealth = 10
        self.discovery = discovery
        self.movement = movement

        #dict containing all the agent's known objects
        #where the value of each object is another dict containing all the ways the agent knows to say that object (i.e., the word for that object)
        #the value of each known word is the number of times the agent has been exposed to that word in an interaction
        self.language = {}

        #True when an agent is interacting with another agent
        self.interacting = False
    
    def step(self):

        if random.random() < self.movement:
        	self.move()


        #50 percent chance of agent discovering an object 

        if random.random() < self.discovery:

            discovery = random.choice(self.objects)

            #if agent has not discovered object, add it to language dict and then attempt to interact with a cellmate
            if discovery not in self.language:
                self.language[discovery] = {self.word_gen(): 1}    

            self.interact(discovery)
        if len(self.model.grid.get_neighbors(self.pos,moore=True,include_center=False)) > 0:

            try: 
                conversation_topic = random.choice(self.language)
                self.interact(conversation_topic)
            #agent can't have a conversation if it doesnt know any words
            except IndexError:
                pass
            except KeyError:
                pass

    def get_agent_popular_words(self):
        """
        Return this agents most popular words in a list of tuples.
        The tuple has a form (object, word)
        """
        pop_word_li = []

        for object_name in self.language:
            if len(self.language[object_name]) == 0:
                pop_word_li.append((object_name,None))
                continue
            pop_word_li.append((object_name, max(self.language[object_name], key = self.language[object_name].get)))

        return pop_word_li
 

    def interact(self, discovery):
        """models the interaction between two agents in the same cell
        """

        #keeps track of whether an agents word for an object has changed because of this interaction
        self_word_change = False
        peer_word_change = False

        #all the agents in the agents cell
        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        #A list of neighboring agents
        neighboring_agents = self.model.grid.get_neighbors(self.pos,moore=True,include_center=False)

        if len(neighboring_agents) > 0:
        
            self.interacting = True
            peer = random.choice(neighboring_agents)
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

def most_popular_banana(model):

    try:
        # print('hello')
        # print(model.get_most_popular_words()[0][1])
        graph.append(model.get_most_popular_words()[0][2])
        if model.get_most_popular_words()[0][2] == 50:
            print(graph)
            time.sleep(50)
        return model.get_most_popular_words()[0][2]
    except IndexError:
        # print('noooo')
        return 0

#Data collector function wrapper for get herfindahl index method
def get_h_index(model):
    try:
        print('returing ', model.get_herfindahl_index()["banana"])
        return model.get_herfindahl_index()["banana"]
    except KeyError:
        print('returning 0')
        return 0

class LanguageModel(Model):
    """A model simulating the language diffusion"""

    def __init__(self, N, width, height,discovery = .5,movement =.5):
        """
        N: Number of agents
        """

        self.num_agents = N
        #Grid third parameters - Boolean for wrapping around
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.discovery = discovery
        self.movement = movement

        #dict containing all the globally known objects
        #where the value of each object is another dict containing all the currently used words for that object
        #the value of each word is the number of agents who use that word
        self.global_languages = {}

        #Create agents
        #Add agents
        for i in range(self.num_agents):
            a = LanguageAgent(i,self,discovery = self.discovery,movement=self.movement)
            self.schedule.add(a)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x,y))


        #initialize data collector
        self.datacollector = DataCollector(
            #most popular word for all agents 
            #model_reporters={"Popular Word": most_popular_word},
            model_reporters={"Herfindahl index": get_h_index},
            agent_reporters={"Prominence": lambda a: a.wealth})




    def update_global_language(self):
        self.global_languages = {"banana": {}}#, "apple": {}, "pear": {}, "orange": {}}
        # self.global_languages = [{},{},{},{}]
        for agent in self.schedule.agents:
            for i in agent.get_agent_popular_words():
                object_name = i[0]
                object_word = i[1]
                if (object_word) is None:
                    continue
                self.global_languages[object_name][object_word] = self.global_languages[object_name].get(object_word, 0) + 1

       
    def get_most_popular_words(self):
        """
           Returns a list of most popular words and its frequency for each object in tuple form (object name, word, frequency)
        """ 
        pop_word_li = []
        for object_name in self.global_languages:
            if (len(self.global_languages[object_name]) == 0):
                pop_word_li.append((object_name, None, 0))
                continue
            #A word mapping that most number of agents in the model uses for a particular object
            most_pop_word = max(self.global_languages[object_name], key = self.global_languages[object_name].get)
            #A number of agents that use this word
            pop_word_freq = self.global_languages[object_name][most_pop_word]
            pop_word_li.append((object_name, most_pop_word, pop_word_freq))

        # print(pop_word_li)
        return pop_word_li

    def get_herfindahl_index(self):
        """
        Returns a dictionary of an object to its herfindahl index
        """
        d = {}
        for object_type in self.global_languages.keys():
            h_index = 0
            word_list = self.global_languages[object_type].keys()
            for word in word_list:
                h_index += (self.global_languages[object_type][word]/self.num_agents)**2
            d[object_type] = h_index
        return d
            
    def step(self):
        """Advance the model by one step"""
        self.datacollector.collect(self)
        self.update_global_language()
        #print(self.get_most_popular_words())
        self.schedule.step()
        #print(self.global_languages)
        print('current herfindahl index: ')
        print(self.get_herfindahl_index())
        print('\n\n\n')

if __name__ == '__main__':
	for disc in [1.0]:
		step_count = []
		for i in range(500):
			test_model = LanguageModel(50,20,20,discovery = disc)
			for step in count():
				if step > 50 and len(test_model.global_languages['banana']) == 1:
					step_count.append(step)
					break
				test_model.step()

		print(disc,np.mean(step_count))
