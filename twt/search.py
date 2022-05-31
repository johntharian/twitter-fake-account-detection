from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys 

import pandas as pd

data=list()

def twt(name):

    created_at=[]
    statuses_count=[]
    followers_count=[]
    friends_count=[] 	
    favourites_count=[] 	
    listed_count 	=[]

    consumer_key="JPpiXxTbFOk3EKjNMxpMIFsAZ"
    consumer_secret="nhsHsTl4v7lYwScZwPfZLz85QITaNASY2evoZwDujmRhs5GI9q"
    access_token="1054754166588014592-wBBya1iu4OnpErV35sVjKM51HJle9T"
    access_token_secret="Mwr5itle2lWItwwnAeqorFkrkkWicowh46JWdkxoIM9eT"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)

    if len(name)>0:
        item = auth_api.get_user(screen_name=name)
        statuses_count.append(item.statuses_count)
        followers_count.append(item.followers_count)
        friends_count.append(item.friends_count)
        favourites_count.append(item.favourites_count) 
        listed_count.append(item.listed_count)
        created_at.append(item.created_at)

    data={'statuses_count':statuses_count,'followers_count':followers_count,'friends_count':friends_count,'favourites_count':favourites_count,'listed_count':listed_count,'created_at':created_at}
    data=pd.DataFrame(data=data)
    return data

if __name__=='__main__':
    twt()