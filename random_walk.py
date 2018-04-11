from random import choice


class RandomWalk:
	"""生成随机漫步的类"""

	def __init__(self, walk_numbers=5000):
		"""初始化随机漫步属性"""
		self.walk_numbers = walk_numbers

		# 存储漫步的横纵坐标列表，随机漫步开始于(0, 0)
		self.x_value = [0]
		self.y_value = [0]

	def fill_walk(self):
		"""计算随机漫步的所有点"""

		# 不断漫步，直到到达步数
		while len(self.x_value) < self.walk_numbers:

			# 调用get_step()，获取前进方向及距离
			x_step = self.get_step()
			y_step = self.get_step()

			# 拒绝原地踏步
			if x_step == 0 and y_step == 0:
				continue

			# 计算下一步的横纵坐标
			# 用列表最后一项加上新的步数
			next_x = self.x_value[-1] + x_step
			next_y = self.y_value[-1] + y_step

			self.x_value.append(next_x)
			self.y_value.append(next_y)

	def get_step(self):
		"""获取前进方向和距离"""
		direction = choice([-1, 1])
		distance = choice(range(0, 6))
		step = direction * distance

		return step