import json
import pprint
import os
import glob
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import re
import sys


def add(replies, id):
	if id in replies:
		for r in replies[id]:
			d = {}
			d[r] = add(replies, r)
			return d  
	else:
		return list()

urls = ["/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/germanwings-crash/rumours/*","/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/germanwings-crash/non-rumours/*",'/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/charliehebdo/rumours/*','/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/charliehebdo/non-rumours/*','/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/ferguson/rumours/*','/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/ferguson/non-rumours/*','/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/ottawashooting/rumours/*','/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/ottawashooting/non-rumours/*','/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/sydneysiege/rumours/*','/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/sydneysiege/non-rumours/*']

#url = "/Users/a0s01gh/Desktop/project/pheme-rnr-dataset/charliehebdo/rumours/*"
for url in urls:
	for tweets in glob.glob(url):
		structure = {}
		source = tweets + "/source-tweet/*.json"
		sourceData = json.load(open(glob.glob(source)[0]))
		sourceId = sourceData['id_str']
		structure[sourceId] = {}

		reactions = tweets + "/reactions/*.json"
		replies = {}
		for reaction in glob.glob(reactions):
			reactionData = json.load(open(reaction))
			replyTo = reactionData["in_reply_to_status_id_str"]
			reactionId = reactionData["id_str"]
			if replyTo not in replies:
				replies[replyTo] = []
			replies[replyTo].append(reactionId)
		if sourceId in replies:
			for k in replies[sourceId]:
				structure[sourceId][k] = add(replies, k)
		result = tweets + "/structure.json"
		with open(result, 'w') as fp:
			json.dump(structure, fp)
	#pprint.pprint(structure)



