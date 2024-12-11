from flask import Flask #Para criar a aplicação web com Flask.
from flask_sqlalchemy import SQLAlchemy #Para integração com o banco de dados.
from datetime import datetime
import streamlit as st


# Conexão com o banco de dados com GET, POST, DELET...
app = Flask("registro") # essa função serve para conectar com o banco

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False # Configura o SQLAlCHEMY para rastrear modificações

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:senai%40134@127.0.0.1/bd_medidor'


mybd= SQLAlchemy(app) #Cria uma instância do SQLAlchemy, passando a aplicação Flask como parâmetro.

class Registro_User(mybd.Model):
    __tablename__ = 'tb_usuario'
    id = mybd.Column(mybd.Integer, primary_key=True, autoincrement=True)
    nome = mybd.Column(mybd.String(255))
    email = mybd.Column(mybd.String(255))

class Registro_Canal(mybd.Model):
    __tablename__ = 'tb_canal'
    id = mybd.Column(mybd.Integer, primary_key=True, autoincrement=True)
    nome = mybd.Column(mybd.String(255))
    tipo = mybd.Column(mybd.String(255))
    data_criacao = mybd.Column(mybd.DateTime)

def cadastrar_usuario(nome, email):
    with app.app_context():

        dados_cadastro = Registro_User(
            nome = nome,
            email = email
        )
        mybd.session.add(dados_cadastro)
        mybd.session.commit()
        print("Dados inseridos com sucesso no banco de dados!")

def cadastrar_canal(nome, tipo):
    with app.app_context():

        dados_cadastro = Registro_Canal(
            nome = nome,
            tipo = tipo,
            data_criacao = datetime.now()
        )
        mybd.session.add(dados_cadastro)
        mybd.session.commit()
        print("Dados inseridos com sucesso no banco de dados!")
        return True

if __name__ == '__main__':
    with app.app_context():
        mybd.create_all()
        
        app.run(port=5000, host='localhost', debug=True)
