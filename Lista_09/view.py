from model import Servico, ServicoDAO
class View:
    def servico_inserir(d, v):
        ServicoDAO.inserir(Servico(0, d, v))
    def servico_listar():
        return ServicoDAO.listar()
    def servico_listar_id(i):
        return ServicoDAO.listar_id(i)
    def servico_atualizar(i, d, v):
        ServicoDAO.atualizar(Servico(i, d, v))
    def servico_excluir(i):
        ServicoDAO.excluir(i)