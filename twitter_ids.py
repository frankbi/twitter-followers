import tweepy
import time
import csv

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

twitter_handle = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file_output = open(twitter_handle + "_follower_ids.csv", "wb")
csv_w = csv.writer(file_output)

total_ids_collected = 0

for user_list in tweepy.Cursor(api.followers_ids, screen_name=twitter_handle).pages():

	# returns seperate lists for each page
	for id in user_list:
		csv_w.writerow([id])

	# update total followers counter
	total_ids_collected = len(user_list) + total_ids_collected
	print "total ids collected: %d" % total_ids_collected

	# pause 60 seconds for rate limit
	time.sleep(60)


file_output.close()
