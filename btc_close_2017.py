import json, pygal, math

filename = 'data/btc_close_2017.json'
dates = []
months = []
weeks = []
weekdays = []
closes = []

with open(filename) as f:
	btc_data = json.load(f)
	for btc_dict in btc_data:
		# 每一天的信息
		try:
			date = btc_dict['date']
			month = int(btc_dict['month'])
			week = int(btc_dict['week'])
			weekday = btc_dict['weekday']
			close = int(float(btc_dict['close']))
		except ValueError:
			print(btc_dict, 'missing data')
		else:
			dates.append(date)
			months.append(month)
			weeks.append(week)
			weekdays.append(weekday)
			closes.append(close)

			# print("{} is month {} week {}, {}, the close price"
			# 	  " is {} RMB.".format(date, month, week,
			#						   weekday, close))
# 创建Line实例，x轴标签旋转20度，不显示x轴所有标签
scattergram = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
scattergram.title = '收盘价对数变换（¥）'
scattergram.x_title = '日期'
scattergram.x_labels = dates
# 横坐标显示间距为20天
scattergram.x_labels_major = dates[::20]
# 利用半对数转换(semi-logarithmic)降低非线性影响
closes_log10 = [math.log10(_) for _ in closes]
scattergram.add(title='log收盘价', values=closes_log10)

scattergram.render_to_file('收盘价对数变换折线图.svg')


from itertools import groupby

def draw_line(x_data, y_data, title='', x_title='', y_title='', y_legend=''):
	"""绘制线图的函数"""
	# 参数包括x值，y值，图表名称，x轴名称，y轴名称，图例名称

	xy_map = []

	# 将xy值打包为元组
	xy_zipped = zip(x_data, y_data)
	# 对xy元祖进行排序，按照第一个元素
	xy_sorted = sorted(xy_zipped,key=lambda _:_[0])
	# 将进行sort的元素，按照第一个元素进行分组
	xy_group = groupby(xy_sorted,key=lambda _:_[0])
	#
	for x, y in xy_group:
		# 将每组数据放入list中
		y_list = [y2 for y1, y2 in y]
		# 将分组依据和计算后的平均值存储在list中
		xy_map.append([x, sum(y_list) / len(y_list)])

	# 上述步骤可以简化为:
	# for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):
	# 	y_list = [y2 for y1, y2 in y]
	# 	xy_map.append([x, sum(y_list) / len(y_list)])

	# 将分组依据和计算值的列表分别存储，类型是元组
	# x_unique_list, y_mean_list = [], []
	# for ls in xy_map:
	# 	x_unique_list.append(ls[0])
	# 	y_mean_list.append(ls[1])
	# x_unique = tuple(x_unique_list)
	# y_mean = tuple(y_mean_list)

	# 上述步骤可简化为：
	x_unique, y_mean = [*zip(*xy_map)]

	# 创建Line实例
	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.x_title = x_title
	line_chart.y_title = y_title
	line_chart.x_labels = x_unique
	line_chart.add(y_legend, y_mean)
	line_chart.render_to_file(title+'.svg')

	return line_chart


# 绘制前11个月的收盘平均值
# 获取日期索引
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(x_data=months[:idx_month],
							 y_data=closes[:idx_month],
							 title='收盘价月平均值',
							 y_legend='月平均值')

# 绘制前49周的收盘平均值
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(x_data=weeks[1:idx_week],
							 y_data=closes[1:idx_week],
							 title='收盘价周平均值',
							 y_legend='周平均值')

# 绘制前49周，weekday的平均值
weekday_str = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
			   'Friday', 'Saturday', 'Sunday']
# 获取前49周所有weekday的列表
weekday_int = [weekday_str.index(_) + 1 for _ in weekdays[1:idx_week]]
line_chart_weekday = draw_line(x_data=weekday_int,
							 y_data=closes[1:idx_week],
							 title='收盘价weekday平均值',
							 y_legend='weekday平均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四',
							   '周五', '周六', '周日', ]
line_chart_weekday.render_to_file('收盘价weekday平均值'+'.svg')



# 创建数据仪表盘
with open('收盘价仪表盘.html', 'w', encoding='utf8') as html_file:
	html_file.write('<html><head><title>收盘价Dashboard'
					'</title><meta charset="utf-8"></head><body>\n')
	for svg in [
		'收盘价折线图.svg', '收盘价对数变换折线图.svg',
		'收盘价月平均值.svg', '收盘价周平均值.svg',
		'收盘价weekday平均值.svg'
	]:
		html_file.write('<object type="image/svg+xml" data="{0}"> '
						'height=500></object>\n'.format(svg))
	html_file.write('</body></html>')
