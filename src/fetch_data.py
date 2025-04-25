import tweepy

def fetch_tweets(api_key, api_secret, token, token_secret, query, count=100):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)
    return api.search_tweets(q=query, count=count, lang='pt')