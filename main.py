#importa as classes criadas programa principal
import classes as cl
if __name__ =='__main__':
    #entrada de dados
    nome =       input('Informe o nome do usuário:')
    email =      input('Informe  o e-mail do usuário: ')
    cpf =        input('Informe o CPF do usuário: ')
    profissao =  input('Informe a profição do usuário: ')
    endereco =   input('Informe o endereço do usuário: ')
    telefone =   input('Informe o telefone do usuário: ')

    #instancia a classe pessoa fisica
    usuario = cl.PessoaFisica(nome,cpf,profissao,endereco,email,telefone)
    
    #ntrada de dados 

    nome  =        input('informe o nome da empresa: ')
    email =        input('Informe  o e-mail da empresa: ')
    cnpj =         input('Informe o CNPJ da empresa: ')
    razao_social = input('Informe a Razão Social da empresa: ')
    endereco =     input('Informe o endereço da empresa: ')
    telefone =     input('Informe o telefone da empresa: ')


    #instancia a classe a pessoa juridica 
    empresa = cl.PessoaJuridica(nome,razao_social,cnpj,endereco,email,telefone)

    #saida de dados 
    usuario.mostrar_cartao_visitas()
    print('-'*30)
    empresa.mostrar_cartao_visitas()