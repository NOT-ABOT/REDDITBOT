import praw, time
import re, random, sqlite3
import admin
url = 'http://www.google.com/?#q='
disclaimer = '''
\n\n -----------------------------------------------------------------------------------------------------------------------\n\n
*I am a bot, and this was done automatically. If you have any questions or concerns regarding my operation, or simply would like to know how
you can contribute to my development, please [message the very human owner of this account](https://www.reddit.com/message/compose/?to=___NOT_A_BOT___)* '''

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
f7='''
Never go to bed mad. Stay up and fight. ― *Phyllis Diller*
'''
f8='''
The planet is fine. The people are fucked.
― *George Carlin*
'''
f9='''
If a book about failures doesn't sell, is it a success?
― *Jerry Seinfeld*'''
f10 = '''
Don't be so humble - you are not that great.
― *Golda Meir*'''
f11='''
If you're too open-minded; your brains will fall out.
― *Lawrence Ferlinghetti*'''
f12 = '''I don't hate you.. I just don't like that you exist
― *Gena Showalter*'''
f13='''
When I die, I want to go peacefully like my grandfather did–in his sleep. Not yelling and screaming like the passengers in his car.
- *Bob Monkhouse*'''
f14='''
I AM NOT A BOT, AS MY USERNAME SUGGESTS - */u/___NOT_A_BOT___*
'''


################################################################################################################
#Search list                                                                                                   #
################################################################################################################

self_words = [
            '(.*)thehelpfulbot',
            'quote(.*)',

]

self_responses = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]

curious_words = [
                'how',
                'why',
                'what',
                'who(.*)'
]

curious_responses = [
                    '[Here, let me help you with that](' + url,
                    '[Maybe I can help?](' + url,
                    '[Let me know if this helps](' + url,
                    '[Perhaps this link would help](' + url,
                    '[This link might help](' + url
]


regular_words = ['(.*) how pretty am i(.*)',
                '(.*) (.*)how smart am i(.*)',
                '(.*) (.*)how cool am i(.*)',
                '(.*) (.*)how awesome am i(.*)',]

dating_words = ['i got a date(.*)',
                'i(.*)m in bo(.*)',
                ]

dating_responses = ['Cool! Great jo -- I\'m happy for you!',
                    'That\'s great dude!']

common_words = [
                'count'
                ]

numbers = []
for i in range(1001):
    numbers.append(str(i))

common_responses = [
                 'Yay! I love numbers!: \n ' + str(' \n'.join(numbers)),
                 ]

###########################################################################################################
###########################################################################################################

sub = input('Which sub? ')
username = 'TheHelpfulBot'
maxposts = int(input('How many posts? '))

print('Opening SQlite Database...')

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
                                r.send_message('___NOT_A_BOT___','Answer','Answered ' + author)
                                r.send_message(author, 'Have a nice day', 'I hope you have a nice day!')
                                comment.reply(random.choice(response_type) + disclaimer)
                                cur.execute('INSERT INTO oldposts VALUES(?)', [comment.id])
                                sql.commit()
                            else:
                                pass
                except AttributeError:
                    pass

    def set_reply_to_comment(comment_type, response_type):
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
                                print('Replying to /u/' + author)
                                r.send_message('___NOT_A_BOT___', 'Answer', 'Answered comment by /u/' + author)
                                comment.reply(response_type[i])
                                cur.execute('INSERT INTO oldposts VALUES(?)', [comment.id])
                                sql.commit()
                            else:
                                pass
                except AttributeError:
                    pass

    def single_reply_to_comment(look, say):
        comments = r.get_subreddit(sub).get_comments(limit=maxposts)
        for comment in comments:
            cur.execute('SELECT * FROM oldposts WHERE ID=?', [comment.id])
            if not cur.fetchone():
                try:
                    author = comment.author.name
                    if author.lower() != username.lower():
                        comment_text = comment.body.lower()
                        if re.match(look, comment_text):
                            print('Replying with ' + say + ' to /u/' + author)
                            comment.reply(say)
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
                            if re.match(curious_words[i], comment_text) and len(comment_text) <= 100 and not re.match(regular_words[i], comment_text):
                                print('Replying to comment by /u/' + author + ' with url')
                                comment.reply(random.choice(curious_responses) + str(comment_text) + ')' + disclaimer)
                                cur.execute('INSERT INTO oldposts VALUES(?)', [comment.id])
                                sql.commit()
                except AttributeError:
                    pass

    def looks(comment_type):
            comments = r.get_subreddit(sub).get_comments(limit=maxposts)
            for comment in comments:
                cur.execute('SELECT * FROM oldposts WHERE ID=?', [comment.id])
                if not cur.fetchone():
                    try:
                        author = comment.author.name
                        comment_text = comment.body.lower()
                        if author.lower() != username.lower():
                            for i in range(len(comment_type)):
                                if re.match(comment_type[i], comment_text):
                                    badrating = [1,2,3,4]
                                    b = random.choice(badrating)
                                    rating = random.randint(4,10)
                                    resp = [
                                            'I would rate you a ' + str(rating) + ' on a scale of 1 to 10',
                                            'I would say that you are a ' + str(rating),
                                            'Hmm, you\'re a ' + str(rating),
                                            'I was gonna say ' + str(b) + ', but on second thought I would say ' + str(random.randint(5,10))
                                            ]
                                    comment.reply(random.choice(resp) + disclaimer)
                                    r.send_message(author, 'Have a nice day', 'I hope you have a nice day!' + disclaimer)
                                    print('Rating /u/' + author)
                                    r.send_message('___NOT_A_BOT___', 'Rating', 'Rated /u/' + author)
                                    cur.execute('INSERT INTO oldposts VALUES(?)', [comment.id])
                                    sql.commit()
                                else:
                                    pass
                    except AttributeError:
                        pass

    def single_user(look, say):
        user = input('Which user shall I obey? ')
        comments = r.get_subreddit(sub).get_comments(limit=maxposts)
        for comment in comments:
            cur.execute('SELECT * FROM oldposts WHERE ID=?', [comment.id])
            if not cur.fetchone():
                try:
                    author = comment.author.name
                    if author.lower() == user.lower():
                        comment_text = comment.body.lower()
                        if re.match(look, comment_text):
                            print('Replying with ' + say + ' to /u/' + author)
                            comment.reply(say)
                            cur.execute('INSERT INTO oldposts VALUES(?)', [comment.id])
                            sql.commit()
                        else:
                            pass
                except AttributeError:
                    pass

