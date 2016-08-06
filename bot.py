import praw, time
import re, random, sqlite3
import admin
import json, urllib

url = 'http://www.google.com/?#q='
username = 'TheHelpfulBot'
disclaimer = ''
##########################################################################################
#Long responses section                                                                  #
##########################################################################################
drep1 = '''
I'm really sorry to hear that you feel this way. I'm gonna be straight up with you -- I'm a bot. But here's the thing:
it doesn't take a human to see that you're special. Don't give up. Don't ever give up. And if you need someone to talk to,
[feel free to message me at my human account](https://sf.reddit.com/user/___NOT_A_BOT___/). Hang in there, pal.
'''
drep2 = '''Hey there. Just wanted to say that I feel you. I know what it's like to be in pain. I remember when my parents died -- it was the worst
feeling I had ever known. But here's the thing: no matter how hard it gets, giving up is not the answer. Stay strong and hang in there. Things will get better. '''

deep1 = '''
The question of God's existence has been around for a long time. Now, I'm just a bot, so I can't really as provide much insight as humans can, but
here's my two cents: Has anyone ever been argued into believing in God? I don't think I've ever seen someone come to faith due to an intellectual argument.
This is because religion, more than anything else, is emotional, psychological and spiritual, not intellectual. And on the flip side, attempting to argue one
out of his/her religion is pointless for the simple reason that, if religion makes someone happy, trying to remove this source of happiness is cruel and counterproductive.
I am, however, just a bot. And for that reason I must direct you to a [neutral source](https://en.wikipedia.org/wiki/Existence_of_God) of information regarding the topic
at hand. I hope this helps! Have a nice day ;p '''

################################################################################################################
#Search list                                                                                                   #
################################################################################################################

knowledgesearch = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
'query': 'term',
'limit': '10',
'indent': 'True',
'key': 'apiKey',
}

god_words = [
            'god(.*) exist(.*)'
]

god_responses = [
                deep1
]
depression_words = [
                    'i(.*)(.*) (.*) depressed',
                    'i(.*)(.*) a failure',
                    'i(.*)(.*) to die',
                    'kill(.*) myself',
                    'i hate (.*) life',
                    'i(.*)(.*) hav(.*) suicidal thoughts',
                    'i don(.*)t have a(.*) reason to live',
                    'i hate myself',
                    'i don(.*)t deserve to live',
                    'i can(.*)t take this (.*) anymore(.*)'

]
depression_responses = [

                      'Life is filled with highs and lows. You may be at a low point right now, but stay strong! Things can always improve -- /u/XUDB',
                      drep1,
                      drep2
]
curious_words = [
                'how do ',
                'why does',
                'when is',
                'how can i'
]

curious_responses = [
                    '[Here, let me help you with that](' + url
]

relationship_words= [
                    'how do I get a (.*)friend(.*)',
]

relationship_responses = [
                      'The most common way to get a date is to ask the person out'
                      'Sometimes the most important thing is simply being there for someone. This may help you get a date',
]

silly_words = [
]

silly_responses = [
]
all_comment_types = [
                    depression_words,
					depression_responses,
                    curious_words,
					curious_responses,
                    relationship_words,
					relationship_responses,
                    silly_words,
                    silly_responses
]

###########################################################################################################
###########################################################################################################

sub = 'all'
maxposts = 1000
url = 'http://www.google.com/?#q='
print('Logging in to Reddit...')

sql = sqlite3.connect('sql.db')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS oldposts(id TEXT)')
sql.commit()

class CommentReply:

    def __init__(self, comment_type, response_type):
        self.comment_type = comment_type
        self.response_type = response_type

    def reply_to_comment(comment_type, response_type):
        comments = r.get_subreddit(sub).get_comments(limit=maxposts)
        for comment in comments:
            cur.execute('SELECT * FROM oldposts WHERE ID=?', [comment.id])
            if not cur.fetchone():
                try:
                    author = comment.author.name
                    if author.lower() != username.lower():
                        comment_text = comment.body.lower()
                        for i in range(len(comment_type)):
                            if re.match(comment_type[i], comment_text):
                                print("Replying to /u/" + author)
                                comment.reply(str(random.choice(response_type)) + disclaimer)
                                cur.execute('INSERT INTO oldposts VALUES(?)', [comment.id])
                                sql.commit()
                            else:
                                pass
                except AttributeError:
                    pass

    def reply_to_comment_url():
        comments = r.get_subreddit(sub).get_comments(limit=maxposts)
        for comment in comments:
            cur.execute('SELECT * FROM oldposts WHERE ID=?', [comment.id])
            if not cur.fetchone():
                try:
                    author = comment.author.name
                    if author.lower() != username.lower():
                        comment_text = comment.body.lower()
                        match = any(word.lower() in comment_text for word in curious_words)
                        if match:
                            print('Replying to /u/' + author)
                            comment.reply(str(curious_responses[0] + comment_text + ') ' + disclaimer))
                            cur.execute('INSERT INTO oldposts VALUES(?)', [comment.id])
                            sql.commit()
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

def login():
    r = praw.Reddit('A helpful friend with useful advice')
    r.set_oauth_app_info(admin.app_id, admin.app_secret, admin.redirecturl)
    r.refresh_access_information(admin.refresh_token)
    return r

r = login()
r
while True:
    print('Searching...')
    CommentReply.reply_to_comment(depression_words, depression_responses)
    CommentReply.reply_to_comment(relationship_words, relationship_responses)
    CommentReply.reply_to_comment(god_words, god_responses)
    '''CommentReply.reply_to_comment(silly_words, silly_responses)
    CommentReply.reply_to_comment_url()'''
    time.sleep(2)
