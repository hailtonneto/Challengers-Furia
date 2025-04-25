import streamlit as st
from fetch_data import fetch_tweets
from analyze_data import analyze_tweets

st.title("Know Your Fan - FURIA Tech")
st.write("Análise de dados dos fãs da FURIA no Twitter")

# Preenchendo chaves da API do Twitter (substitua com suas próprias)
API_KEY = "sua_api_key"
API_SECRET = "sua_api_secret"
TOKEN = "seu_token"
TOKEN_SECRET = "seu_token_secret"

# Input do usuário
st.sidebar.header("Configurações de Pesquisa")
query = st.sidebar.text_input("Digite um termo para pesquisa:", "FURIA eSports")
tweet_count = st.sidebar.slider("Número de tweets para buscar", 10, 500, 100)

if st.button("Analisar Tweets"):
    st.write(f"Buscando tweets com o termo: {query}")
    
    # Buscar e analisar tweets
    tweets = fetch_tweets(API_KEY, API_SECRET, TOKEN, TOKEN_SECRET, query, tweet_count)
    word_count = analyze_tweets(tweets)
    
    # Exibir gráfico com as palavras mais comuns
    st.write("Palavras mais comuns nos tweets:")
    st.bar_chart(word_count)
