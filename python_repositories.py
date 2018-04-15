import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)

# 将API响应存储在变量中
response_dict = r.json()
# print("Keys:",response_dict.keys())
print("Total repositories:", response_dict['total_count'])

# 探索仓库信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
# print("\nrepo_dict keys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
# 	print(key)

# 获取前十名仓库的一些信息
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts[:10]:
# 	print('Name:', repo_dict['name'])
# 	print('Owner:', repo_dict['owner']['login'])
# 	print('Stars:', repo_dict['stargazers_count'])
# 	print('Repository:', repo_dict['html_url'])
# 	print('Created:', repo_dict['created_at'])
# 	print('Updated:', repo_dict['updated_at'])
# 	print('Description:', repo_dict['description'])
# 	print('\n\n')

names, plot_dicts = list(), list()
for repo_dict in repo_dicts:
	# 将用于x周刻度
	names.append(repo_dict['name'])
	# 将用于绘制柱状图
	plot_dict = dict(
		value=repo_dict['stargazers_count'],
		label=str(repo_dict['description']),
		# 增加链接网站
		xlink=repo_dict['html_url']
	)
	plot_dicts.append(plot_dict)
# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
# 主标签字号
my_config.major_label_font_size = 18
# 标签名15字符以内
my_config.truncate_label = 15
# 隐藏水平线
my_config.show_y_guides = False
# 自定义图表宽度
my_config.width = 1000

chart = pygal.Bar(config=my_config, style=my_style)
chart.title = 'Most-Starred Python Project on Github'
chart.x_labels = names

chart.add('', plot_dicts)
# 存储文件过程中发生AttributeError: 'NoneType' object has no attribute 'decode'，
# 是由于在读取关于描述的过程中，有空值的原因，
# 解决方法是使用str()，将空值转换为None
chart.render_to_file('python_repositories.svg')
