class Contato:
    def __init__(self, nome: str, celular: str):
        self.nome = nome
        self.celular = celular

class Mensagem:
    def __init__(self, destinatario: Contato, horaEnvio: str, conteudo: str):
        self.destinatario = destinatario
        self.horaEnvio = horaEnvio
        self.conteudo = conteudo

class Whatsapp:
    def __init__(self):
        self.contatos = []
        self.mensagens = []

    def listarContatos(self):
        for contato in self.contatos:
            print(f'Nome: {contato.nome}, Celular: {contato.celular}')

    def listarMensagens(self):
        for mensagem in self.mensagens:
            print(f'Destinatário: {mensagem.destinatario.nome}, Hora de Envio: {mensagem.horaEnvio}, Conteúdo: {mensagem.conteudo}')
