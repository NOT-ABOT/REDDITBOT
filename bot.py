import praw, time, os
from depository.py import matched

#Just a starter. This is by no means good programming. It was just a hasty type up to get something down for us to work with

r = praw.Reddit(user_agent='') #This needs to be filled in
print("Starting")
time.sleep(.85)
print("Processing comments")
r.login()

words = [] #What are we gonna look for?

def action():
	subreddit = r.get_subreddit('test')
	comment = subreddit.get_comments(limit=75)
	for comment in comments:
    	comment_text = comment.body.lower()
    	match = any(string in comment_text for string in words)
    	if comment.id not in matched and match:
    		print("Here's one " + str(comment.id))
      		comment.reply("") #This needs to be filled in with what we want our bot to do
      		with open('depository.py', 'a') as myFile:
      			myFile.write(matched.append(str(comment.id)))
      			myFile.close()
      
while True:
  action()
  time.sleep(10)
  
