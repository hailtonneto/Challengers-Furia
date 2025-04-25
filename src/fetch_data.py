import tweepy

def authenticate_twitter(API_KEY, API_SECRET, TOKEN, TOKEN_SECRET):
    """
    Autentica na API do Twitter usando Tweepy.
    """
    try:
        auth = tweepy.OAuth1UserHandler(
            API_KEY, 
            API_SECRET,
            TOKEN,
            TOKEN_SECRET
        )
        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api
    except Exception as e:
        raise Exception(f"Erro ao autenticar: {str(e)}")

def fetch_tweets(API_KEY, API_SECRET, TOKEN, TOKEN_SECRET, query, count):
    """
    Busca tweets com base no termo de pesquisa fornecido.
    """
    try:
        api = authenticate_twitter(API_KEY, API_SECRET, TOKEN, TOKEN_SECRET)
        tweets = api.search_tweets(q=query, count=count, lang="pt", tweet_mode="extended")
        return [tweet.full_text for tweet in tweets]
    except tweepy.TweepyException as e:
        raise Exception(f"Erro ao buscar tweets: {str(e)}")
    except Exception as e:
        raise Exception(f"Erro inesperado: {str(e)}")