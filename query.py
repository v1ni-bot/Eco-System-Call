
# Essa query serve para conectar com o banco
#pip install streamlit


from sqlalchemy import create_engine
import pandas as pd
def conexao(query):
    # Crie um engine do SQLAlchemy (substitua pelo URI de conexão do seu banco de dados)
    engine = create_engine('mysql://root:senai%40134@127.0.0.1/bd_medidoreliane')  # Exemplo para SQLite, altere conforme seu banco

    # Use pandas para ler os dados do banco de dados
    df = pd.read_sql(query, engine)
    print(df)
    return df