import praw, time
import sqlite3

#Just a starter. This is by no means good programming. It was just a hasty type up to get something down for us to work with

"""
We need to determine the following: 

user_agent = purpose of bot
username = /u/examplebot
password = examplepassword

"""

match = sqlite3.connect('matched.db')
cur = sql.cursor()

r = praw.Reddit(user_agent='') #This needs to be filled in
r.login()
print("Starting up and loggin in to Reddit")

words = [] #What are we gonna look for?
response = "" #What are we gonna say?

def action():
	subreddit = r.get_subreddit('test')
	comments = subreddit.get_comments(limit=100)
	for comment in comments:
		try:
    		author = comment.author.name
    		if author.lower() != username.lower():
    		    comment_text = comment.body.lower()
    	    	match = any(string in comment_text for string in words)
    		    if str(comment.id) not in matched and match:
    			    print("Replying to " + author)
      			    comment.reply(response)
      			    with open('depository.py', 'a') as myFile:
      				    myFile.write(matched.append(str(comment.id)) + ', ')
      				    myFile.close()
      	except AttributeError:
      		pass
      

while True:
  	action()
  	time.sleep(1)
  
