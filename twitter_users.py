import unicodedata
import tweepy
import time
import unicodecsv as csv

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file_input = open("realdonaldtrump_follower_ids.csv")

reader = csv.reader(file_input)

user_ids = [user_id[0] for user_id in list(reader)]

# seperated into groups of 100 plus remainder
user_partitions = [user_ids[x:x + 100] for x in xrange(0, len(user_ids), 100)]

def getUserData(d):
	keys = ['name', 'screen_name', 'created_at', 'id', 'friends_count',
			'followers_count', 'statuses_count', 'profile_image_url',
			'verified', 'location', 'time_zone', 'utc_offset', 'lang',
			'description']
	return [d._json[key] for key in keys]

file_output = open("twitter_follower_data.csv", "wb")
csv_w = csv.writer(file_output)

rows_written = 0

for user in user_partitions:
	
	# makes a single request
	list_user_obj = api.lookup_users(user_ids=user)

	user_data = [getUserData(u) for u in list_user_obj]

	for twitter_user in user_data:
		csv_w.writerow(twitter_user)

		rows_written = rows_written + 1
		print rows_written

	time.sleep(5)

file_output.close()


