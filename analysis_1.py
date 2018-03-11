import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

objects = pd.read_pickle('source_tweets.pickle')
events = list(set(objects["event_name"]))

statuses_count_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
statuses_count_non_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
retweet_count_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
retweet_count_non_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
friends_count_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
friends_count_non_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
in_reply_to_user_id_count_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
in_reply_to_user_id_count_non_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
followers_count_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
followers_count_non_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
favourite_count_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
favourite_count_non_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
verified_count_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}
verified_count_non_rumour = {"charliehebdo":0, "ferguson":0, "germanwings-crash":0, "ottawashooting":0, "sydneysiege":0}


'''
for i in range(len(events)):
	for j in range(5802):
		if objects["classification"][j] == "rumours" and objects["event_name"][j] == events[i]:
			statuses_count_rumour[events[i]]+=objects["user"][j]["statuses_count"]
		elif objects["event_name"][j] == events[i]:
			statuses_count_non_rumour[events[i]]+=objects["user"][j]["statuses_count"]

print(statuses_count_rumour, statuses_count_non_rumour)


for i in range(len(events)):
	labels = ('Rumour', 'Non-rumour')
	y_pos = np.arange(len(labels))
	stats_statuses_count = [statuses_count_rumour[events[i]], statuses_count_non_rumour[events[i]]]
	plt.bar(y_pos, stats_statuses_count, align='center', alpha=0.5)
	plt.xticks(y_pos, labels)
	plt.ylabel('No. of statsuses')
	plt.title('Status count of rumour vs non rumour - '+events[i])
	plt.show()


for i in range(len(events)):
	for j in range(5802):
		if objects["classification"][j] == "rumours" and objects["event_name"][j] == events[i]:
			retweet_count_rumour[events[i]]+=objects["retweet_count"][j]
		elif objects["event_name"][j] == events[i]:
			retweet_count_non_rumour[events[i]]+=objects["retweet_count"][j]

print(retweet_count_rumour, retweet_count_non_rumour)


for i in range(len(events)):
	labels = ('Rumour', 'Non-rumour')
	y_pos = np.arange(len(labels))
	stats_retweet_count = [retweet_count_rumour[events[i]], retweet_count_non_rumour[events[i]]]
	plt.bar(y_pos, stats_retweet_count, align='center', alpha=0.5)
	plt.xticks(y_pos, labels)
	plt.ylabel('No. of retweets')
	plt.title('Retweet count of rumour vs non rumour - '+events[i])
	plt.show()

for i in range(len(events)):
	for j in range(5802):
		if objects["classification"][j] == "rumours" and objects["event_name"][j] == events[i]:
			friends_count_rumour[events[i]]+=objects["user"][j]["friends_count"]
		elif objects["event_name"][j] == events[i]:
			friends_count_non_rumour[events[i]]+=objects["user"][j]["friends_count"]

print(friends_count_rumour, friends_count_non_rumour)


for i in range(len(events)):
	labels = ('Rumour', 'Non-rumour')
	y_pos = np.arange(len(labels))
	stats_friends_count = [friends_count_rumour[events[i]], friends_count_non_rumour[events[i]]]
	plt.bar(y_pos, stats_friends_count, align='center', alpha=0.5)
	plt.xticks(y_pos, labels)
	plt.ylabel('No. of friends')
	plt.title('Friends count of rumour vs non rumour - '+events[i])
	plt.show()

for i in range(len(events)):
	for j in range(5802):
		if objects["classification"][j] == "rumours" and objects["event_name"][j] == events[i]:
			if objects["in_reply_to_user_id"][j] != "null":
				in_reply_to_user_id_count_rumour[events[i]]+=1
		elif objects["event_name"][j] == events[i]:
			if objects["in_reply_to_user_id"][j] != "null":
				in_reply_to_user_id_count_non_rumour[events[i]]+=1

print(in_reply_to_user_id_count_rumour, in_reply_to_user_id_count_non_rumour)

for i in range(len(events)):
	labels = ('Rumour', 'Non-rumour')
	y_pos = np.arange(len(labels))
	stats_in_reply_to_user_id = [in_reply_to_user_id_count_rumour[events[i]], in_reply_to_user_id_count_non_rumour[events[i]]]
	plt.bar(y_pos, stats_in_reply_to_user_id, align='center', alpha=0.5)
	plt.xticks(y_pos, labels)
	plt.ylabel('No. of rumours that were replies')
	plt.title('Replies - rumour vs non rumour - '+events[i])
	plt.show()
'''

