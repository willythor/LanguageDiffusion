Github: <https://github.com/willythor/LanguageDiffusion>


# A Simple Model for Language Formation
## Sungwoo Park, Willem Thorbecke, Ziyu Selina Wang
## Team Name: Shoots Den!




### Abstract:
This model investigates the process of language formation through the use of an agent-based model. Each agent in the model starts with no language at all and gradually builds their vocabulary through interaction with other agents. The formation and variation of the vocabulary follows a set of simple rules. We aim to provide an explanatory model that can be used to show a set of factors that explain the rate and process of language formation. One of our results models real world behavior by showing slow convergence upon a single language when the mobility of our agents is limited. This coincides with how humans having limited mobility (some more than other) results in slow convergence upon a single language, but convergence nonetheless. This is evident during colonization, for example in Hawaii native Hawaiian speakers currently account for 0.1% of the state population compared to nearly 100% years prior to U.S. occupation. 






###Experiments:
The language formation model that we create is inspired by and loosely based on a similar experiment from “A Self Organizing Spatial Vocabulary” (Steels, 1995). The paper defines a set of rules that governs the interactions between agents that lead to the formation of a shared language. 


In our model, a language is defined as a random sequence of three letters that an agent uses to refer to a certain object. Agents have no language to start with and there is a predefined list of objects that they can discover. At each step of the simulation, an agent has a user-defined chance of discovering an object. When an agent discovers an object, it generates a random letter sequence as a “word” for that object and uses that word to refer to that object in future interactions with other agents.


Also at each time step the agents move to a random neighboring location. Then each agent checks to see if there are neighboring agents and picks a random one to have a conversation with. The conversation is the sharing of the word that each agent is using to refer to a certain object of their choice. If both of the agents (initiator and receiver of the conversation) do not have any words in their vocabulary referring the said object, nothing happens. If one of the agents do not have a word referring to the object, then that agent learns the word from the other agent. If both agents have a word for the object and the words are different, each agent adds the word that other agent is using to its “word bank.” The word bank is a collection of all the words that are being used to refer to a certain object that the agent has heard. After the interaction, the word that an agent uses to refer to an object is the word that has highest frequency in its “word bank” - a word for the object that the agents has heard the most.


Using this model we answer questions that both pertain to real world language evolution and are relevant to the scope of our model.


###Question, Methodology, Results, and Interpretation


First, we want to make sure that our model does produce an unified language.


**Question**: 
Does our model result in the formation of an unified language?


