print('This is our script')import numpy as np

class Dog:
	def __init__(self):
		self.n_paws = 4
		self.n_ears = 2

	def bark(self):
		print('Woof')

	def get_number_of_paws(self):
		return self.n_paws

