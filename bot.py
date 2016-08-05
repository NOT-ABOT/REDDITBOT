import praw, time
import re, random
import admin, records
url = 'http://www.google.com/?#q='
username = 'TheHelpfulBot'

'''
Ignore these
one_word =['I']
one_word_responses =['Hi']
'''
depression_words = [
                    '(.*)Iwanttodie(.*)',
                    '(.*)Iwanttokillmyself(.*)',
                    '(.*)Ihatelife(.*)',
                    '(.*)I\'mhavingsuicidalthoughts(.*)',
                    '(.*)Idon\'thaveareasontolive(.*)',
                    '(.*)Ihatemyself(.*)',
                    '(.*)Iamafailure(.*)',
                    '(.*)Idon\'tdeservetolive(.*)',
                    '(.*)Ican\'tdothisanymore(.*)'

]
depression_responses = [
                      'I\'m so sorry to hear that you\'re in pain. If you are in serious pain and need help' + ', ' + '[please visit this site](https://afsp.org/)',
                      'I understand your pain. [This site might be able to help](https://afsp.org/)'
]
curious_words = [
                'How',
                'Why'
                'When'
]

curious_responses = [
                    '[Here, let me help you with that](' + url
]

relationship_words= [
                    'HowdoIgeta(.*)friend(.*)'
]

relationship_responses = [
                      'The most common way is to ask the person out'
                      'Sometimes the most important thing is simply being there for someone',
                      'How do I ask him out',
                      'How do I ask her out'


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

sub = 'reddit_bot_test'
maxposts = 100
url = 'http://www.google.com/?#q='
print('Logging in to Reddit...')

class CommentReply:

    def __init__(self, comment_type, response_type):
        self.comment_type = comment_type
        self.response_type = response_type

    def reply_to_comment(comment_type, response_type):
        comments = r.get_subreddit(sub).get_comments(limit=maxposts)
        for comment in comments:
            if str(comment.id) not in records.answered_comments:
                try:
                    author = comment.author.name
                    if author.lower() != username.lower():
                        comment_text = ''.join(comment.body.lower())
                        match = any(word.lower() in comment_text for word in comment_type)
                        if match:
                            print("Replying to /u/" + author)
                            comment.reply(str(random.choice(response_type)))
                            with open('records.py', 'a') as rec:
                                answered_comments.append(str(comment.id) + ', ')
                                rec.close()
                except AttributeError:
                    pass

    def reply_to_comment_url():
        comments = r.get_subreddit(sub).get_comments(limit=maxposts)
        for comment in comments:
            if str(comment.id) not in records.answered_comments:
                try:
                    author = comment.author.name
                    if author.lower() != username.lower():
                        comment_text = comment.body.lower()
                        match = any(word.lower() in comment_text for word in curious_words)
                        if match:
                            print('Replying to /u/' + author)
                            comment.reply(str(curious_responses[0] + comment_text + ')'))
                            with open('records.py', 'a') as rec:
                                answered_comments.append(str(comment.id)+', ')
                                rec.close()
                except AttributeError:
                	pass
"""
This is still not functional due to whitespace issues

class SubmissionReply:

		def __init__(self, submission_type, submission_reply):
			self.submission_type = submission_type
			self.submission_reply = submission_reply

		def reply_to_submission(submission_type, _response_type):
			submissions = r.get_subreddit(sub).get_new(limit=maxposts)
			for submission in submissions:
				if submission.id not in answered_submissions:
					try:
						author = submission.author.name
						if author.lower() != username.lower():
							submission_text = submission.text.lower()
							match = any(string in submission_text for word in submission_type)
                            with open('records.py', 'a') as rec:
                                answered_submissions.append(submission.id)
                                rec.close()
							if match:
								print('Replying to ' + author)
								submission.reply(random.choice(response_type))
					except AtrributeError:
						pass
"""
r = admin.login()
print('Running')
print(r.user)
CommentReply.reply_to_comment(one_word, one_word_responses)

'''
This will be the main loop when things are running better, and I will add a for loop in here to streamline the search process
while True:
    CommentReply.reply_to_comment(depression_words, depression_responses)
    time.sleep(5)
'''
