import requests
from pprint import pprint
from requests_oauthlib import OAuth1
import calendar
import datetime

#url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
url = 'https://api.twitter.com/1.1/tweets/search/30day/dev2.json'
#url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23RIPSridevi%20since%3A2018-02-25%20until%3A2018-02-26&src=typd'
auth = OAuth1('z9SndE5xVOmC7va09oAFZVYyg', 'De0ajBMXUjeSAzt9KirtnPI6j6MKaFFHKby53PjWUu1yGJ4gIM', '750948636255739904-GW1E3dqz4HAL6ldn97xebpj1Xf7ubmu', 'udgs8g9tgkwwHLb1WIMqkf2ZGwk88dm35yiLaEmLjzTcN')

search_params = {
    "query" : "#RIPSridevi",
    #'fromDate' : calendar.timegm(datetime.datetime(2018,2,25).utctimetuple()),
    #'toDate' : calendar.timegm(datetime.datetime(2018,3,3).utctimetuple())
    "fromDate" : "201802250000",
    "toDate" : "201803030000",
    "next" : "eyJhdXRoZW50aWNpdHkiOiJlMGU2NjBhMjI4YTBiYmQ0NWI2ZGM2ZjkwY2YwNTg5N2RjNjk2YTJiMmEyMGM0YTViYTYxMzNmNmQwNjIyZjA3IiwiZnJvbURhdGUiOiIyMDE4MDIyNTAwMDAiLCJ0b0RhdGUiOiIyMDE4MDMwMzAwMDAiLCJuZXh0IjoiMjAxODAzMDIxMzAxMzMtOTY5NTU4MzI1NjY1NzM4NzUzLTAifQ=="
}

r = requests.get(url, auth=auth, params = search_params)
pprint(r.text)