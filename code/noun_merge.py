# --*-- encoding: iso-8859-1 --*--

# Mutation of a vowel sound with 0.1 probability
# Mutation of a const sound with 0.1 probability
# Compounding with another word with 0.1 probability
# Without any mutation

import numpy as np

class Pidgin:
	"""defines interactions between languages"""

	def __init__(self):
		self.data = []

	def combine_langs(self, lang1, lang2):
		return ''

		output_lang = []
		
		for i, word in enumerate(lang1):

			word1 = lang1[i]
			word2 = lang2[i]

			np.random()

			if len(word1) > len(word2):
				output_lang.append(word2)

			elif len(word1) < len(word2):
				output_lang.append(word2)

			else:
				output_lang.append(word1)

		return output_lang

#a class for each language?
#a class for mashing??

class French:

	self.prominence = .5
	nouns = "Temps personne annee maniere jour chose chose homme monde vie main partie enfant oeil femme place travail semaine cas point gouvernement societe numero groupe probleme fait".split()

	def __init__(self):
		self.data = []


class English: 

	self.prominence = .5
	nouns = "time person year way day thing man world life hand part child eye woman place work week case point government company number group problem fact".split()
