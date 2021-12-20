import tweepy
import keys
import requests
import json
import pandas as pd
import sys

client = tweepy.Client(bearer_token=keys.bearer_token)
tweet_id = sys.argv[1]
rts_dict = {'user':[], 'followers_count': []}

res = requests.get(f'https://api.twitter.com/2/tweets/{tweet_id}/retweeted_by?user.fields=public_metrics',headers={'Authorization': f'Bearer {keys.bearer_token}'})

rts_list = json.loads(res.text)['data']

# print(rts_list)

for rt in rts_list:
    rts_dict['user'].append(rt['username'])
    rts_dict['followers_count'].append(rt['public_metrics']['followers_count'])

df = pd.DataFrame(rts_dict)
df_sorted = df.sort_values('followers_count', ascending=False)

print(df_sorted)

