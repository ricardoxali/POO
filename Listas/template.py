import streamlit as st
import pandas as pd
import time
from datetime import datetime
from view import View

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            fone = st.text_input("Informe o novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                View.cliente_atualizar(id, nome, email, fone)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"):
                id = op.get_id()
                View.cliente_excluir(id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            list_dic = []
            for obj in servicos:
                dic = obj.to_json()
                dic['valor'] = f"R$ {dic['valor']:.2f}"
                list_dic.append(dic)
            df = pd.DataFrame(list_dic)
            df = df.rename(columns={"id": "ID", "desc": "Descrição", "valor": "Valor"})
            st.dataframe(df)
    def inserir():
        desc = st.text_input('Informe a descrição')
        valor = st.text_input('Informe o valor')
        if st.button('Inserir'):
            View.servico_inserir(desc, valor)
            st.success('Serviço inserido com sucesso')
            time.sleep(2)
            st.rerun()
    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            op = st.selectbox('Atualização de Serviços', servicos)
            desc = st.text_input('Nova descrição', op.get_desc())
            valor = st.text_input('Novo valor', f'{op.get_valor():.2f}')
            if st.button('Atualizar'):
                id = op.get_id()
                View.servico_atualizar(id, desc, valor)
                st.success('Serviço atualizado com sucesso')
                time.sleep(2)
                st.rerun()
    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            op = st.selectbox('Exclusão de Serviços', servicos)
            if st.button('Excluir'):
                i = op.get_id()
                View.servico_excluir(i)
                st.success('Serviço excluído com sucesso')
                time.sleep(2)
                st.rerun()

class ManterHorarioUI:
    def main():
        st.header('Cadastro de Horários')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()
    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write('Nenhum horário cadastrado')
        else:
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_desc()
                if profissional != None: profissional = profissional.get_nome()
                dic.append({'id' : obj.get_id(), 'data' : obj.get_data(), 'confirmado' : obj.get_confirmado(), 'cliente' : cliente, 'serviço' : servico, 'profissional' : profissional})
            df = pd.DataFrame(dic)
            st.dataframe(df)
    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissionais = View.profissional_listar()
        data = st.text_input('Informe a data e horário do serviço', datetime.now().strftime('%d/%m/%Y %H:%M'))
        confirmado = st.checkbox('Confirmado')
        cliente, servico, profissional = None, None, None
        if len(clientes) == 0:
            st.warning('⚠️ Nenhum cliente cadastrado.')
        else:
            cliente = st.selectbox('Informe o cliente', clientes, index = None)
        if len(servicos) == 0:
            st.warning('⚠️ Nenhum serviço cadastrado.')
        else:
            servico = st.selectbox('Informe o serviço', servicos, index = None)
        if len(profissionais) == 0:
            st.warning('⚠️ Nenhum profissional cadastrado.')
        else:
            profissional = st.selectbox('Informe o profissional', profissionais, index = None)
            if st.button('Inserir'):
                if profissional == None:
                    st.write('Selecione um profissional')
                else:
                    id_cliente, id_servico, id_profissional = None, None, None
                    if cliente != None:
                        id_cliente = cliente.get_id()
                    if servico != None:
                        id_servico = servico.get_id()
                    if profissional != None:
                        id_profissional = profissional.get_id()
                    View.horario_inserir(datetime.strptime(data, '%d/%m/%Y %H:%M'), confirmado, id_cliente, id_servico, id_profissional)
                    st.success('Horário inserido com sucesso')
                    time.sleep(2)
                    st.rerun()
    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write('Nenhum horário cadastrado')
        else:
            clientes = View.cliente_listar()
            servicos = View.servico_listar()
            profissionais = View.profissional_listar()
            op = st.selectbox('Atualização de Horários', horarios)
            data = st.text_input('Informe a nova data e horário do serviço', op.get_data().strftime('%d/%m/%Y %H:%M'))
            confirmado = st.checkbox('Nova confirmação', op.get_confirmado())
            if op.get_id_cliente() in [0, None]:
                id_cliente = None
            else:
                id_cliente = op.get_id_cliente()
            if op.get_id_servico() in [0, None]:
                id_servico = None
            else:
                id_servico = op.get_id_servico()
            if op.get_id_profissional() in [0, None]:
                id_profissional = None
            else:
                id_profissional = op.get_id_profissional()
            ind = None
            for i, c in enumerate(clientes):
                if c.get_id() == id_cliente:
                    ind = i
                    break
            cliente = st.selectbox('Informe o novo cliente', clientes, index = ind)
            ind = None
            for i, c in enumerate(servicos):
                if c.get_id() == id_servico:
                    ind = i
                    break
            servico = st.selectbox('Informe o novo serviço', servicos, index = ind)
            ind = None
            for i, c in enumerate(profissionais):
                if c.get_id() == id_profissional:
                    ind = i
                    break
            profissional = st.selectbox('Informe o novo profissional', profissionais, index = ind)
            if st.button('Atualizar'):
                id_cliente = None
                id_servico = None
                id_profissional = None
                if cliente != None:
                    id_cliente = cliente.get_id()
                if servico != None:
                    id_servico = servico.get_id()
                if profissional != None:
                    id_profissional = profissional.get_id()
                View.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
                st.success('Horário atualizado com sucesso')
                time.sleep(2)
                st.rerun()
    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write('Nenhum horário cadastrado')
        else:
            op = st.selectbox('Exclusão de Horários', horarios)
            if st.button('Excluir'):
                View.horario_excluir(op.get_id())
                st.success('Horário excluído com sucesso')
                time.sleep(2)
                st.rerun()

class ManterProfissionalUI:
    def main():
        st.header('Cadastro de Profissionais')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()
    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        espec = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        if st.button("Inserir"):
            View.profissional_inserir(nome, espec, conselho)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            espec = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            if st.button("Atualizar"):
                id = op.get_id()
                View.profissional_atualizar(id, nome, espec, conselho)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                View.profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()