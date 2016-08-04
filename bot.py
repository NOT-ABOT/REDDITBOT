import praw, time
from Search&Respond.py import words, response
import sqlite3

#Building up the framework, still a work in progress

print("Database opening")
found = sqlite3.connect('answered.db') #create a database w/SQLite3 python library
x = found.cursor()
x.execute('CREATE TABLE IF NOT EXISTS answered(COMMENT ID TEXT, SUBMISSION ID TEXT)')
found.commit()

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
    		        r.send_message("___NOT_A_BOT___", "Response", "Comment answered")  
    	    	    match = any(string in comment_text for string in words)
    		        if match:
    				print("Replying to " + author)
      			    comment.reply(response)
      	    	except AttributeError:
      		    	pass
      		    
      		x.execute('INSERT INTO answered VALUES(?)', [commend.id])
      		found.commit()
      
def submission_reply():
	submissions = r.get_subreddit(sub).get_new(limit=50)
	for submission in submissions:
		x.execute('SELECT * FROM answered WHERE ID=?,' [submission.id]
		if not x.fetchone():
			try:
				author = submission.author.name
				if author.lower() != username.lower():
					submission_text = submission.text.lower()
					r.send_message("___NOT_A_BOT___", "Response", "Submission answered")
					match = any(string in submission_text for string in words)
					if match:
						print("Replying to " + author)
						comment.reply(response)
			except AttributeError:
				pass
			x.execute('INSERT INTO answered VALUES(?)', [submission.id])
			found.commit()
				
while True:
  	comment_reply()
  	submission_reply()
  	time.sleep(10)
  
