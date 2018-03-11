from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
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

def random_forest_classifier(features, target):
    """
    To train the random forest classifier with features and target data
    :param features:
    :param target:
    :return: trained random forest classifier
    """
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf

def main():
	vectorizer = CountVectorizer(analyzer = 'word')

	rf = RandomForestClassifier(n_estimators = 100)
	tweets = pd.read_pickle('../Datasets/source_tweets.pickle')

	headers = ["contributors", "truncated", "text", "in_reply_to_status_id", "id",
	               "favourite_count", "source", "retweeted", "coordinates", "entities",
	               "lang", "created_at","in_reply_to_status_id_place", "event_name", "classification", "possibly_sensitive", "extended_entities", "filter_level","metadata" ]

	#print(tweets.describe())
	HEADERS = ["user_followers_count", "user_friends_count", "retweet_count", "classification"]
	data = pd.DataFrame(tweets[["user_followers_count", "user_friends_count", "retweet_count", "classification"]], columns=['user_followers_count','user_friends_count', 'retweet_count', 'classification'])
	#print(data)
	train_x, test_x, train_y, test_y = split_dataset(data, 0.5, HEADERS[:3], HEADERS[-1])
	print("Train_x Shape :: ", train_x.shape)
	print("Train_y Shape :: ", train_y.shape)
	print("Test_x Shape :: ", test_x.shape)
	print("Test_y Shape :: ", test_y.shape)

	trained_model = random_forest_classifier(train_x, train_y)
	print("Trained model :: ", trained_model)
	predictions = trained_model.predict(test_x)
	print(predictions)

	for i in range(0, 50):
	        print("Actual outcome :: {} and Predicted outcome :: {}".format(list(test_y)[i], predictions[i]))
	 
	print("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
	print("Test Accuracy  :: ", accuracy_score(test_y, predictions))
	print(" Confusion matrix ", confusion_matrix(test_y, predictions))

if __name__ == "__main__":
	main()