import tweepy

consumer_key = 'GMaYLuEFNO1InO51SX7FVlgKG'
consumer_secret = 'N3ghtpxVtDRm7bjLNO3oJmkSPn3kj44hGZ4YCj4d9lKxpxRm6Q'

access_token = '904696702925389825-dQerFVZIEQQRQxVk3XHeg75OeLkxs3I'
access_token_secret = '7BmKtIDj6egQvcehN0AYG1ejGZtf42MaW3hGak55Th31Y'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.followers_ids('384779793')
for tweet in public_tweets:
    print(tweet)