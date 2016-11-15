from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import *

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5,
                 "h": 0.5,
                 "w": 0.5}
   
    if str(type(agent)) == "<class 'model.FrenchAgent'>":
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
        portrayal["Shape"] = "rect"
        portrayal["h"] = .5
        portrayal["w"] = .5


    elif str(type(agent)) == "<class 'model.EnglishAgent'>":
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1

    return portrayal


grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)

server = ModularServer(LanguageModel,
                       [grid],
                       "Language Diffusion",
                       100, 100, 20, 20)

server.port = 8889
server.launch()