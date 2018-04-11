import matplotlib.pyplot as plt
import pygal

from random_walk import RandomWalk

rw = RandomWalk(10000)
rw.fill_walk()

# 利用matplotlib可视化
# 设置绘图窗口的尺寸
plt.figure(figsize=(10, 6), dpi=128)

c_numbers = list(range(rw.walk_numbers))
plt.scatter(rw.x_value, rw.y_value, s=1,
			c=c_numbers, cmap=plt.cm.Reds, edgecolors='none')
# 突出起点和终点
plt.scatter(rw.x_value[0], rw.y_value[0], s=10,
			c='blue', edgecolors='none')
plt.scatter(rw.x_value[-1], rw.y_value[-1], s=10,
			c='green', edgecolors='none')

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_xaxis().set_visible(False)

plt.savefig('random_walk_visual.png')


# 利用pygal可视化
histogram = pygal.XY()

histogram.title = "Random Walk"

values = []
for num in range(rw.walk_numbers):
	values.append((rw.x_value[num], rw.y_value[num]))

histogram.add('step', values)
histogram.render_to_file('random_walk_visual.svg')