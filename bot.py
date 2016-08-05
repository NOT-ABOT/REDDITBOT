import praw, time
import sqlite3
import re
import oauth
url = 'http://www.google.com/?#q='
username = 'TheHelpfulBot'
depression_words = [
                    'I want to die',
                    'I want to kill myself',
                    'I hate life',
                    'I\'m having suicidal thoughts'
                    'I don\'t have a reason to live'
                    'I hate myself'
                    'I am a failure'
                    'I don\'t deserve to live'
                    'I can\'t do this anymore'
                    
] 
depression_responses = [
                      'I\'m so sorry to hear that you\'re in pain. If you are in serious pain and need help' + ', ' + '[please visit this site](https://afsp.org/)',
                      'I understand your pain. [This site might be able to help](https://afsp.org/)'
]
curious_words = [
                'I wonder why'
                'How does',
                'What if',
                'When did'
]

curious_responses = [
                    '[Here, let me help you with that](' + url + ')'
]

relationship_words= [
                    'How do I get a *friend*'
]

relationship_responses = [
                      'The most common way is to ask the person out'
  
  
]

all_comment_types = [
                    depression_words, 
                    curious_words,
                    relationship_words,
]
all_comment_responses = [
                      depression_responses,
                      curious_responses,
  
]
###########################################################################################
#Stil working in things, but I'm gonna try to test this thing out tonight, if possible    #
###########################################################################################

print("Opening Database...")
found = sqlite3.connect('answered.db') #create a database w/SQLite3 python library
x = found.cursor()
x.execute('CREATE TABLE IF NOT EXISTS answered(COMMENT TEXT, SUBMISSION TEXT)')
found.commit()

print("Logging in to Reddit...")
r = praw.Reddit("A helpful friend with useful advice")
r.set_oauth_app_info(oauth.app_id, oauth.app_secret, oauth.redirecturl)
sub = 'test'
maxposts = 100
url = 'http://www.google.com/?#q='

class CommentReply:
	
	def __init__(self, comment_type, response_type):
		self.comment_type = comment_type
		self.response_type = response_type
		
	def reply_to_comment(comment_type, reponse_type):
		comments = r.get_subreddit(sub).get_comments(limit=maxposts)
		for comment in comments:
			x.execute('Select * FROM answered WHERE COMMENT=?', [comment.id])
			if not x.fetchone():
				try:
					author = comment.author.name
					if author.lower() != username.lower():
						comment_text = comment.body.lower()
						string = comment.body.lower().split()
						match = any(string.lower() in comment_text for word in comment_type)
						if match:
							print("Replying to " + author)
							comment.reply(response_type)
						else:
							pass
				except AttributeError:
					pass
				x.execute('INSERT INTO answered VALUES(?),'[comment.id])
				found.commit()


      
class SubmissionReply:
		
		def __init__(self, submission_type, submission_reply):
			self.submission_type = submission_type
			self.submission_reply = submission_reply
			
		def reply_to_submission(submission_type, _response_type):
			submissions = r.get_subreddit(sub).get_new(limit=maxposts)
			for submission in submissions:
				x.execute('SELECT * FROM answered WHERE SUBMISSION TEXT=?', [submission.id])
				if not x.fetchone:
					try:
						author = submission.author.name
						if author.lower() != username.lower():
							submission_text = submission.text.lower()
							match = any(string in submission_text for word in submission_type)
							if match:
								print('Replying to ' + author)
								submission.reply(response_type)
					except AtrributeError:
						pass
					x.execute('INSERT INTO answered VALUES(?)', [submission.id])
					found.commit()
					

while True:
	CommentReply.reply_to_comment(depression_words, depression_responses)
	time.sleep(5)
