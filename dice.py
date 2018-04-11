from random import randint


class Dice:
	"""骰子类"""

	def __init__(self, num_sides=6):
		"""骰子有6面"""
		self.num_sides = num_sides

	def roll(self):
		"""获取骰子点数"""
		return randint(1, self.num_sides)
