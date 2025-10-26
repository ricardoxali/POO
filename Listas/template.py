from view import View
from datetime import datetime
import streamlit as st
import pandas as pd
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    def listar():
        clientes = [c for c in View.cliente_listar() if c.get_email() != 'admin'] # Retira o admin
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes:
                if obj.get_email() != "admin": list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            df = df.rename(columns={"id":"ID", "nome":"Nome", "email":"E-mail", "fone":"Telefone", "senha":"Senha"})
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail", None)
        fone = st.text_input("Informe o telefone")
        senha = st.text_input("Informe a senha", None, type="password")
        if st.button("Inserir"):
            try:
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Cliente inserido com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
    def atualizar():
        clientes = [c for c in View.cliente_listar() if c.get_email() != 'admin'] # Retira o admin
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            fone = st.text_input("Informe o novo fone", op.get_fone())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.cliente_atualizar(id, nome, email, fone, senha)
                    st.success("Cliente atualizado com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
    def excluir():
        clientes = [c for c in View.cliente_listar() if c.get_email() != 'admin'] # Retira o admin
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.cliente_excluir(id)
                    st.success("Cliente excluído com sucesso")
                except ValueError as erro:
                    st.error(erro)
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
            try: 
                View.servico_inserir(desc, float(valor))
                st.success('Serviço inserido com sucesso')
            except ValueError as erro:
                st.error(erro)
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
                try:
                    id = op.get_id()
                    View.servico_atualizar(id, desc, float(valor))
                    st.success('Serviço atualizado com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            op = st.selectbox('Exclusão de Serviços', servicos)
            if st.button('Excluir'):
                try:
                    i = op.get_id()
                    View.servico_excluir(i)
                    st.success('Serviço excluído com sucesso')
                except ValueError as erro:
                    st.error(erro)
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
            list_dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_desc()
                if profissional != None: profissional = profissional.get_nome()
                list_dic.append({'ID':obj.get_id(), 'Data':obj.get_data(), 'Confirmado':obj.get_confirmado(), 'Cliente':cliente, 'Serviço':servico, 'Profissional':profissional})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        clientes = [c for c in View.cliente_listar() if c.get_email() != 'admin'] # Retira o admin
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
            if st.button('Inserir'): # VERIFICAR
                try:
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
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write('Nenhum horário cadastrado')
        else:
            clientes = [c for c in View.cliente_listar() if c.get_email() != 'admin'] # Retira o admin
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
            if st.button('Atualizar'): # VERIFICAR
                try:
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
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write('Nenhum horário cadastrado')
        else:
            op = st.selectbox('Exclusão de Horários', horarios)
            if st.button('Excluir'):
                try:
                    View.horario_excluir(op.get_id())
                    st.success('Horário excluído com sucesso')
                except ValueError as erro:
                    st.error(erro)
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
            df = df.rename(columns={"id":"ID", "nome":"Nome", "especialidade":"Especialidade", "conselho":"Conselho","email":"E-mail", "senha":"Senha"})
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        espec = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input('Informe o email')
        senha = st.text_input('Informe a senha', type='password')
        if st.button("Inserir"):
            try:
                View.profissional_inserir(nome, espec, conselho, email, senha)
                st.success("Profissional inserido com sucesso")
            except ValueError as erro:
                st.error(erro)
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
            email = st.text_input('Informe o novo email', op.get_email())
            senha = st.text_input('Informe a nova senha', op.get_senha(), type='password')
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.profissional_atualizar(id, nome, espec, conselho, email, senha)
                    st.success("Profissional atualizado com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.profissional_excluir(id)
                    st.success("Profissional excluído com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

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
            try:
                View.cliente_inserir(nome, email, fone, senha)
                st.success('Conta criada com sucesso')
            except ValueError as erro:
                st.error(erro)
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
            try:
                id = op.get_id()
                View.cliente_atualizar(id, nome, email, fone, senha)
                st.success('Cliente atualizado com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

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
            try:
                id = op.get_id()
                View.profissional_atualizar(id, nome, espec, conselho, email, senha)
                st.success('Profissional atualizado com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

class AgendarServicoUI:
    def main():
        st.header('Agendar Serviço')
        profs =  View.profissional_listar()
        if len(profs) == 0: st.write('Nenhum profissional cadastrado')
        else:
            profissional = st.selectbox('Informe o profissional', profs)
            horarios = View.horario_agendar_horario(profissional.get_id())
            if len(horarios) == 0: st.write('Nenhum horário disponível')
            else:
                horario = st.selectbox('Informe o horário', horarios)
                servicos = View.servico_listar()
                servico = st.selectbox('Informe o serviço', servicos)
                if st.button('Agendar'):
                    View.horario_atualizar(horario.get_id(), horario.get_data(), False, st.session_state['usuario_id'], servico.get_id(), profissional.get_id())
                    st.success('Horário agendado com sucesso')
                    time.sleep(2)
                    st.rerun()

class AbrirMinhaAgendaUI:
    def main():
        st.header('Abrir Minha Agenda')
        data = st.text_input('Informe a data no formato dd/mm/aaaa')
        horario_inicial = st.text_input('Informe o horário inicial no formato HH:MM')
        horario_final = st.text_input('Informe o horário final no formato HH:MM')
        intervalo = st.text_input('Informe o intervalo entre os horários (min)')
        if st.button('Abrir Agenda'):
            try: # VERIFICAR
                hora_inicial, min_inicial = map(int, horario_inicial.split(':'))
                hora_final, min_final = map(int, horario_final.split(':'))
                inicio_total = hora_inicial * 60 + min_inicial
                fim_total = hora_final * 60 + min_final
                while inicio_total <= fim_total:
                    hora = inicio_total // 60
                    minuto = inicio_total % 60
                    data_hora = datetime.strptime(f'{data} {hora:02d}:{minuto:02d}', '%d/%m/%Y %H:%M')
                    View.horario_inserir(data_hora, False, None, None, st.session_state['usuario_id'])
                    inicio_total += int(intervalo)
                st.success('Horários abertos com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

class VisualizarMinhaAgendaUI:
    def main():
        st.header('Visualizar Minha Agenda')
        list_dic = []
        for h in View.horario_listar():
            if h.get_id_profissional() == st.session_state['usuario_id']:
                cliente = h.get_id_cliente()
                if cliente != None:
                    cliente = View.cliente_listar_id(cliente).get_nome()
                servico = h.get_id_servico()
                if servico != None:
                    servico = View.servico_listar_id(servico).get_desc()
                list_dic.append({'ID':h.get_id(), 'Data':h.get_data(), 'Confirmado':h.get_confirmado(), 'Cliente':cliente, 'Serviço':servico})
        if len(list_dic) == 0: st.write('Agenda Vazia')
        else:
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

class VisualizarMeusServicosUI:
    def main():
        st.header('Visualizar Meus Serviços')
        list_dic = []
        for h in View.horario_listar():
            if h.get_id_cliente() == st.session_state['usuario_id']:
                servico = View.servico_listar_id(h.get_id_servico())
                if servico != None:
                    servico = servico.get_desc()
                profissional = View.profissional_listar_id(h.get_id_profissional()).get_nome()
                list_dic.append({'ID':h.get_id(), 'Data':h.get_data(), 'Confirmado':h.get_confirmado(), 'Serviço':servico, 'Profissional':profissional})
        if len(list_dic) == 0: st.write('Nenhum serviço agendado')
        else:
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

class ConfirmarServicoUI:
    def main():
        st.header('Confirmar Serviço')
        horarios = []
        for h in View.horario_listar():
            if h.get_id_profissional() == st.session_state['usuario_id'] and not h.get_confirmado() and h.get_id_cliente() != None:
                horarios.append(h)
        if len(horarios) == 0:
            st.write('Nenhum serviço pendente')
            return
        h = st.selectbox('Informe o horário', horarios)
        if h != None:
            cliente = View.cliente_listar_id(h.get_id_cliente())
            cliente = st.selectbox('Cliente', cliente, disabled = True)
            if st.button('Confirmar'):
                View.horario_atualizar(h.get_id(), h.get_data(), True, h.get_id_cliente(), h.get_id_servico(), st.session_state['usuario_id'])
                st.success('Serviço confirmado com sucesso')
                time.sleep(2)
                st.rerun()

class AlterarSenhaUI:
    def main():
        st.header('Alterar Senha')
        senha = st.text_input('Informe a nova senha', type='password')
        for c in View.cliente_listar():
            if c.get_nome() == 'admin':
                if st.button('Alterar'):
                    View.cliente_atualizar(c.get_id(), c.get_nome(), c.get_email(), c.get_fone(), senha)
                    st.success('Senha atualizada com succeso')
                    time.sleep(2)
                    st.rerun()