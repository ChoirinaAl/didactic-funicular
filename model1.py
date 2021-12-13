#!/usr/bin/env python
# coding: utf-8

# In[22]:


import tweepy
import re
from textblob import TextBlob


# In[23]:


api_key = "IugtQ3zs90f4dIpobxEgeTCR6"
api_key_secret = "qftKgqQTpjqlce9mlNhpUeNfZbnb5i0jb7ZnhmVCQPcPfDHd8T"
access_token = "1470147780635074563-LDzKeXZRVIVzxbdVLg3V2Lk9YJ8xDh"
access_token_secret = "1oFqiFUAWABIBsYnABA5qkWI01J9XDEUBz4TtYFkqvs24"
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[24]:


HasilSearch = api.search_tweets(q="vaccine", lang="en", count=100)


# In[25]:


HasilSearch


# In[26]:


hasilAnalisis = []

for tweet in HasilSearch:
    tweet_properties = {}
    tweet_properties['tanggal'] = tweet.created_at
    tweet_properties['user'] = tweet.user.screen_name
    tweet_properties['isi_tweet'] = tweet.text
    tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split())
    
    analysis = TextBlob(tweet_bersih)
    
    if analysis.sentiment.polarity > 0.0:
        tweet_properties["sentimen"] = "positif"
    elif analysis.sentiment.polarity == 0.0:
        tweet_properties["sentimen"] = "netral"
    else:
        tweet_properties["sentimen"] = "negatif"
        
    if tweet.retweet_count > 0:
        if tweet_properties not in hasilAnalisis:
            hasilAnalisis.append(tweet_properties)
        else:
            hasilAnalisis.append(tweet_properties)


# In[27]:


tweet_positif = [t for t in hasilAnalisis if t["sentimen"]=="positif"]
tweet_netral = [t for t in hasilAnalisis if t["sentimen"]=="netral"]
tweet_negatif = [t for t in hasilAnalisis if t["sentimen"]=="negatif"]


# In[28]:


print("Hasil Sentimen")
print("positif: ", len(tweet_positif), "({} %)".format(100*len(tweet_positif)/len(hasilAnalisis)))
print("netral: ", len(tweet_positif), "({} %)".format(100*len(tweet_netral)/len(hasilAnalisis)))
print("negatif: ", len(tweet_positif), "({} %)".format(100*len(tweet_negatif)/len(hasilAnalisis)))


# In[ ]:




