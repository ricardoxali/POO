from model import Cliente, Servico, Horario, Profissional
from model import ClienteDAO, ServicoDAO, HorarioDAO, ProfissionalDAO

class View:
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(c)
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(c)
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(c)
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id":c.get_id(), "nome":c.get_nome()}
        return None

    def servico_inserir(d, v):
        s = Servico(0, d, v)
        ServicoDAO.inserir(s)
    def servico_listar():
        return ServicoDAO.listar()
    def servico_listar_id(i):
        return ServicoDAO.listar_id(i)
    def servico_atualizar(i, d, v):
        s = Servico(i, d, v)
        ServicoDAO.atualizar(s)
    def servico_excluir(i):
        s = Servico(i, '', 1)
        ServicoDAO.excluir(s)

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(0, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.inserir(h)
    def horario_listar():
        return HorarioDAO.listar()
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(id, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(h)
    def horario_excluir(i):
        h = Horario(i, '1/1/2000')
        HorarioDAO.excluir(h)

    def profissional_inserir(nome, espec, conselho, email, senha):
        p = Profissional(0, nome, espec, conselho, email, senha)
        ProfissionalDAO.inserir(p)
    def profissional_listar():
        return ProfissionalDAO.listar()
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    def profissional_atualizar(id, nome, espec, conselho, email, senha):
        p = Profissional(id, nome, espec, conselho, email, senha)
        ProfissionalDAO.atualizar(p)
    def profissional_excluir(i):
        p = Profissional(i, '', '', '', '', '')
        ProfissionalDAO.excluir(p)
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id":p.get_id(), "nome":p.get_nome()}
        return None