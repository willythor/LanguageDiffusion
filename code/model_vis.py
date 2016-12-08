from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import *
from mesa.visualization.modules import ChartModule


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5,
                 "h": 0.5,
                 "w": 0.5}
   
    if agent.interacting:
        portrayal["Color"] = "blue"
     
    return portrayal


grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)


chart = ChartModule([{"Label": "Herfindahl index", "Color": "Black"}],
                    data_collector_name='datacollector')


server = ModularServer(LanguageModel,
                       [grid, chart],
                       "Language Model",
                        50, 20, 20)

server.port = 8889
server.launch()