**Methodology**: 
We run the model explained above with 50% chance of discovering an object. To quantitatively observe the process of the formation of an unified language, we monitor the [Herfindahl Index](https://en.wikipedia.org/wiki/Herfindahl_index).  For the sake of simplification, there is only one object in this simulation.


**Results**:
For the simulation of 50 agents in the grid of 20 by 20, the Herfindahl index reached 1, meaning everyone uses same word to refer to the object, after 134 steps. 


![dist](herfindahl_indicies.jpg)
*Graph of change in the Herfindahl index over time*


**Interpretation**:
We expect the model to produce an uniform language and the result above confims our expectation. Given enough time for the agents to interact with each other, the words that agents use converge into single dominant word. 






Now that we know our model does produce convergence, we want to investigate the effect of different parameters on the time it takes to reach convergence. One of such parameters is the odds of discovering an object at each time step.


**Question**: 
How object-discovery odds affect the time it takes to reach word convergence?
**Methodology**
At each step we defined the chance of an agent discovering a new object. We swept through odds of discovery being 10% all the way up to 100%, incrementing by steps of 10%. For each new chance of discovery we ran 500 trials and took the average as a result.
**Results**
![dist](discovery.png)
*Graph of the number of steps till convergence with varing object discovery odds*

**Interpretation**
The figure shows that the higher the odds of discovering a new object, the faster the agents can converge on a single word for a given object. Higher odds of discovering a new object result in more words being generated during each of the early time steps, and more words for a given object should mean slower convergence right? No. If discovery odds are too low then agents take a long time to come up with words for a given object: an agent has to discover an object before it can name it. Thus many interactions between agents result in empty interactions where no words/objects are exchanged, slowing down the rate of convergence.






Another parameter of interest is the mobility of each agent. 


**Question**:
How does mobility of the agents affect the time it takes to reach word convergence?
**Methodology**
At each step we specified a the chance of movement for each agent. We swept through the odds of movement being 10% all the way up to 100%, incrementing by steps of 10%.  
**Results**
![dist](mobility.png)
*Graph of the number of steps till convergence with varing agent mobility*

**Interpretation**
It takes a long time for a grid of agents to converge on a single word for a given object if the agents have low mobility. The results validate our hypothesis that the higher the mobility, the shorter it takes to reach convergence. With no mobility there is no convergence because each agent can only interact with its neighbors but not people from the other parts of the grid.  When agents have high mobility the rate of diffusion of vocabulary is very quick, because popular words from one area of a grid spread to the rest of the grid faster than when agents have low mobility. As stated in the abstract, this results coincides with historical moments of high mobility, such as colonization, resulting in language conversion.






### Conclusion:
Through an agent-based model with simple rules that are loosely based on how people communicate in real life, we modeled the process of language evolution. In our model we observed a key characteristic of language evolution - convergence of multiple languages upon a single dominant language. We ran a number of experiments by modifying object-discovery-odds as well as agent mobility and thus observed that a population with high discovery odds and high mobility has faster language convergence. These results are loosely reflective of real world language behavior - specifically higher mobility resulting in faster language convergence. This can be best observed during colonial times when a colonized community takes on the language of the settlers. 






### Bibliography:


**A Javascript Implementation of Agent-based Simulation in Language Evolution**


<https://fatiherikli.github.io/language-evolution-simulation/>


This is a link to a javascript implementation of an agent-based simulation in language evolution context. Even though this is not an academic paper, the experiment that this simulation is replicating is very relevant to the topic that we are trying to investigate. In this agent-based model, there is a number of agents from three distinct islands with different vocabularies. The experiment simulates the random interactions between those agents and introduces the mutations among the vocabularies. It does not seem like this simulation has a meaningful interpretation or result, so it would be our job to extend this simulation by adding more detailed agent interactions and observing the result to come up with a meaningful conclusion.


**Lekvam, Gamback, Bungum, "Agent-based modeling of Language Evolution"**


<http://www.aclweb.org/anthology/W14-0510>


This paper models the process of language evolution through a simulation model called a language game simulation. In this model, artificial agents interact with each other to reach a cooperative goal: to create a shared language. Based on a certain set of rules, agents attempt a conversation. If both agents can understand the conversation, the conversation becomes a part of the language. If a conversation isn’t successful, the agents attempt to create a new set of words that other agent would be able to understand.


**Berrah, Glotin, Laboissiere, Bessiere, Boe, "From Form to Formation of Phonetic Structures: An evolutionary computing perspective"**


<http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=237E415FCEE4528600B201AC44CB51A0?doi=10.1.1.54.7332&rep=rep1&type=pdf>


This paper explores the evolution of phonetics using a society of speech robots. One such experiment in this paper used machine learning to create a function that takes as an input vowel sounds and outputs a metric of difficult to expose a more prominent explanation of why certain vowel sounds are so prominent. This experiment used machine learning to parameters including lips, jaw, larynx, and tongue, to correctly model the difficulty of each vowel sound. The paper concluded that a large factor in the popularity of a given syllable was the acoustic efficiency and articulatory cost of said syllable.


**Luc Steels, “The synthetic modeling of language origins”**


<https://www.csl.sony.fr/downloads/papers/1997/web-coe.pdf>


This paper delves into the various aspects of the formation of a language. This includes the fact that language is diffused in a cultural manner instead of in a generic fashion (memetic). Language evolution is also a product of factors such as communicative success, and a minimization of brain processing. Thus language is often a product of functionality more than anything else. The paper was more or less inconclusive, but stated that the three main areas of research that seem most promising are genetic evolution, cultural adaptation, and genetic assimilation.


**Luc Steels, "A Self Organizing Spatial Vocabulary"**


<https://ai.vub.ac.be/sites/default/files/Steels%20-%201995%20-%20A%20Self-Organizing%20Spatial%20Vocabulary.pdf>


The experiment that this paper is presenting is an agent-based model that simulates the evolution and adaption of a language. In this model, agents are programmed to attempt a conversation with a different agent in the model and communicate the location of other agents. In the very beginning of the simulation, the agents do not have any words in their language. As a model progresses, the agents interact with other agents and develop a set of words that have spatial meanings (ex. left, right, front, etc) to help them communicate with other agents.


