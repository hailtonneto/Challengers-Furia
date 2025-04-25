import streamlit as st
from fetch_data import fetch_tweets
from analyze_data import analyze_tweets

st.title("Know Your Fan - FURIA Tech")
st.write("Análise de dados dos fãs da FURIA no Twitter")

# Obtendo chaves da API do Twitter do secrets.toml
API_KEY = st.secrets["API_KEY"]
API_SECRET = st.secrets["API_SECRET"]
TOKEN = st.secrets["TOKEN"]
TOKEN_SECRET = st.secrets["TOKEN_SECRET"]

# Configuração do usuário
st.sidebar.header("Configurações de Pesquisa")
query = st.sidebar.text_input("Digite um termo para pesquisa:", "FURIA eSports")
tweet_count = st.sidebar.slider("Número de tweets para buscar:", 10, 200, 50)

# Analisar Tweets
if st.sidebar.button("Analisar Tweets"):
    st.write(f"Buscando tweets sobre: {query}")
    
    try:
        with st.spinner('Buscando tweets...'):
            tweets = fetch_tweets(API_KEY, API_SECRET, TOKEN, TOKEN_SECRET, query, tweet_count)
            if tweets:
                st.success(f"Foram encontrados {len(tweets)} tweets.")
                
                word_count = analyze_tweets(tweets)
                
                st.subheader("Palavras mais comuns:")
                st.bar_chart(word_count)
                
                # Mostrar alguns tweets como exemplo
                st.subheader("Alguns tweets encontrados:")
                for i, tweet in enumerate(tweets[:3], 1):
                    st.write(f"{i}. {tweet}")
            else:
                st.warning("Nenhum tweet encontrado.")
    except Exception as e:
        st.error(f"Erro ao buscar tweets: {str(e)}")