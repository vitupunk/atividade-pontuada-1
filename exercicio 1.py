#Escrever um algoritmo que solicite ao usuário um
#número e faça a contagem regressiva a partir do
#número informado até o número 1, aguardando um
#segundo para exibir cada número.


import streamlit as st
import time

st.title("Contagem Regressiva")

numero = st.number_input("Digite um número para iniciar a contagem regressiva:", min_value=1, step=1)

if st.button("Iniciar contagem"):
    contador = st.empty()  
    for i in range(numero, 0, -1):
        contador.write(f"{i}")
        time.sleep(1)
    st.write("Contagem regressiva finalizada!")
