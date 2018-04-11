import pygal
import matplotlib.pyplot as plt
from dice import Dice

# 创建一个6面骰子和掷骰子结果的列表
dice1 = Dice(6)
dice2 = Dice(10)

# 掷一定次数骰子，并存储结果
results = []

for roll_num in range(5000):
	result = dice1.roll() + dice2.roll()
	results.append(result)

# 分析结果
frequencies = []
max_results = dice1.num_sides + dice2.num_sides
for value in range(1, max_results + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

# 对结果进行可视化
# 建立直方图
histogram = pygal.Bar()

histogram.title = "Results of rolling one D6+D10 5000 times."
histogram.x_title = "Result"
histogram.y_title = "Frequency of Result"
histogram.x_labels = list(range(2, max_results + 1))
# 将值传入相应标签中
histogram.add(title='D6+D10', values=frequencies)

histogram.render_to_file('dice_visual.svg')

# 使用matplotlib可视化
# 注意x和y的列表长度要相等
plt.figure(figsize=(10, 6), dpi=128) # 要放在前面
x_value = list(range(1, max_results + 1))
y_value = frequencies

plt.plot(x_value, y_value, linewidth=2)
plt.scatter(x_value, y_value, s=10, c='red',
			edgecolors='none')
plt.title("Results of rolling one D6+D10 5000 times.",
		  fontsize=16)
plt.xlabel("Result", fontsize=16)
plt.ylabel("Frequency of Result", fontsize=16)

plt.tick_params(axis='both', labelsize=10)

plt.savefig('dice_visual.png', bbox_inches='tight')
