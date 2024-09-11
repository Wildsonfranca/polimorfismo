#classe chamada (Veiculo) superclasse , classe-pai,classe base
class Pessoa:
    #atributos
    def __init__(self,endereco,email,telefone):
        self.endereco = endereco
        self.email= email
        self.telefone = telefone


    #método
    def mostrar_cartao_visitas(self):
        print(f'Endereço: {self.endereco}.')
        print(f'E-mail: {self.email}.')
        print(f'Telefone: {self.telefone}.')    



# subclasse,classe-filha,classe derivada Pessoa física
class PessoaFisica(Pessoa):
    #POLIMORFISMO DO CONSTRUTOR
    def __init__(self,nome,cpf,proficao ,endereco, email,telefone):
        self.nome = nome
        self.cpf =cpf
        self.proficao =proficao
        super().__init__(endereco,email,telefone)

    def mostrar_cartao_visitas(self):
        print(f'Nome do usuário: {self.nome}.')
        print(f'CPF so usuário : {self.cpf}.')
        print(f'Profição do usuário: {self.proficao}.')
        super().mostrar_cartao_visitas()


class PessoaJuridica(Pessoa):
    # polimorfismo do construtor
    def __init__(self,nome_fantasia,razao_social,cnpj,endereco,email,telefone):
        self.nome_fantasia = nome_fantasia
        self.razao_social =razao_social
        self.cnpj = cnpj
        super().__init__(endereco,email,telefone) 

    def mostrar_cartao_visitas(self):
        print(f'Nome da empresa: {self.nome_fantasia}.')
        print(f'Razão Social: {self.razao_social}.')
        print(f'CNPJ: {self.cnpj}.')
        super().mostrar_cartao_visitas()          