class SubmissionReply:

    def __init__(self, submission_type, submission_reply):
        print('Parsing Submissions')
        self.submission_type = submission_type
        self.submission_reply = submission_reply

    def reply_to_submission(submission_type, response_type):
        submissions = r.get_subreddit(sub).get_hot(limit=maxposts)
        for submission in submissions:
            cur.execute('SELECT * FROM oldposts WHERE ID=?', [submission.id])
            if not cur.fetchone():
                try:
                    author = submission.author.name
                    if author.lower() != username.lower():
                        submission_title = submission.title.lower()
                        submission_text = submission.body.lower()
                        for i in range(len(submission_type)):
                            if re.match(submission_type[i], submission_title):
                                print('Replying to submission by /u/' + author)
                                submission.add_comment(random.choice(response_type))
                                cur.execute('INSERT INTO oldposts VALUES(?)', [submission.id])
                                sql.commit()
                            else:
                                pass
                except AttributeError:
                    pass

    def reply_to_submission_url():
        submissions = r.get_subreddit(sub).get_hot(limit=maxposts)
        for submission in submissions:
            cur.execute('SELECT * FROM oldposts WHERE ID=?', [submission.id])
            if not cur.fetchone():
                try:
                    author = submission.author.name
                    if author.lower() != username.lower():
                        submission_title = submission.title.lower()
                        for i in range(len(curious_words)):
                            if re.match(curious_words[i], submission_title) and not re.match(regular_words[i], submission_title):
                                print('Replying to submission by /u/' + author + ' with url')
                                submission.add_comment(random.choice(curious_responses) + submission_title + ') ' + disclaimer)
                                cur.execute('INSERT INTO oldposts VALUES(?)', [submission.id])
                                sql.commit()
                except AttributeError:
                    pass

def login():
    print('Logging in...')
    r = praw.Reddit('A helpful friend with useful advice')
    r.set_oauth_app_info(admin.app_id, admin.app_secret, admin.redirecturl)
    r.refresh_access_information(admin.refresh_token)
    return r
r = login()
r

def test():
    comments = r.get_subreddit(sub).get_comments(limit=maxposts)
    for comment in comments:
        comment_text = comment.body.lower()
        print(comment_text + '\n\n---------------------------------------------------------------\n\n')


num = 1

while True:
    print('...')
    SubmissionReply.reply_to_submission_url()
    SubmissionReply.reply_to_submission(self_words, self_responses)
    SubmissionReply.reply_to_submission(common_words, common_responses)
    SubmissionReply.reply_to_submission(dating_words, dating_responses)
    CommentReply.reply_to_comment(dating_words, dating_responses)
    CommentReply.single_reply_to_comment('thanks', 'You\'re welcome' + disclaimer)
    CommentReply.single_reply_to_comment('thank you', 'You\'re welcome' + disclaimer)
    CommentReply.single_reply_to_comment('kar(.*)', 'It looks like you mentioned karma! You can get all the free karma you want on r/FreeKarma4You' + disclaimer)
    CommentReply.reply_to_comment_url()
    CommentReply.looks(regular_words)
    CommentReply.reply_to_comment(self_words, self_responses)
    time.sleep(2)
    num += 1
    if num == 1200:
        r
