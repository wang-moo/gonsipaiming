import os
import datetime

import matplotlib.pyplot as plt

base_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.dirname(os.path.dirname(base_path))
picture_file = base_path + '/{}.png'.format(datetime.date.today())
file = base_path + '/NingboYusingLighting.txt'
# file = path + '/NingboYusingLighting.txt'
x = []
y = []
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(50, 10))
with open(file, 'r') as r:
    for i in r.readlines():
        times, ranking = i.split(' ')
        x.append(times)
        y.append(ranking)


plt.plot(x, y, color='red', linewidth=2)

#
# plt.xlabel(u'时间戳')
# plt.ylabel(u'名次')
# plt.title(u'Ningbo Yusing Lighting 排名波动')

plt.savefig(picture_file)
# plt.show()
