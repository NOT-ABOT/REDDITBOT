import praw, time, os
#Just a starter. This is by no means good programming. It was just a hasty type up to get something down

r = praw.Reddit(user_agent='')
print("Running")
r.login()

words = []
matched = []

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
    		slow("I, A HUMAN, HAVE FOUND ONE")
      		comment.reply("")
      		matched.append(comment.id)
      
while True:
  action()
  time.sleep(10)
  
#So this is the preliminary stuff that I can pull off the top of my head
