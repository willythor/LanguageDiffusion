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


<<<<<<< HEAD
chart = ChartModule([{"Label": "Popular Word", "Color": "Black"}, {"Label": "Prominence", "Color": "Blue"}],
=======
chart = ChartModule([{"Label": "Herfindahl index", "Color": "Black"}],
>>>>>>> fef6df288a0dba994007d348c92a365d807bf044
                    data_collector_name='datacollector')


server = ModularServer(LanguageModel,
                       [grid, chart],
                       "Language Model",
                        50, 20, 20, discovery=.3)

server.port = 8889
server.launch()
