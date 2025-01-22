import streamlit as st
from pymongo import MongoClient, UpdateOne
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Exemplo Requisição MongoDB com Filtros", page_icon="💰", layout="wide")

# Função auxiliar para pegar os dados do MongoDB
@st.cache_data
def get_dataframe_from_mongodb(collection_name, database_name, query={}):

    client = MongoClient(f"mongodb+srv://rpdprocorpo:iyiawsSCfCsuAzOb@cluster0.lu6ce.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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

st.title("Exemplo Requisição MongoDB com Filtros")

# Inicia o seletor de datas

hoje = datetime.now()
primeiro_dia_do_mes = hoje.replace(day=1)

data_input = st.date_input(
    "Selecione uma data",
    (primeiro_dia_do_mes, hoje),
    format="DD/MM/YYYY",
)

data_inicial = datetime.combine(data_input[0], datetime.min.time())
data_final = datetime.combine(data_input[1], datetime.max.time())

# Faz a query

botao_fazer_query = st.button("Fazer Query")

if botao_fazer_query:
  query = {"date": {"$gte": data_inicial, "$lte": data_final}}
  billcharges_df = get_dataframe_from_mongodb(collection_name="billcharges_db", database_name="dash_midia",query=query)

  st.dataframe(billcharges_df)
