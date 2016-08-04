import praw, time
from Search&Respond.py import words, response
import sqlite3

#Just a starter. This is by no means good programming. It was just a hasty type up to get something down for us to work with
"""
useragent =
app_id = Leave empty for now
app_secret = leave empty for now
"""
print("Database opening")
found = sqlite3.connect('answered.db')
x = found.cursor()
x.execute('CREATE TABLE IF NOT EXISTS answered(ID TEXT)')
found.commit()

"""
Callback on redirect url: https://127.0.0.1:65010/authorize_callback
r= praw.Reddit(useragent = '')
"""
print("Starting up and loggin in to Reddit")

sub = 'test'


def comment_reply():
	subreddit = r.get_subreddit(sub)
	comments = subreddit.get_comments(limit=100)
	for comment in comments:
	    x.execute('SELECT * FROM answered WHERE ID=?', [comment.id])
	    if not x.fetchone():
	    	try:
    		    author = comment.author.name
    		    if author.lower() != username.lower():
    		        comment_text = comment.body.lower()
    	    	    	match = any(string in comment_text for string in words)
    		        	if match:
    					print("Replying to " + author)
      			        	comment.reply(response)
      	    	except AttributeError:
      		    pass
      		    
      		x.execute('INSERT INTO answered VALUES(?)', [commend.id])
      		found.commit()
      
def submission_reply():
	
while True:
  	comment_reply()
  	time.sleep(10)
  
