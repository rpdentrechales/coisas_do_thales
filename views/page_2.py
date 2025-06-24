import streamlit as st
import certifi
from pymongo import MongoClient, UpdateOne
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Exemplo Requisição MongoDB sem Filtros", page_icon="💰", layout="wide")

# Função auxiliar para pegar os dados do MongoDB
@st.cache_data(show_spinner="📡 Pulling from MongoDB…")
def get_dataframe_from_mongodb(
        collection_name: str,
        database_name: str,
        query: dict | None = None
) -> pd.DataFrame:
    query = {} if query is None else query

    # Never hard-code secrets – read them from an env-var or secrets manager
    uri = "mongodb+srv://thalesprocorpoestetica:Proc%402025@cluster0.tkcrpgj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"      # mongodb+srv://user:pass@cluster0.…
    client = MongoClient(
        uri,
        serverSelectionTimeoutMS=10000,    # 10 s is enough for Atlas
        tls=True,
        tlsCAFile=certifi.where()          # <- key line: use up-to-date bundle
    )

    data = list(client[database_name][collection_name].find(query))
    df = pd.DataFrame(data).drop(columns=["_id"], errors="ignore")
    return df

st.title("Exemplo Requisição MongoDB sem Filtros")

botao_fazer_query = st.button("Fazer Query")

if botao_fazer_query:

  df = get_dataframe_from_mongodb(collection_name="custos_fixos_2025", database_name="rentabilidade_anual")

  st.dataframe(df)


