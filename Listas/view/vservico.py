from Listas.model.mservico import Servico, ServicoDAO
class View:
    def servico_inserir(d, v):
        ServicoDAO.inserir(Servico(0, d, v))
    def servico_listar():
        return ServicoDAO.listar()
    def servico_listar_id(i):
        return ServicoDAO.listar_id(i)
    def servico_atualizar(id_antigo, id_novo, d, v):
        ServicoDAO.atualizar(id_antigo, Servico(id_novo, d, v))
    def servico_excluir(i):
        ServicoDAO.excluir(i)