import streamlit as st
from bd import *
st.title("EcoSystem Call: Criador de Canais")

form = st.form(key="Canal", clear_on_submit=True)

with form:
    input_name=st.text_input("Nome: ", placeholder="Insira o nome do canal")
    input_email=st.text_input("Tipo: ", placeholder="Insira o tipo de canal")
    submit_bt=form.form_submit_button("Cadastrar")

if submit_bt:
    cadastrar_canal(input_name, input_email)