import praw, time
import sqlite3
import re
import admin,records
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
                      'Sometimes the most important thing is simply being there for someone'


]

all_comment_types = [
                    depression_words,
					depression_responses,
                    curious_words,
					curious_responses,
                    relationship_words,
					relationship_responses
]

###########################################################################################
#Still working in things, but I'm gonna try to test this thing out tonight, if possible    #
###########################################################################################

#r = praw.Reddit("A helpful friend with useful advice")
#r.set_oauth_app_info(admin.app_id, admin.app_secret, admin.redirecturl)
#r.get_authorize_url('...', oauth.app_scopes, True)

def login():
	r = praw.Reddit("A friend providing useful information and helpful advice")
	r.set_oauth_app_info(admin.app_id, admin.app_secret, admin.redirecturl)
	r.refresh_access_token(admin.refresh_token)
	return r

sub = 'test'
maxposts = 100
url = 'http://www.google.com/?#q='
print('Logging in to Reddit...')

class CommentReply:

	def __init__(self, comment_type, response_type):
		self.comment_type = comment_type
		self.response_type = response_type

	def reply_to_comment(comment_type, reponse_type):
		comments = r.get_subreddit(sub).get_comments(limit=maxposts)
		for comment in comments:
			if comment.id not in answered_comments:
				try:
					author = comment.author.name
					if author.lower() != username.lower():
						comment_text = comment.body.lower()
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
	for i in range(len(all_comment_types)-1):
        CommentReply.reply_to_comment(all_comment_types[i], all_coment_types[i+1])
        time.sleep(5)
