import os
import glob
import json
from pprint import pprint
import pandas as pd

# Function that returns a list containing names of the immediate subdirectories in the
# directory path passed as argument
def get_immediate_subdir(dir_path):

    imm_subdir = []
    for file_name in os.listdir(dir_path):

        file_path = os.path.join(dir_path, file_name)
        if(os.path.isdir(file_path)):

            imm_subdir.append(file_name)

    return imm_subdir

def pickle_source_tweets():

    source_tweets = dict()

    for event_name in EVENT_LIST:

        event_dir_path = os.path.join(DATA_SET_DIR, event_name)
        subdirs = get_immediate_subdir(event_dir_path)

        for classification in subdirs:

            class_dir_path = os.path.join(event_dir_path, classification)
            tweet_folder_list = os.listdir(class_dir_path)
            for tweet_folder in tweet_folder_list:

                file_name = tweet_folder + ".json"
                source_tweet = os.path.join(class_dir_path, tweet_folder, 'source-tweet', file_name)
                data = json.load(open(source_tweet))
                data['event_name'] = event_name
                data['classification'] = classification
                source_tweets[tweet_folder] = data

    source_tweets_df = pd.DataFrame.from_dict(source_tweets, orient = 'index')
    source_tweets_df.to_pickle(r'C:\Users\Abhishek\Desktop\source_tweets.pickle')

def pickle_reaction_tweets():

    reaction_tweets = dict()

    for event_name in EVENT_LIST:

        event_dir_path = os.path.join(DATA_SET_DIR, event_name)
        subdirs = get_immediate_subdir(event_dir_path)

        for classification in subdirs:

            class_dir_path = os.path.join(event_dir_path, classification)
            tweet_folder_list = os.listdir(class_dir_path)
            for tweet_folder in tweet_folder_list:

                reaction_tweet_paths = glob.glob(os.path.join(class_dir_path, tweet_folder, r'reactions\*.json'), recursive=True)
                
                for reaction_tweet in reaction_tweet_paths:

                    data = json.load(open(reaction_tweet))
                    data['event_name'] = event_name
                    #data['classification'] = classification
                    tweet_id = data['id_str']
                    reaction_tweets[tweet_id] = data
                #pprint(reaction_tweets)

    reaction_tweets_df = pd.DataFrame.from_dict(reaction_tweets, orient = 'index')
    reaction_tweets_df.to_pickle(r'C:\Users\Abhishek\Desktop\reaction_tweets.pickle')

DATA_SET_DIR = r'C:\Users\Abhishek\Desktop\pheme-rnr-dataset'
EVENT_LIST = get_immediate_subdir(DATA_SET_DIR)

#pickle_source_tweets()
pickle_reaction_tweets()