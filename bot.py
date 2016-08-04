import praw, time, os
from depository.py import matched

#Just a starter. This is by no means good programming. It was just a hasty type up to get something down for us to work with

"""
We need to determine the following: 

user_agent = purpose of bot
username = /u/examplebot
password = examplepassword

"""


r = praw.Reddit(user_agent='') #This needs to be filled in
r.login()
print("Starting up and loggin in to Reddit")

words = [] #What are we gonna look for?
response = "" #What are we gonna say?

def action():
	subreddit = r.get_subreddit('test')
	comment = subreddit.get_comments(limit=75)
	for comment in comments:
    	comment_text = comment.body.lower()
    	author = comment.author.name
    	match = any(string in comment_text for string in words)
    	if str(comment.id) not in matched and match:
    		if author.lower() != username.lower():
    			print("Found one by " + str(author))
      			comment.reply(response)
      			with open('depository.py', 'a') as myFile:
      				myFile.write(matched.append(str(comment.id)) + ', ')
      				myFile.close()
      

while True:
  	action()
  	time.sleep(10)
  
