from flask import *
from praw import *
from os import *
from random import *

""" Meme API by AnshAgarwal using Flask + PRAW """

app = Flask(__name__)
reddit = Reddit(
    client_id=getenv("CLIENT_ID"),
    client_secret=getenv("CLIENT_SECRET"),
    user_agent="python",
    username=getenv("USERNAME"),
    password=getenv("PASSWORD"))


@app.route('/')
def home():
	
	subreddit = reddit.subreddit('dankmemes')
	submissions = subreddit.hot(limit=500)
	
	all_subs = []
	
	for submission in submissions:
		all_subs.append(submission)
	
	final_sub = choice(all_subs)
	
	res = {
		'postTitle': str(final_sub.title),
		'postUrl': str(final_sub.url),
		'postText': str(final_sub.selftext),
		'isNSFW': bool(final_sub.over_18),
		'isVideo': bool(final_sub.is_video)
	}
	
	return jsonify(res)
		

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080,debug=True)