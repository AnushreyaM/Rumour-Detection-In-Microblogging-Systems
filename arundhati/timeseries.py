import json
import pprint
import os
import glob
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np



yearsFmt = mdates.DateFormatter('%Y')
fig, ax = plt.subplots()

count = {}
def add(time):
	time = time.split(' ')
	time = time[1] + " " + time[2] + " " + time[5] + " " + time[0] + " " + time[3]
	d = datetime.strptime(time, '%b %d %Y %a %H:%M:%S')
	time = datetime.strftime(d, '%Y %m %d %H')
	if time not in count:
		count[time] = 0
	count[time] += 1

def timeSeries(url,what,lab):
	global count
	count = {}	
	read = glob.glob(url)
	for f in read:
		'''
		reactions = glob.glob(f + "/reactions/*.json")
		for r in reactions:
			time = (json.load(open(r)))['created_at']
			add(time)
		'''
		source = glob.glob(f + "/source-tweet/*.json")
		for s in source:
			time = (json.load(open(s)))['created_at']
			add(time)

	x = []
	y = []

	for k in sorted(count.iterkeys()):
		x.append(datetime.strptime(k,"%Y %m %d %H"))
		y.append(count[k])

	x = np.array(x)
	y = np.array(y)
	
	#plt.plot(x, y, what, label=lab)
	ax.plot(x, y, label=lab)
	
	
timeSeries('/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/germanwings-crash/rumours/*', 'b','rumour')
timeSeries('/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/germanwings-crash/non-rumours/*','g','non-rumour')

myFmt = mdates.DateFormatter("%d-%h-%y:%H")
ax.xaxis.set_major_formatter(myFmt)

## Rotate date labels automatically
fig.autofmt_xdate()

plt.title("germanwings-crash")
plt.legend(loc='upper center', shadow=True)
plt.show()

