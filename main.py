# Perceptron OCR Project
# Author: Fernando Terra
# Date: 2018 APR 18

import sys
import random
from datetime import datetime
#from helpers import *

class Perceptron:
	def __init__(self, patterns, outputs, lr=0.5, epochs=2000, threshold=1):
		self.patterns = patterns
		self.outputs = outputs
		self.lr = lr
		self.epochs = epochs
		self.threshold = threshold
		self.n_patterns = len(patterns)
		self.n_attribute = len(patterns[0])
		self.weight = []

	def training(self):
		print('Training started...')
		for pattern in self.patterns:
			pattern.insert(0, self.threshold)

		print('Initializing weights...')
		for i in range(self.n_attribute):
#                       TODO: Uncomment line below to generate random values to initial weights
#                       self.weight.append(random.random())
#                       TODO: Uncomment line below to generate weights with value equal zero
			self.weight.append(0)

		self.weight.insert(0, self.threshold)
		print('Weights ... OK')
		n_epochs = 0

		while(True):
			error = False
			for i in range(self.n_patterns):
				u = 0
				for j in range(self.n_attribute + 1):
					u += self.weight[j] * self.patterns[i][j]

				y = self.signal(u)
				if y != self.outputs[i]:
					error_aux = self.outputs[i] - y
					for j in range(self.n_attribute + 1):
						self.weight[j] = self.weight[j] + self.lr * error_aux * self.patterns[i][j]
					error = True

				error_aux = self.outputs[i] - y
#				print('error = ', error_aux)

				n_epochs += 1

			print('Interations = ', n_epochs)
			if error or n_epochs >= self.epochs:
				break

	def signal(self, u):
		return 1 if u >= 0 else -1

	def evaluate(self, pattern):
		pattern.insert(0, self.threshold)
		u = 0

		for i in range(self.n_attribute + 1):
			print('weight', i,' = ', self.weight[i])
			u += self.weight[i] * pattern[i]

		y = self.signal(u)
		print('Classe: %d' % y)



pattern = []
#pattern = [[0.72, 0.82], [0.91, -0.69],
#	[0.46, 0.80],   [0.03, 0.93],
#	[0.12, 0.25],   [0.96, 0.47],
#	[0.8, -0.75],   [0.46, 0.98],
#	[0.66, 0.24],   [0.72, -0.15],
#	[0.35, 0.01],   [-0.16, 0.84],
#	[-0.04, 0.68],  [-0.11, 0.1],
#	[0.31, -0.96],  [0.0, -0.26],
#	[-0.43, -0.65], [0.57, -0.97],
#	[-0.47, -0.03], [-0.72, -0.64],
#	[-0.57, 0.15],  [-0.25, -0.43],
#	[0.47, -0.88],  [-0.12, -0.9],
#	[-0.58, 0.62],  [-0.48, 0.05],
#	[-0.79, -0.92], [-0.42, -0.09],
#	[-0.76, 0.65],  [-0.77, -0.76]]
#output = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# GATE AND
pattern = [[-1,-1],[-1,1],[1,-1],[1,1]]
#output = [-1,-1,-1,1]

# GATE XOR
output = [-1,1,1,-1]

net = Perceptron(pattern, output)

#log = Helpers()
net.training()
net.evaluate([1,-1])
#net.evaluate([0.56, 2.80, -1.9])

sys.exit('End of algorithm')
