from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import sklearn

def split_dataset(dataset, train_percentage, feature_headers, target_header):
    """
    Split the dataset with train_percentage
    :param dataset:
    :param train_percentage:
    :param feature_headers:
    :param target_header:
    :return: train_x, test_x, train_y, test_y
    """
 
    # Split dataset into train and test dataset
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header],
                                                        train_size=train_percentage)
    return train_x, test_x, train_y, test_y


def main():
	tweets = pd.read_pickle('.\\source_tweets.pickle')

	headers = ["contributors", "truncated", "text", "in_reply_to_status_id", "id",
	               "favourite_count", "source", "retweeted", "coordinates", "entities",
	               "lang", "created_at","in_reply_to_status_id_place", "event_name", "classification", "possibly_sensitive", "extended_entities", "filter_level","metadata" ]

	HEADERS = ["user_followers_count", "user_friends_count", "retweet_count", "classification"]
	data = pd.DataFrame(tweets[["user_followers_count", "user_friends_count", "retweet_count", "classification"]], columns=['user_followers_count','user_friends_count', 'retweet_count', 'classification'])

	train_x, test_x, train_y, test_y = split_dataset(data, 0.9, HEADERS[:3], HEADERS[-1])
	NB_Classifier = GaussianNB()
	NB_Classifier.fit(train_x, train_y)
	predictions = NB_Classifier.predict(test_x)
	
	accuracy = accuracy_score(y_true = test_y, y_pred = predictions)
	print(accuracy)

if __name__ == "__main__":
	main()