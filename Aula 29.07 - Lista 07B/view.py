from model import Contato, ContatoDAO
class View:
    @staticmethod
    def contato_inserir(i, no, e, f, na):
        ContatoDAO.inserir(Contato(i, no, e, f, na))
    @staticmethod
    def contato_listar():
        return ContatoDAO.listar()
    @staticmethod
    def contato_listar_id(i):
        return ContatoDAO.listar_id(i)
    @staticmethod
    def contato_atualizar(ind, i, no, e, f, na):
        ContatoDAO.atualizar(ind, Contato(i, no, e, f, na))
    @staticmethod
    def contato_excluir(i):
        ContatoDAO.excluir(i)
    @staticmethod
    def contato_pesquisar(i):
        return ContatoDAO.pesquisar(i)
    @staticmethod
    def contato_aniversariantes(i):
        return ContatoDAO.aniversariantes(i     )