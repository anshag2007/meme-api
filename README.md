### About

#### A Completely Free-to-use and open-source Meme API !!

#### The Source Code of this API is available at [Github.com](https://github.com/AnshAg2007/meme-api)

#### This API is made in Python using Flask & PRAW (Python Reddit API Wrapper)


- ##### [jump to bottom](#jump-to-top)
 + **In this page:**
     - **[About](#about)**
     - **[Usage](#usage)**
     - **[Links](#links)**
      

### Usage

#### This API provides data in json format, to get a random meme from a random subreddit, go to  `/get` route (`https://meme-api.anshag2007.repl.co/get`)

#### To get memes from a subreddit of your choice go to `/get/<subreddit_name>` route(`https://meme-api.anshag2007.repl.co/get/<subreddit_name>`), the subreddit_name will be the subreddit from where you want memes
#### Example usage: `https://meme-api.anshag2007.repl.co/get/dankmemes` 

### Making an HTTP Request in Python using this API
```py
import requests
link = requests.get('https://meme-api.anshag2007.repl.co/get/memes')
print(link.json())
# This will return a dict.
```
##### Example output 
```py
{
  "imageURL": "https://i.redd.it/llpr1xxphxi61.jpg", 
  "isNSFW": False, 
  "isVideo": False, 
  "postText": "this post has no text", 
  "postTitle": "Sad but true", 
  "postURL": "https://www.reddit.com/r/memes/comments/lpbcuh/sad_but_true/"
}
```

### Links

- ####  [Website](https://meme-api.anshag2007.repl.co)
- #### [Website/get](https://meme-api.anshag2007.repl.co)
- #### [Github Repository](https://github.com/AnshAg2007/meme-api)

### Thanks for visiting here & using my API <3

- #####  [jump to top](#about)

