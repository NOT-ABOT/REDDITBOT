import praw, time
from Search&Respond.py import *
import sqlite3

#Building up the framework, still a work in progress

print("Database opening")
found = sqlite3.connect('answered.db') #create a database w/SQLite3 python library
x = found.cursor()
x.execute('CREATE TABLE IF NOT EXISTS answered(COMMENT ID TEXT, SUBMISSION ID TEXT)')
found.commit()

print("Starting up and loggin in to Reddit...")
r = praw.Reddit("ThisIsNotTheBotYouAreLookingFor") #Because this bot needs more star wars refrences.
o = OAuth2Util.OAuth2Util(r)
o.refresh(force=True)
sub = 'test'
limit = 100
cid = comment.id
sid = submission.id

class CommentReply:
	
	def __init__(self, comment_type, response_type):
		self.comment_type = comment_type
		self.response_type = response_type
		
	def reply_to_comment(comment_type, reponse_type):
		comments = r.get_subreddit(sub).get_comments(limit)
		for comment in comments:
			x.execute('Select * FROM answered WHERE ID=?', [cid])
			if not x.fetchone():
				try:
					author = comment.author.name
					if author.lower() != username.lower():
						comment_text = comment.body.lower()
						r.send_message('___NOT_A_BOT___', 'Response', 'Comment answered')
						match = any(string in comment_text for word in comment_type)
						if match:
							print("Replying to " + author)
							comment.reply(response_type)
					except AttributeError:
						pass
					x.execute('INSERT INTO answered VALUES(?),'[cid])
					found.commit()


      
class SubmissionReply:
		
		def __init__(self, submission_type, submission_reply):
			self.submission_type = submission_type
			self.submission_reply = submission_reply
			
		def reply_to_submission(submission_type, _response_type)
			submissions = r.get_subreddit(sub).get_new(limit)
			for submission in submissions:
				x.execute('SELECT * FROM answered WHERE ID=?', [sid])
				if not x.fetchone:
					try:
						author = submission.author.name
						if author.lower() != username.lower():
							submission_text = submission.text.lower()
							r.send_message('___NOT_A_BOT___', 'Response', 'Submission answered')
							match = any(string in submission_text for word in submission_type)
							if match:
								print('Replying to ' + author)
								submission.reply(response_type)
					except AttributeError:
						pass
					x.execute('INSERT INTO answered VALUES(?)', [sid]
					found.commit()
					

while True:
	for i in range(len(all_comment_types)):
	  	CommentReply.reply_to_comment(all_comment_types[i], all_comment_types[i+1])
  		time.sleep(10)
  
