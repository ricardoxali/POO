import streamlit as st
from view import View
from template import ManterClienteUI, ManterServicoUI, ManterHorarioUI, ManterProfissionalUI
from UI import LoginUI, AbrirContaUI, PerfilClienteUI, PerfilProfissionalUI

class IndexUI:
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Profissionais", "Cadastro de Horários"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
    def menu_visitante():
        op = st.sidebar.selectbox('Menu', ['Entrar no Sistema', 'Abrir Conta'])
        if op == 'Entrar no Sistema': LoginUI.main()
        if op == 'Abrir Conta': AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox('Menu', ['Meus Dados'])
        if op == 'Meus Dados': PerfilClienteUI.main()
    def menu_profissional():
        op = st.sidebar.selectbox('Menu', ['Meus Dados'])
        if op == 'Meus Dados': PerfilProfissionalUI.main()
    def sair_sistema():
        if st.sidebar.button('Sair'):
            del st.session_state['usuario_id']
            del st.session_state['usuario_nome']
            st.rerun()
    def sidebar():
        if 'usuario_id' not in st.session_state:
            IndexUI.menu_visitante()
        else:
            user = st.session_state['usuario_nome']
            st.sidebar.write('Bem-vindo(a), ' + st.session_state['usuario_nome'])
            if user == 'admin':
                IndexUI.menu_admin()
            elif user in [p.get_nome() for p in View.profissional_listar()]:
                IndexUI.menu_profissional()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_sistema()
    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()