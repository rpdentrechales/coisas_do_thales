import streamlit as st
from pymongo import MongoClient, UpdateOne
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Exemplo Requisição MongoDB sem Filtros", page_icon="💰", layout="wide")

# Função auxiliar para pegar os dados do MongoDB
@st.cache_data
def get_dataframe_from_mongodb(collection_name, database_name, query={}):
    uri = "mongodb+srv://thalesprocorpoestetica:Proc%402025@cluster0.tkcrpgj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    client = MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]

    data = list(collection.find(query))

    if data:
        dataframe = pd.DataFrame(data)
        if '_id' in dataframe.columns:
            dataframe = dataframe.drop(columns=['_id'])
    else:
        dataframe = pd.DataFrame()

    return dataframe

st.title("Exemplo Requisição MongoDB sem Filtros")

botao_fazer_query = st.button("Fazer Query")

if botao_fazer_query:

  df = get_dataframe_from_mongodb(collection_name="custos_fixos_2025", database_name="rentabilidade_anual")

  st.dataframe(df)


