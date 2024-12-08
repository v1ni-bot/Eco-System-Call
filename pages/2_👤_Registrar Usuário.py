import streamlit as st
from bd import *
st.title("Cadastre-se no EcoSystem Call!")

form = st.form(key="Clientes", clear_on_submit=True)

with form:
    input_name=st.text_input("Nome: ", placeholder="Insira seu nome")
    input_email=st.text_input("Email: ", placeholder="Insira seu email")

    submit_bt=form.form_submit_button("Cadastrar")

if submit_bt:
    cadastrar_usuario(input_name, input_email)