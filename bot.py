import praw, time, os
from depository.py import matched
#Just a starter. This is by no means good programming. It was just a hasty type up to get something down

r = praw.Reddit(user_agent='')
print("Starting")
time.sleep(.85)
print("Processing comments")
r.login()

words = []

def slow(string):
	#This is just for effect
	string = str(string) + '\n'
	for letter in string:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(.055)

def action():
	subreddit = r.get_subreddit('test')
	comment = subreddit.get_comments(limit=75)
	for comment in comments:
    	comment_text = comment.body.lower()
    	match = any(string in comment_text for string in words)
    	if comment.id no in matched and match:
    		slow("I, A HUMAN, HAVE FOUND {} ONE").format(comment.id)
      		comment.reply("")
      		with open('depository.py', 'a') as myFile:
      			myFile.write(matched.append(str(comment.id)))
      			myFile.close()
      
while True:
  action()
  time.sleep(10)
  
#So this is the preliminary stuff that I can pull off the top of my head
