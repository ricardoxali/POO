from view import View
import template
import streamlit as st

class IndexUI:
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ['Cadastro de Clientes', 'Cadastro de Serviços', 'Cadastro de Profissionais', 'Cadastro de Horários', 'Alterar Senha', 'Feedback de Profissionais'])
        if op == 'Cadastro de Clientes': template.ManterClienteUI.main()
        if op == 'Cadastro de Serviços': template.ManterServicoUI.main()
        if op == 'Cadastro de Profissionais': template.ManterProfissionalUI.main()
        if op == 'Cadastro de Horários': template.ManterHorarioUI.main()
        if op == 'Alterar Senha': template.AlterarSenhaUI.main()
        if op == 'Feedback de Profissionais': template.FeedbackUI.main()
    def menu_visitante():
        op = st.sidebar.selectbox('Menu', ['Entrar no Sistema', 'Abrir Conta'])
        if op == 'Entrar no Sistema': template.LoginUI.main()
        if op == 'Abrir Conta': template.AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox('Menu', ['Meus Dados', 'Agendar Serviço', 'Visualizar Meus Serviços'])
        if op == 'Meus Dados': template.PerfilClienteUI.main()
        if op == 'Agendar Serviço': template.AgendarServicoUI.main()
        if op == 'Visualizar Meus Serviços': template.VisualizarMeusServicosUI.main()
    def menu_profissional():
        op = st.sidebar.selectbox('Menu', ['Meus Dados', 'Abrir Minha Agenda', 'Visualizar Minha Agenda', 'Confirmar Serviço'])
        if op == 'Meus Dados': template.PerfilProfissionalUI.main()
        if op == 'Abrir Minha Agenda': template.AbrirMinhaAgendaUI.main()
        if op == 'Visualizar Minha Agenda': template.VisualizarMinhaAgendaUI.main()
        if op == 'Confirmar Serviço': template.ConfirmarServicoUI.main()
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