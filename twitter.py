#twitter.py

import urllib
import json
import sys

def search_twitter (query='python'):
	url = 'http://search.twitter.com/search.json?show_user&q=' + query
	response = urllib.urlopen(url).read()
	data = json.loads(response)
	return data['results']
	
def print_tweets(tweets):
	for tweet in tweets:
	
def search_user (query):
	url = 'http://api.twitter.com/1/statuses/user_timeline.format.json?screen_name&q=' + query
	response = urllib.urlopen(url).read()
	data = json.loads(response)
	return data['results']

if __name__ == "__main__":
	query = sys.argv[1]
	results = search_twitter(query)
	print_tweets(results)
	