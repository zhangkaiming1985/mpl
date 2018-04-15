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
	# 以x值升序排列
	xy_sorted = sorted(xy_zipped, key=lambda _:_[0])
	print(zip(xy_zipped))
	print("----------")
	print(xy_sorted)

	# for x, y in groupby(sorted(xy_zipped))
	# 创建Line实例
	# scattergram = pygal.Line()
	# scattergram.title = title
	# scattergram.x_title = x_title
	# scattergram.y_title = y_title
	# scattergram.x_labels = dates
	# # 利用半对数转换(semi-logarithmic)降低非线性影响
	# closes_log10 = [math.log10(_) for _ in closes]
	# scattergram.add(title=y_legend, values=closes_log10)

draw_line(dates, closes)