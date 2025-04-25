import pandas as pd

def analyze_tweets(tweets):
    df = pd.DataFrame(tweets)
    word_count = df['text'].str.split().explode().value_counts().head(10)
    return word_count