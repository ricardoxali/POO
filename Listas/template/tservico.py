import streamlit as st
import pandas as pd
import time
from Listas.view.vservico import View

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Inserir", "Listar", "Listar ID", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.inserir()
        with tab2: ManterServicoUI.listar()
        with tab3: ManterServicoUI.listar_id()
        with tab4: ManterServicoUI.atualizar()
        with tab5: ManterServicoUI.excluir()
    def inserir():
        desc = st.text_input('Informe a descrição')
        valor = st.text_input('Informe o valor')
        if st.button('Inserir'):
            View.servico_inserir(desc, valor)
            st.success('Serviço inserido com sucesso')
            time.sleep(2)
            st.rerun()
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
    def listar_id():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            id = st.text_input('Informe o ID')
            if st.button('Listar'):
                obj = View.servico_listar_id(id)
                if type(obj) == str:
                    st.write(obj)
                else:
                    dic = obj.to_json()
                    dic['valor'] = f"R$ {dic['valor']:.2f}"
                    df = pd.DataFrame([dic])
                    df = df.rename(columns={"id": "ID", "desc": "Descrição", "valor": "Valor"})
                    st.dataframe(df)
    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            op = st.selectbox('Atualização de Serviços', servicos)
            id_novo = st.text_input('Novo ID', op.get_id())
            desc = st.text_input('Nova descrição', op.get_desc())
            valor = st.text_input('Novo valor', f'{op.get_valor():.2f}')
            if st.button('Atualizar'):
                id_antigo = op.get_id()
                View.servico_atualizar(id_antigo, id_novo, desc, valor)
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
    
class IndexUI:
    def main():
        ManterServicoUI.main()

IndexUI.main()