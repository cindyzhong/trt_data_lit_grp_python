# -*- coding: utf-8 -*-
"""
@Creator: Cindy Zhong
@Date: December 05, 2016
@Name: mining_twitter_lesson_1.py
"""
from __future__ import division
from twython import Twython, TwythonError
import pandas as pd
from datetime import datetime
import numpy as np
#-----------------------------set twitter credentials--------------------------
twitter_creds_df = pd.read_csv("C:\\twitter_creds.csv")

#-----------------------------Set up Twitter search parameters-----------------
APP_KEY = twitter_creds_df.ix[0,0]
APP_SECRET = twitter_creds_df.ix[1,0]
OAUTH_TOKEN = twitter_creds_df.ix[2,0]
OAUTH_TOKEN_SECRET = twitter_creds_df.ix[3,0]

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#%% Understanding the Twitter API - REST vs. Streaming

# Let's look at the results twitter returns when we send a request through the API
user_timeline = twitter.get_user_timeline(screen_name="realDonaldTrump",count=1)

# Walk through the result returned
# example:
print user_timeline[0]['text']
print user_timeline[0]['user']['followers_count']

#%%
# Let's fetch all of Trump and Hilary's tweets
api = twitter # Twitter authentication
searchQuerys = ['realDonaldTrump','HillaryClinton']
#create a dataframe to store the tweets
tweet_fields = ['handle','tweet_body','tweet_created_at','likes','retweet','hashtags','user_mentions','place']
tweet_df = pd.DataFrame(data=np.zeros((0,len(tweet_fields))), columns=tweet_fields)

for searchQuery in searchQuerys:
    maxTweets = 400 #Maximum number of tweets to download per user
    max_id = -1L  #If results only below a specific ID are, set max_id to that ID
    sinceId = None #no lower limit, go as far back as API allows
    tweetCount = 0
    tweetsPerQry = 200 #Number of tweets to grab per query, maximum is 100
    print("Downloading max {0} tweets for handle {1}".format(maxTweets,searchQuery))
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.get_user_timeline(screen_name=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.get_user_timeline(screen_name=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.get_user_timeline(screen_name=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.get_user_timeline(screen_name=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            
            for tweet in new_tweets:
                #insert key information about tweets into our tweet_df
                handle = searchQuery
                tweet_body = tweet['text'].encode('utf-8')
                tweet_created_at = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                likes = tweet['favorited']
                retweet = tweet['retweet_count']
                hashtags = [h['text'] for h in tweet['entities']['hashtags']]
                user_mentions = [user['name'] for user in tweet['entities']['user_mentions']]
                if tweet['place'] != None:
                    left_pt = tweet['place']['bounding_box']['coordinates'][0][0]
                    right_pt = tweet['place']['bounding_box']['coordinates'][0][2]
                    long_pt = (left_pt[0] + right_pt[0])/2
                    lat_pt = (left_pt[1] + right_pt[1])/2
                    place = (long_pt, lat_pt)
                else:
                    place = None
                #append to our dataframe
                tweet_ap = pd.DataFrame([[handle,tweet_body,tweet_created_at,likes,retweet,hashtags,user_mentions,place]],columns=tweet_fields)
                tweet_df = tweet_df.append(tweet_ap, ignore_index = True)
                
            tweetCount += len(new_tweets)
            
            print("Downloaded {0} tweets".format(tweetCount))
                           
            max_id = new_tweets[-1]['id']
        
        except TwythonError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break
        print ("Downloaded {0} tweets, for handle {1}".format(tweetCount,searchQuery))
        #Take a break
#        time.sleep(10)
#%%
# Now let's do some exploratory analytics with the tweets!
from collections import Counter
from bokeh.charts import Bar, output_file, show
from bokeh.charts.attributes import cat
from bokeh.layouts import row

# A look at Hilary's Most used hashtags
hilary_all_hashtags = [hashtag for t in tweet_df[tweet_df.handle != 'realDonaldTrump']['hashtags'] for hashtag in t]
hilary_most_common_hashtags = Counter(hilary_all_hashtags).most_common(15)
# A look at Trump's
trump_all_hashtags = [hashtag for t in tweet_df[tweet_df.handle == 'realDonaldTrump']['hashtags'] for hashtag in t]
trump_most_common_hashtags = Counter(trump_all_hashtags).most_common(15)

trump_all_mentions = [hashtag for t in tweet_df[tweet_df.handle == 'realDonaldTrump']['user_mentions'] for hashtag in t]
trump_most_common_mentions = Counter(trump_all_mentions).most_common(15)

#put them on a plot
labels, freq = zip(*trump_most_common_hashtags)
data = {'data': freq, 'x': labels}
bar = Bar(data, values='data',\
          label=cat(columns='x', sort=False),\
          title="Top Hashtags Used By Trump", \
          legend = False,
          xlabel="Hashtags", ylabel="Number of Occurance")

labels_2, freq_2 = zip(*trump_most_common_mentions)
data_2 = {'data_2': freq_2, 'x_2': labels_2}
bar_2 = Bar(data_2, values='data_2',\
          label=cat(columns='x_2', sort=False),\
          title="Top User Mentions By Trump", \
          legend = False,
          xlabel="User Mentions", ylabel="Number of Occurance")

output_file("C:\\Users\\cancxz\\Desktop\\CindyLocal\\TDLG\\Lesson1\\trump_top_mentions.png.html")
show(row(bar,bar_2))

#%%
# Let's Geo Track Trump
#import os
import matplotlib.pyplot as plt
#pip install seaborn
#import seaborn as sns
#conda install basemap
from mpl_toolkits.basemap import Basemap
#from matplotlib.patches import Polygon

# Coordinates
coord_frame = pd.DataFrame(tweet_df[tweet_df.handle == 'realDonaldTrump']['place'])
coord_frame[['Long', 'Lat']] = coord_frame['place'].apply(pd.Series)    

lon_min, lon_max = -130,-55
lat_min, lat_max = 20,50
 
plt.figure(2, figsize=(12,6))
 
m = Basemap(projection='merc',
             llcrnrlat=lat_min,
             urcrnrlat=lat_max,
             llcrnrlon=lon_min,
             urcrnrlon=lon_max,
             lat_ts=35,
             resolution='i')
 
m.fillcontinents(color='#bfbfbf')
m.drawcountries(linewidth=0.2)
m.drawstates(linewidth=0.2)  
# Plot the data
mxy = m(coord_frame['Long'].tolist(), coord_frame['Lat'].tolist())
m.scatter(mxy[0], mxy[1], c='#ff3333', lw=0, alpha=0.5, zorder=10)

plt.title('Where is Trump Tweeting From?')
plt.savefig("C:\\Users\\cancxz\\Desktop\\CindyLocal\\TDLG\\Lesson1\\trump.png", dpi=300)
plt.show()


