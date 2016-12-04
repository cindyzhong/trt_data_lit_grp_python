# trt_data_lit_grp_python
The Repository for Learn Python Hard Way: Mining Social Media Series

Installing Python
---------

If you don't have python on your computer already, please install Anaconda Python 2.7
Follow the instruction here and select the most appropriate option based on your OS
https://www.continuum.io/downloads

Twitter API Access
---------
In order to get access to the Twitter API through OAuth (open standard for authorization), 
we have to obtain our consumer information and access tokens first by registering 
our app on https://apps.twitter.com.

1. Go to https://apps.twitter.com/ and log into your twitter account

2. Click on "Create New App"

3. Obtain the Consumer key, Consumer secret, Access token, and Access token secret. Save them somewhere.
DO NOT SHARE THIS INFORMATION WITH ANYBODY ELSE!

Test Twitter Access
---------
We will use Twython to access Twitter data, you can install it by 

```
pip install twython
```

Note: if you have installed Anaconda for Windows, go to Anaconda Command Prompt, cd into C:\Program Files\Anaconda2\Scripts


Create a Twython instance with your Consumer Key and Consumer Secret

```
from twython import Twython

APP_KEY = "yTsbWUVcHIZLhAGiEIW3cLcBD"
APP_SECRET = "1ueRj649WHLVamjndLTmtyyLhSMmOH5N178WYgJ2TPPRuX9q7r"
OAUTH_TOKEN="188627356-H59h9W5BzVDlx6ZRIG7rDkqlllu9h296vCSQom4f"
OAUTH_TOKEN_SECRET="5uW5AxWx3IMQP26bZzG8Epkeyuh0piKOqsQ9tZsY25UYD"

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
```

Let's try to post a status on your twitter account through Python

```
twitter.update_status(status='I am going to TDLG to Learn Python the Hard Way!')
```

Check your Twitter Profile. Hooray! You have completed the Prerequisites! See you at the session!

Credits
---------
* [Mining Social Media Web 2nd Edition](https://github.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition)
