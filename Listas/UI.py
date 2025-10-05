from view import View
import streamlit as st
import time

class LoginUI:
    def main():
        st.header('Entrar no Sistema')
        email = st.text_input('Informe o e-mail')
        senha = st.text_input('Informe a senha', type="password")
        if st.button('Entrar'):
            user = View.cliente_autenticar(email, senha) or View.profissional_autenticar(email, senha)
            if user:
                st.session_state["usuario_id"] = user["id"]
                st.session_state["usuario_nome"] = user["nome"]
                st.rerun()
            else:
                st.write("E-mail ou senha inválidos")


class AbrirContaUI:
    def main():
        st.header('Abrir Conta no Sistema')
        nome = st.text_input('Informe o nome')
        email = st.text_input('Informe o email')
        fone = st.text_input('Informe a telefone')
        senha = st.text_input('Informe a senha', type='password')
        if st.button('Inserir'):
            View.cliente_inserir(nome, email, fone, senha)
            st.success('Conta criada com sucesso')
            time.sleep(2)
            st.rerun()

class PerfilClienteUI:
    def main():
        st.header('Meus Dados')
        op = View.cliente_listar_id(st.session_state['usuario_id'])
        nome = st.text_input('Informe o novo nome', op.get_nome())
        email = st.text_input('Informe o novo e-mail', op.get_email())
        fone = st.text_input('Informe o novo telefone', op.get_fone())
        senha = st.text_input('Informe a nova senha', op.get_senha(), type='password')
        if st.button('Atualizar'):
            id = op.get_id()
            View.cliente_atualizar(id, nome, email, fone, senha)
            st.success('Cliente atualizado com sucesso')

class PerfilProfissionalUI:
    def main():
        st.header('Meus Dados')
        op = View.profissional_listar_id(st.session_state['usuario_id'])
        nome = st.text_input('Informe o novo nome', op.get_nome())
        espec = st.text_input('Informe a nova especialidade', op.get_especialidade())
        conselho = st.text_input('Informe o novo conselho', op.get_conselho())
        email = st.text_input('Informe o novo email', op.get_email())
        senha = st.text_input('Informe a nova senha', op.get_senha(), type='password')
        if st.button('Atualizar'):
            id = op.get_id()
            View.profissional_atualizar(id, nome, espec, conselho, email, senha)
            st.success('Profissional atualizado com sucesso')