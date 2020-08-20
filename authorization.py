import TOKENS as TOK
from tweepy import API, OAuthHandler


def get_auth(): # Get athorazation to connect to tweeter

	# Set Keys & Secret keys
	consumer_key = TOK.consumer_key
	consumer_secret = TOK.consumer_secret
	access_key = TOK.Access_Token
	access_secret = TOK.Access_Token_Secret
	
	# Get athorazation
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	
	return auth




def start():
	# Get auth
	auth = get_auth()
	
	# Connect to Tweeter server and verifiy device
	client = API(auth)
	
	return client
