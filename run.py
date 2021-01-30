import tweepy
import authorization
import sys
from time import sleep

import json




live = False




class Tweeter_Data_Streaming(tweepy.StreamListener):
	
	def __init__(self):
		self.hashtag_counts = 0
		self.attended_users = []
		self.T = 0 # Tweets
		self.RT = 0 #Retweets
		self.friend = []  #Enter your friends id : ['Twitter',"jack"]
		self.raw_friend = []
		for i in self.raw_friend:
			self.friend.append(i.lower())
	
	
	def on_data(self, data): # When data collected
		Data = json.loads(data)
		
		if "RT @" in Data["text"]:
			self.RT += 1 # Increase RT by 1
		else:
			self.T += 1 # Increse Tby 1
		
		try:
			user = Data["entities"]["user_mentions"][0]["screen_name"] #Get id if retweeted
		
		except:
			user = Data["user"]["screen_name"] #Get id if tweet
		
		if user not in self.attended_users:
			self.attended_users.append(user) # set attended user

		self.hashtag_counts += 1 # Increase allcounts by 1
		with open("attended_user.txt", "a+") as file: # Write users
			if user.lower() not in file.read().lower():
				DATA = str(user) + "\n"
				file.write(DATA)

		if user.lower() in self.friend:
			print("User name:{0}\tAll:{1}\tUsers count:{2}\tTweets:{3}".format(user,self.hashtag_counts,len(self.attended_users),self.T))
		else:
			print("User name:{0}\tAll:{1}\tUsers count:{2}\tTweets:{3}".format(user,self.hashtag_counts,len(self.attended_users),self.T))
		
		
		return True
		
		
		
	
	def on_error(self, error): # When raise error
		print(error)
		sleep(5)
		return False
	
	def on_timeout(self, time_out): # When connection timed out
		print(time_out)
		sleep(10)
		return False
	
	def on_exception(self, get_exeption): #When other exeption hase raised
		print(get_exeption)
		sleep(5)
		return False




def help():
	HELP = """
	Use like this
	python run.py {True/False (Optional)} Hashtag1 Hashtag2 ...
	
	python run.py Trump		//Find all tweets wich contain #Trump and print them all
	python run.py True Trump 	Find all tweets and just print last user id
	
	
	"""
	print(HELP)





if __name__ == "__main__":
	FILTER = []
	if sys.argv: # Get filters data from CMD, Terminal & etc.
		if sys.argv[0] == "--help":
			help()
			sys.exit()
		if sys.argv[0] == True: #Live Update of Code
			live = True
		if sys.argv[1]:
			for i in sys.argv[1:]:
				FILTER.append(i)
		else:
			FILTER = [input("Enter filteration>> ")]
	else:
		FILTER = [input("Enter filteration>> ")]


	listener = Tweeter_Data_Streaming() # Set up Steam listener
	
	auth = authorization.get_auth() # Get authorization
	print("User\tNumber\tCount of attend\t Number of users\tTweets")
	
	stream = tweepy.Stream(auth, listener) # Set up Streamer
	stream.filter(track=FILTER) # Set up Stream filter


