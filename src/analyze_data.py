import pandas as pd

def analyze_tweets(tweets):
    # Convertendo os dados para um DataFrame
    df = pd.DataFrame(tweets)
    
    # Contando as palavras mais usadas
    word_count = df['text'].str.split().explode().value_counts().head(10)
    return word_count