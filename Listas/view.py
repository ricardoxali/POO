from model import Cliente, Servico, Horario, Profissional
from dao import ClienteDAO, ServicoDAO, HorarioDAO, ProfissionalDAO
from datetime import datetime

class View:
    def cliente_inserir(n, e, f, s):
        usuarios = []
        for obj in View.cliente_listar():
            usuarios.append(obj)
        for obj in View.profissional_listar():
            usuarios.append(obj)
        if e == 'admin':
            raise ValueError('E-mail Inválido')
        for obj in usuarios:
            if obj.get_email() == e:
                raise ValueError('E-mail já cadastrado')
        c = Cliente(0, n, e, f, s)
        ClienteDAO.inserir(c)
    def cliente_listar():
        c = ClienteDAO.listar()
        c.sort(key=lambda obj:obj.get_nome())
        return c
    def cliente_listar_id(i):
        return ClienteDAO.listar_id(i)
    def cliente_atualizar(i, n, e, f, s):
        user_atual = View.cliente_listar_id(i)
        admin = user_atual.get_email() == 'admin'
        if not admin and e == 'admin':
            raise ValueError('E-mail Inválido')
        usuarios = []
        for obj in View.cliente_listar():
            if obj.get_id() != i:
                usuarios.append(obj)
        for obj in View.profissional_listar():
            usuarios.append(obj)
        for obj in usuarios:
            if obj.get_email() == e:
                raise ValueError('E-mail já cadastrado')
        c = Cliente(i, n, e, f, s)
        ClienteDAO.atualizar(c)
    def cliente_excluir(i):
        for obj in View.horario_listar():
            if obj.get_id_cliente() == i:
                raise ValueError('Cliente com agendamento ativo: não é possível excluir')
        c = Cliente(i, 'none', 'none', 'none', 'none')
        ClienteDAO.excluir(c)
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        ClienteDAO.inserir(Cliente(0, 'admin', 'admin', 'fone', '1234')) # Pular a verificação do View.cliente_inserir()
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id":c.get_id(), "nome":c.get_nome()}
        return None

    def servico_inserir(d, v):
        for obj in View.servico_listar():
            if obj.get_desc() == d:
                raise ValueError('Serviço já cadastrado')
        s = Servico(0, d, v)
        ServicoDAO.inserir(s)
    def servico_listar():
        s = ServicoDAO.listar()
        s.sort(key=lambda obj:obj.get_desc())
        return s
    def servico_listar_id(i):
        return ServicoDAO.listar_id(i)
    def servico_atualizar(i, d, v):
        for obj in View.servico_listar():
            if obj.get_id() != i and obj.get_desc() == d:
                raise ValueError('Descrição já cadastrada em outro serviço')
        s = Servico(i, d, v)
        ServicoDAO.atualizar(s)
    def servico_excluir(i):
        for obj in View.horario_listar():
            if obj.get_id_servico() == i:
                raise ValueError('Serviço já agendado: não é possível excluir')
        s = Servico(i, 'none', 1)
        ServicoDAO.excluir(s)

    def horario_inserir(d, c, id_cliente, id_servico, id_profissional):
        for obj in View.horario_listar():
            if obj.get_data() == d:
                if obj.get_id_profissional() == id_profissional:
                    raise ValueError('Horário já cadastrado')
        h = Horario(0, d)
        h.set_confirmado(c)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.inserir(h)
    def horario_listar():
        h = HorarioDAO.listar()
        h.sort(key=lambda obj:obj.get_data())
        return h
    def horario_listar_id(i):
        return HorarioDAO.listar_id(i)
    def horario_atualizar(i, d, c, id_cliente, id_servico, id_profissional):
        for obj in View.horario_listar():
            if obj.get_data() == d and obj.get_id_profissional() == id_profissional and obj.get_id() != i:
                raise ValueError('Horário já cadastrado')
        h = Horario(i, d)
        h.set_confirmado(c)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(h)
    def horario_excluir(i):
        for obj in View.horario_listar():
            if obj.get_id() == i and obj.get_id_cliente() != None:
                raise ValueError('Horário agendado: não é possível excluir')
        h = Horario(i, datetime.now())
        HorarioDAO.excluir(h)
    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional: # Ver se der erro
                r.append(h)
        r.sort(key=lambda h:h.get_data())
        return r

    def profissional_inserir(n, es, c, em, s):
        usuarios = []
        for obj in View.cliente_listar():
            usuarios.append(obj)
        for obj in View.profissional_listar():
            usuarios.append(obj)
        if em == 'admin':
            raise ValueError('E-mail Inválido')
        for obj in usuarios:
            if obj.get_email() == em:
                raise ValueError('E-mail já cadastrado')
        p = Profissional(0, n, es, c, em, s)
        ProfissionalDAO.inserir(p)
    def profissional_listar():
        p = ProfissionalDAO.listar()
        p.sort(key=lambda obj:obj.get_nome())
        return p
    def profissional_listar_id(i):
        return ProfissionalDAO.listar_id(i)
    def profissional_atualizar(i, n, es, c, em, s):
        usuarios = []
        for obj in View.cliente_listar():
            usuarios.append(obj)
        for obj in View.profissional_listar():
            if obj.get_id() != i:
                usuarios.append(obj)
        if em == 'admin':
            raise ValueError('E-mail Inválido')
        for obj in usuarios:
            if obj.get_email() == em:
                raise ValueError('E-mail já cadastrado')
        p = Profissional(i, n, es, c, em, s)
        ProfissionalDAO.atualizar(p)
    def profissional_excluir(i):
        for obj in View.horario_listar():
            if obj.get_id_profissional() == i:
                raise ValueError('Profissional com agendamento ativo: não é possível excluir')
        p = Profissional(i, 'none', 'none', 'none', 'none', 'none')
        ProfissionalDAO.excluir(p)
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id":p.get_id(), "nome":p.get_nome()}
        return None