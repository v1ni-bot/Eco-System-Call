
# Essa query serve para conectar com o banco
#pip install mysql-connector-python
#pip install streamlit
"""
import mysql.connector
import pandas as pd

def conexao(query): # vai buscar no arquivo do dash
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="senai@134",
        db="bd_medidor"
    )

    dataframe= pd.read_sql(query, conn) # vai retornar a query
    conn.close() #vai fechar a conexão

    return dataframe
"""

from sqlalchemy import create_engine
import pandas as pd
def conexao(query):
    # Crie um engine do SQLAlchemy (substitua pelo URI de conexão do seu banco de dados)
    engine = create_engine('mysql://root:senai%40134@127.0.0.1/bd_medidor')  # Exemplo para SQLite, altere conforme seu banco

    # Use pandas para ler os dados do banco de dados
    df = pd.read_sql(query, engine)
    print(df)
    return df