import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_player import st_player

from query import *

# Consulta no banco de dados

query = "SELECT * FROM tb_registro" #Dados a receber
df = conexao(query) # Consume a função do banco e retorna o dataframe com os dados

#Transforma os dados de data em formato de data do pandas
df["tempo_registro"] = pd.to_datetime(df["tempo_registro"])
df=df.sort_values("tempo_registro")

#Cria uma nova tabela para filtrar por dia
df["dia"] = df["tempo_registro"].apply(lambda x: str(x.year) + "-" + str(x.month)+ "-" + str(x.day))


# Página

st.set_page_config(layout="wide", page_title="EcoSystemCall", page_icon="icon.png") #Configura a aplicação ao tamanho total da página

# Sidebar
st.sidebar.image("logoo.png", use_container_width=True) #Coloca imagem no sidebar

#Filtro por dia
st.sidebar.header("Filtros")
dia = st.sidebar.selectbox("Dia", df["dia"].unique())
df_filtered = df[df["dia"] ==  dia]

#Filtro por temperatura
temperatura_range = st.sidebar.slider(
"Temperatura (ºC)",
min_value=float(df["temperatura"].min()),   #indica o valor mínimo 
max_value=float(df["temperatura"].max()),   #indica o valor máximo
value=(float(df["temperatura"].min()), float(df["temperatura"].max())), #Faixa de valores selecionados
step=0.1 #incremento para cada movimento do slider
)

#Filtro por umidade
umidade_range = st.sidebar.slider(
"Umidade (%)",
min_value=float(df["umidade"].min()),  # Indica o valor mínimo
max_value=float(df["umidade"].max()),  # Indica o valor máximo
value=(float(df["umidade"].min()), float(df["umidade"].max())),  # Faixa de valores selecionados
step=0.1  # Incremento para cada movimento do slider
)

#Filtro por altitude
altitude_range = st.sidebar.slider(
"Altitude (m)",
#min_value=float(df["altitude"].min()),
max_value=float(df["altitude"].max()),
value=(float(df["altitude"].min()), float(df["altitude"].max()))
)

#Filtro por pressao
pressao_range = st.sidebar.slider(
"Pressao (p)",
min_value=float(df["pressao"].min()),   #indica o valor mínimo 
max_value=float(df["pressao"].max()),   #indica o valor máximo
value=(float(df["pressao"].min()), float(df["pressao"].max())), #Faixa de valores selecionados
step=0.1 #incremento para cada movimento do slider
)

#Filtro por CO2
co2_range = st.sidebar.slider(
"CO2 (ppm)",
min_value=float(df["co2"].min()),   #indica o valor mínimo 
max_value=float(df["co2"].max()),   #indica o valor máximo
value=(float(df["co2"].min()), float(df["co2"].max())), #Faixa de valores selecionados
step=0.1 #incremento para cada movimento do slider
)

#Filtro por poeira
poeira_range = st.sidebar.slider(
"Poeira (p)",
min_value=float(df["poeira"].min()),   #indica o valor mínimo 
max_value=float(df["poeira"].max()),   #indica o valor máximo
value=(float(df["poeira"].min()), float(df["poeira"].max())), #Faixa de valores selecionados
step=0.1 #incremento para cada movimento do slider
)

# Body
st.title("Eco System Call") #Titulo
st.header("Seu contato pessoal ao clima, diretamente a você!")
st.info("Últimos dados coletados", icon="📈")

#Atualizar os dados
if st.button("Atualizar Dados"): 
    df = conexao(query)


abaG, abaSC, aba3,  = st.tabs(["Guaianases", "São Caetano do Sul","Cidade 3"])

with abaG:

    # Montando o grid
    col1, col2 = st.columns(2)
    col3,col4,col5 = st.columns(3)

    # Gráfico 1: Temperatura

    fig_temp = px.line(df, x="id", y="temperatura", title="Registro de temperatura") #Definindo parametros do gráfico
    fig_temp.update_layout(
        yaxis=dict(range=[0, 100]),
        plot_bgcolor='#DDEAE7'
        )
    col1.plotly_chart(fig_temp, use_container_width=True) # Printando o gráfico

    #Gráfico 2: Umidade
    fig_umi = px.bar(df, x="id", y="umidade", title="Registro de umidade") #Definindo parametros do gráfico
    fig_umi.update_layout(
        yaxis=dict(range=[0, 100]),
        plot_bgcolor='#DDEAE7'
        )
    col2.plotly_chart(fig_umi, use_container_width=True) # Printando o gráfico

    #Gráfico 3: Pressão
    fig_press = px.bar(df, x="id", y="pressao", title="Registro de pressão", orientation="h") #Definindo parametros do gráfico
    fig_press.update_layout(
        yaxis=dict(range=[0, 100]),
        plot_bgcolor='#DDEAE7'
        )
    col3.plotly_chart(fig_press, use_container_width=True) # Printando o gráfico

    #Gráfico 4: CO2
    fig_co = px.scatter(df, x="id", y="co2", title="Registro de CO2") #Definindo parametros do gráfico
    fig_co.update_layout(
        yaxis=dict(range=[0, 100]),
        plot_bgcolor='#DDEAE7'
        )
    col4.plotly_chart(fig_co, use_container_width=True) # Printando o gráfico

    #Gráfico 5: Temperatura dnv
    fig_temp2 = px.bar(df, x="id", y="altitude", title="Registro de temperatura") #Definindo parametros do gráfico
    fig_temp2.update_layout(
        yaxis=dict(range=[0, 100]),
        plot_bgcolor='#DDEAE7'
        )
    col5.plotly_chart(fig_temp2, use_container_width=True) # Printando o gráfico


