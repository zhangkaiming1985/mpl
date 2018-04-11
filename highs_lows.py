import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)  # 读取第一行
	# 获取第一行每个元素的索引和值
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	# 获取最高温、日期的所有数据
	dates, highs, lows = [], [], []

	for row in reader:
		current_date = datetime.strptime(row[0], '%Y-%m-%d')
		dates.append(current_date)
		highs.append(int(row[1]))
		lows.append(int(row[3]))

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# 填充两条曲线间区域
plt.fill_between(dates, highs, lows, facecolor='black', alpha=0.1)
plt.title("Daily temperatures, 2014", fontsize=16)
plt.xlabel(s='Date', fontsize=12)
fig.autofmt_xdate()
plt.ylabel(s='Temperatures(F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
