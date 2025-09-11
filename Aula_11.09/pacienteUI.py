import streamlit as st
from paciente import Paciente

class PacienteUI:
    def main():
        st.header('Dados do Paciente')
        nome = st.text_input('Nome')
        cpf = st.text_input('CPF')
        fone = st.text_input('Telefone')
        nasc = st.text_input('Data de Nascimento')
        if st.button('Idade'):
            p = Paciente(nome, cpf, fone, nasc)
            st.write(p.Idade())