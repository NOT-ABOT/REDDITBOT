import praw, time
import re, random, sqlite3
import admin
import json, urllib

url = 'http://www.google.com/?#q='
username = 'TheHelpfulBot'
disclaimer = '\n\n*I am a bot in beta mode. Please be patient with me as I figure things out.*'
##########################################################################################
#Long responses section                                                                  #
##########################################################################################

f1 = '''
I always wanted to be somebody, but now I realize I should have been more specific. - *Lily Tomlin* '''
f2 = '''
If at first you don’t succeed, then skydiving definitely isn’t for you. - *Steven Wright*'''
f3= '''
Luck is what you have left over after you give 100 percent. – *Langston Coleman*'''
f4='''
I didn’t fail the test. I just found 100 ways to do it wrong. – *Benjamin Franklin*'''
f5='''
The elevator to success is out of order. You’ll have to use the stairs… one step at a time. – *Joe Girard*'''
f6='''
It takes less time to do things right than to explain why you did it wrong. – *Henry Wadsworth Longfellow*'''
d1 ='''Life: the condition that distinguishes animals and plants from inorganic matter, including the capacity for growth, reproduction, functional activity, and continual change preceding death.'''

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

self_words = [
            '/u/TheHelpfulBot'
]

self_responses = [f1,f2,f3,f4,f5,f6]


curious_words = [
                'how do(.*) ',
                'why do(.*)',
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

deep_words = ['what(.*) (.*) the meaning of life(.*)'
]

deep_responses = [d1]

dictionary_words =['What does (.*) mean?']
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
                                r.send_message('___NOT_A_BOT___', 'Answered', 'Comment Answered')
                                comment.reply(str(random.choice(response_type)))
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
                        for i in range(len(curious_words)):
                            if re.match(curious_words[i], comment_text):
                                print('Replying to comment by /u/' + author + ' with url')
                                comment.reply(str(curious_responses[0] + comment_text + ') ' + disclaimer))
                                cur.execute('INSERT INTO oldposts VALUES(?)', [comment.id])
                                sql.commit()
                except AttributeError:
                    pass



class SubmissionReply:

    def __init__(self, submission_type, submission_reply):
        print('Parsing Submissions')
        self.submission_type = submission_type
        self.submission_reply = submission_reply

    def reply_to_submission(submission_type, _response_type):
        submissions = r.get_subreddit(sub).get_new(limit=maxposts)
        for submission in submissions:
            if not cur.fetchone():
                try:
                    author = submission.author.name
                    if author.lower() != username.lower():
                        submission_text = submission.text.lower()
                        for i in range(len(submission_type)):
                            if re.match(submission_type[i], submission_text):
                                print('Replying to submission by /u/' + author)
                                submission.reply(random.choice(response_type))
                                cur.execute('INSERT INTO oldposts VALUES(?)', [submission.id])
                                sql.commit()
                except AttributeError:
                    pass


def login():
    r = praw.Reddit('A helpful friend with useful advice')
    r.set_oauth_app_info(admin.app_id, admin.app_secret, admin.redirecturl)
    r.refresh_access_information(admin.refresh_token)
    return r

r = login()
r
num = 1
while True:
    print('Parsing comments...')
    #CommentReply.reply_to_comment(depression_words, depression_responses)
    CommentReply.reply_to_comment(relationship_words, relationship_responses)
    #CommentReply.reply_to_comment(god_words, god_responses)
    #SubmissionReply.reply_to_submission(depression_words, depression_responses)
    CommentReply.reply_to_comment(self_words, self_responses)
    CommentReply.reply_to_comment(deep_words, deep_responses)
    #CommentReply.reply_to_comment_url()
    time.sleep(2)
    num += 1
    if num == 1200:
        login()