'''
for i in range(len(events)):
	for j in range(5802):
		if objects["classification"][j] == "rumours" and objects["event_name"][j] == events[i]:
			followers_count_rumour[events[i]]+=objects["user"][j]["followers_count"]
		elif objects["event_name"][j] == events[i]:
			followers_count_non_rumour[events[i]]+=objects["user"][j]["followers_count"]

for i in range(len(events)):
	labels = ('Rumour', 'Non-rumour')
	y_pos = np.arange(len(labels))
	stats_followers_count = [followers_count_rumour[events[i]], followers_count_non_rumour[events[i]]]
	plt.bar(y_pos, stats_followers_count, align='center', alpha=0.5)
	plt.xticks(y_pos, labels)
	plt.ylabel('No. of followers')
	plt.title('Followers count of rumour vs non rumour - '+events[i])
	plt.show()

print(followers_count_rumour, followers_count_non_rumour)
'''
'''
for i in range(len(events)):
	for j in range(5802):
		if objects["classification"][j] == "rumours" and objects["event_name"][j] == events[i]:
			favourite_count_rumour[events[i]]+=objects["favorite_count"][j]
		elif objects["event_name"][j] == events[i]:
			favourite_count_non_rumour[events[i]]+=objects["favorite_count"][j]

for i in range(len(events)):
	labels = ('Rumour', 'Non-rumour')
	y_pos = np.arange(len(labels))
	stats_favourite_count = [favourite_count_rumour[events[i]], favourite_count_non_rumour[events[i]]]
	plt.bar(y_pos, stats_favourite_count, align='center', alpha=0.5)
	plt.xticks(y_pos, labels)
	plt.ylabel('No. of favourite counts')
	plt.title('Favourite count of rumour vs non rumour - '+events[i])
	plt.show()

print(favourite_count_rumour, favourite_count_non_rumour)

for i in range(len(events)):
	for j in range(5802):
		if objects["classification"][j] == "rumours" and objects["event_name"][j] == events[i]:
			favourite_count_rumour[events[i]]+=objects["favorite_count"][j]
		elif objects["event_name"][j] == events[i]:
			favourite_count_non_rumour[events[i]]+=objects["favorite_count"][j]

for i in range(len(events)):
	labels = ('Rumour', 'Non-rumour')
	y_pos = np.arange(len(labels))
	stats_favourite_count = [favourite_count_rumour[events[i]], favourite_count_non_rumour[events[i]]]
	plt.bar(y_pos, stats_favourite_count, align='center', alpha=0.5)
	plt.xticks(y_pos, labels)
	plt.ylabel('No. of favourite counts')
	plt.title('Favourite count of rumour vs non rumour - '+events[i])
	plt.show()

print(favourite_count_rumour, favourite_count_non_rumour)
'''
for i in range(len(events)):
	for j in range(5802):
		if objects["classification"][j] == "rumours" and objects["event_name"][j] == events[i]:
			if objects["user"][j]["verified"]:
				verified_count_rumour[events[i]]+=1
		elif objects["event_name"][j] == events[i]:
			if objects["user"][j]["verified"]:
				verified_count_non_rumour[events[i]]+=1

for i in range(len(events)):
	labels = ('Rumour', 'Non-rumour')
	y_pos = np.arange(len(labels))
	stats_verified_count = [verified_count_rumour[events[i]], verified_count_non_rumour[events[i]]]
	plt.bar(y_pos, stats_verified_count, align='center', alpha=0.5)
	plt.xticks(y_pos, labels)
	plt.ylabel('No. of Verified Users')
	plt.title('Verified user count of rumour vs non rumour - '+events[i])
	plt.show()

print(verified_count_rumour, verified_count_non_rumour)
