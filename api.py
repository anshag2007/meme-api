from flask import *
from praw import *
from os import *
from random import *

__author__ = "AnshAg2007 <anshag2007@gmail.com>"
__version__ = "1.1.0"

""" Meme API by AnshAgarwal using Flask + PRAW (Python Reddit API Wrapper)

  Website : https://meme-api.anshag2007.repl.co
  Creator : AnshAgarwal
  Version : 1.1.0
  """

app = Flask(__name__)
reddit = Reddit(
    client_id=getenv("CLIENT_ID"),
    client_secret=getenv("CLIENT_SECRET"),
    user_agent="python",
    username=getenv("USERNAME"),
    password=getenv("PASSWORD"))

@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/get',methods=['GET'])
def get():
	try:
		subreddit = reddit.subreddit(
			choice([
				'dankmemes',
				'me_irl',
				'memes']))
				
		submissions = subreddit.hot(limit=500)
		
		all_subs = []
		
		for submission in submissions:
			all_subs.append(submission)
			
		final_sub = choice(all_subs)
		
		if final_sub.selftext == "":
			selftext = "this post has no text"
		else:
			selftext = final_sub.selftext
			
		res = {
			'postTitle': str(final_sub.title),
			'postURL': str(reddit.config.reddit_url+final_sub.permalink),
			'imageURL': str(final_sub.url),
			'postText': str(selftext),
			'isNSFW': bool(final_sub.over_18),
			'isVideo': bool(final_sub.is_video)
			
		}
		return jsonify(res)
		
	except Exception as e:
		return jsonify(e)
		
@app.route('/get/<string:sub>',methods=['GET'])
def getsub(sub):
	try:
		subreddit = reddit.subreddit(sub)
		submissions = subreddit.hot(limit=500)
		all_subs = []
		
		for submission in submissions:
			all_subs.append(submission)
			
		final_sub = choice(all_subs)
		
		if final_sub.selftext == "":
			selftext = "this post has no text"
		else:
			selftext = final_sub.selftext
			
		res = {
			'postTitle': str(final_sub.title),
			'postURL': str(reddit.config.reddit_url+final_sub.permalink),
			'imageURL': str(final_sub.url),
			'postText': str(selftext),
			'isNSFW': bool(final_sub.over_18),
			'isVideo': bool(final_sub.is_video)
			
		}
		return jsonify(res)
	
	except Exception as e:
		return jsonify(e)
		

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080,debug=True)
