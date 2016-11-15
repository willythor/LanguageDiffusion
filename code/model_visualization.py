from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model import *

def agent_portrayal(agent):
	portrayal = {"Shape": "circle",
				 "Color": "red",
				 "Filled": "true",
				 "Layer": 0,
				 "r": 0.5}
	return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(LanguageModel,
                       [grid],
                       "Language Model",
                       25, 25, 10, 10)
server.port = 8889
server.launch()