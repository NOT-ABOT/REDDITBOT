import praw, time
import sqlite3

#Just a starter. This is by no means good programming. It was just a hasty type up to get something down for us to work with

"""
We need to determine the following: 

user_agent = purpose of bot
username = /u/examplebot
password = examplepassword

"""
print("Database opening")
found = sqlite3.connect('answered.db')
x = found.cursor()
x.execute('CREATE TABLE IF NOT EXISTS answered(ID TEXT)')
found.commit()

r = praw.Reddit(user_agent='') #This needs to be filled in
r.login()
print("Starting up and loggin in to Reddit")

words = [] #What are we gonna look for?
response = "" #What are we gonna say?

def action():
	subreddit = r.get_subreddit('test')
	comments = subreddit.get_comments(limit=100)
	for comment in comments:
	    x.execute('SELECT * FROM answered WHERE ID=?', [comment.id])
	    if not x.fetchone():
	    	try:
    		    author = comment.author.name
    		    if author.lower() != username.lower():
    		        comment_text = comment.body.lower()
    	    	    match = any(string in comment_text for string in words)
    		        if match:
    			        print("Replying to " + author)
      			        comment.reply(response)
      			        with open('depository.py', 'a') as myFile:
      				        myFile.write(matched.append(str(comment.id)) + ', ')
      				        myFile.close()
      	    except AttributeError:
      		    pass
      		x.execute('INSERT INTO answered VALUES(?)', [commend.id])
      

while True:
  	action()
  	time.sleep(1)
  
