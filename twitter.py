import snscrape.modules.twitter as sntwitter
import numpy as np
import pandas as pd
import json
# Import data processing helper
from helpers import process_results

 
def get_data(hashtag): 
    #query = "rophnan until:2022-09-08 since:2022-07-10"
    query = hashtag
    tweets = []
    limit = 100

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        
        #print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.id, tweet.date, tweet.url, tweet.user.username, tweet.sourceLabel, tweet.user.location, tweet.content, tweet.likeCount, 
            tweet.retweetCount, tweet.quoteCount, tweet.replyCount, tweet.mentionedUsers, tweet.retweetedTweet, tweet.quotedTweet, tweet.user.created,
            tweet.user.description, tweet.user.displayname, tweet.user.favouritesCount, tweet.user.followersCount, tweet.user.friendsCount,tweet.user.id, 
            tweet.user.label, tweet.user.location, tweet.user.mediaCount, tweet.user.profileBannerUrl, tweet.user.profileImageUrl, tweet.user.rawDescription,
            tweet.user.statusesCount, tweet.user.verified  ])
           
            
    df = pd.DataFrame(tweets, columns=['tweet_id','Date', 'TweetURL','User', 'Source', 'Location', 'Tweet', 'Likes_Count','Retweet_Count', 'Quote_Count', 
        'Reply_Count','Mentioned_Users','Retweeted_Tweet', 'Quoted_Tweet', 'User_Created', 'User_Description', 'User_Displayname', 'User_FavouritesCount', 
        'User_FollowersCount', 'User_FriendsCount', 'User_Id', 'User_Label', 'User_Location', 'User_MediaCount', 'User_ProfileBannerUrl', 'User_ProfileImageUrl',
        'User_RawDescription', 'User_StatusesCount', 'User_Verified' ])
   
   
    # to save to csv
    #df.to_csv('twitterdata.csv',index = False)
    if hashtag =="#EthiopianAirlines":
        df.to_csv('EthiopianAirlines.csv',mode='a',index = False, header=False)
    if hashtag =="#SafaricomEthiopia":
        df.to_csv('SafaricomEthiopia.csv', mode='a',index = False, header=False)    
    if hashtag =="#BeuDelivery":
        df.to_csv('BeuDelivery.csv', mode='a',index = False, header=False)
#########################################
            #print(tweet.cashtags)
            #print(tweet.content)
            #print(tweet.conversationId)
            #print(tweet.coordinates)
            #print(tweet.hashtags)
            #print(tweet.id)
            #print(tweet.inReplyToTweetId)
            #print(tweet.inReplyToUser)
            #print(tweet.json)
            #print(tweet.lang)
            #print(tweet.likeCount)
            #print(tweet.media)
            #print(tweet.mentionedUsers)
            #print(tweet.outlinks)
            #print(tweet.place)
            #print(tweet.quoteCount)
            #print(tweet.quotedTweet)
            #print(tweet.renderedContent)
            #print(tweet.replyCount)
            #print(tweet.retweetCount)
            #print(tweet.retweetedTweet)
            #print(tweet.source)
            #print(tweet.sourceLabel)
            #print(tweet.sourceUrl)
            #print(tweet.tcooutlinks)
            #print(tweet.url)
            #print(tweet.user)
            #print(tweet.user.created)
            #print(tweet.user.description)
            #print(tweet.user.descriptionUrls)
            #print(tweet.user.displayname)
            #print(tweet.user.favouritesCount)
            #print(tweet.user.followersCount)
            #print(tweet.user.friendsCount)
            #print(tweet.user.id)
            #print(tweet.user.json)
            #print(tweet.user.label)
            #print(tweet.user.linkTcourl)
            #print(tweet.user.listedCount)
            #print(tweet.user.location)
            #print(tweet.user.mediaCount)
            #print(tweet.user.profileBannerUrl)
            #print(tweet.user.profileImageUrl)
            #print(tweet.user.protected)
            #print(tweet.user.rawDescription)
            #print(tweet.user.statusesCount)
            #print(tweet.user.url)
            #print(tweet.user.username)
            #print(tweet.user.verified)
            