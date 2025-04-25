import streamlit as st
import os
from fetch_data import fetch_tweets
from analyze_data import analyze_tweets

st.title("Know Your Fan - FURIA Tech")
st.write("Análise de dados dos fãs da FURIA no Twitter")

# Tenta obter as chaves da API dos secrets, recorre a variáveis de ambiente ou permite entrada manual
try:
    API_KEY = st.secrets.get("API_KEY", "")
    API_SECRET = st.secrets.get("API_SECRET", "")
    TOKEN = st.secrets.get("TOKEN", "")
    TOKEN_SECRET = st.secrets.get("TOKEN_SECRET", "")
except Exception:
    # Se os secrets não estiverem disponíveis, inicializa com strings vazias
    API_KEY = ""
    API_SECRET = ""
    TOKEN = ""
    TOKEN_SECRET = ""

# Verifica variáveis de ambiente
if not API_KEY:
    API_KEY = os.environ.get("API_KEY", "")
if not API_SECRET:
    API_SECRET = os.environ.get("API_SECRET", "")
if not TOKEN:
    TOKEN = os.environ.get("TOKEN", "")
if not TOKEN_SECRET:
    TOKEN_SECRET = os.environ.get("TOKEN_SECRET", "")

# Configuração do usuário
st.sidebar.header("Configurações de Pesquisa")
query = st.sidebar.text_input("Digite um termo para pesquisa:", "FURIA eSports")
tweet_count = st.sidebar.slider("Número de tweets para buscar:", 10, 200, 50)

# Permite entrada manual de credenciais da API se não estiverem disponíveis
credentials_expander = st.sidebar.expander("Configurações da API Twitter", expanded=not all([API_KEY, API_SECRET, TOKEN, TOKEN_SECRET]))
with credentials_expander:
    if not all([API_KEY, API_SECRET, TOKEN, TOKEN_SECRET]):
        st.warning("Credenciais da API Twitter não encontradas. Por favor, insira manualmente.")
    
    manual_api_key = st.text_input("API Key:", value=API_KEY, type="password")
    manual_api_secret = st.text_input("API Secret:", value=API_SECRET, type="password")
    manual_token = st.text_input("Access Token:", value=TOKEN, type="password")
    manual_token_secret = st.text_input("Access Token Secret:", value=TOKEN_SECRET, type="password")
    
    # Usa credenciais inseridas manualmente se fornecidas
    API_KEY = manual_api_key or API_KEY
    API_SECRET = manual_api_secret or API_SECRET
    TOKEN = manual_token or TOKEN
    TOKEN_SECRET = manual_token_secret or TOKEN_SECRET

# Analisar Tweets
if st.sidebar.button("Analisar Tweets"):
    if not all([API_KEY, API_SECRET, TOKEN, TOKEN_SECRET]):
        st.error("Por favor, forneça todas as credenciais da API Twitter para continuar.")
    else:
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