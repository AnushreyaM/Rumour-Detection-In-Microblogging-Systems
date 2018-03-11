import os
import glob
import json
from pprint import pprint
import pandas as pd
import nltk
from nltk import pos_tag, word_tokenize

allPosTagsPossible = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD",
"NN", "NNS","NNP","NNPS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS",
"RP", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP","WP$", "WRB"]

#generate feature vector of pos tags for a given text
#@param text
#@return feature_vector
def generate_postag_feature_vector(text):
    feature_vector = [0]*len(allPosTagsPossible)
    postag_list = nltk.pos_tag(word_tokenize(text))
    postag_corresponding_index_list = [allPosTagsPossible.index(wpt[1]) for wpt in postag_list if wpt[1] in allPosTagsPossible]
    for index in postag_corresponding_index_list:
        feature_vector[index] = 1

    return feature_vector

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

                
                remove = dict()
                #populate remove dict with all values which are of json format
                for key in data:
                   if type(data[key]) is dict:
                    remove[key] = data[key]
                #change how they jsons are represented in data: example: users_followers_count
                for key in remove:
                    for subkey in data[key]:
                        data[key+"_"+subkey] = data[key][subkey]
                    del data[key]
                data['pos_tag_feature_vector'] = generate_postag_feature_vector(data["text"])
                source_tweets[tweet_folder] = data

    source_tweets_df = pd.DataFrame.from_dict(source_tweets, orient = 'index')
    source_tweets_df.to_pickle(r'C:\Users\anush\Downloads\Final Sem Project\Datasets\source_tweets_posIncluded.pickle')

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

    #reaction_tweets_df = pd.DataFrame.from_dict(reaction_tweets, orient = 'index')
    #reaction_tweets_df.to_pickle(r'C:\Users\anush\Downloads\Final Sem Project\Datasets\reaction_tweets.pickle')

DATA_SET_DIR = r'C:\Users\anush\Downloads\Final Sem Project\Datasets\pheme-rnr-dataset'
EVENT_LIST = get_immediate_subdir(DATA_SET_DIR)

pickle_source_tweets()
#pickle_reaction_tweets()