import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = list(x**2 for x in range(1, 1001))

# 绘制线，linewidth代表线条粗细
# plt.plot(x_values, y_values, linewidth=2)
# 绘制点，s代表点大小, edgecolor代表点的轮廓颜色，
# c代表点颜色可用（a, b, c）表示，取值范围0～1，0代表最深。
# 或者使用颜色映射，c设置为映射数值列表，cmap为映射颜色
plt.scatter(x_values, y_values, s=10, edgecolors='none',
			c=x_values, cmap=plt.cm.Reds)

# 设置图标标题，坐标轴标签
plt.title("Square Numbers", fontsize=16)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of Value", fontsize=16)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=10)
# 设置坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])

# 保存文件到本目录下，bbox_inches='tight'表示裁边
plt.savefig('squares_plot.png', bbox_inches='tight')
# 显示图形
plt.show()
