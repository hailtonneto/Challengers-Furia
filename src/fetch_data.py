import tweepy

def fetch_tweets(API_KEY, API_SECRET, TOKEN, TOKEN_SECRET, query, count):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(TOKEN, TOKEN_SECRET)
    
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    try:
        tweets = api.search_tweets(q=query, count=count, lang='pt')
        return tweets
    except tweepy.TweepError as e:
        print(f"Erro na requisição: {e}")
        return None
