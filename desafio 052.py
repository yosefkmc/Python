loginUsuario = 'yosefkmc'
senhaUsuario = 'kmc141'


login = input('Digite o seu usuário: ')

senha = input('Digite a sua senha: ')

if login == loginUsuario and senha == senhaUsuario:
    print('Acesso autorizado!')
else:
    print('Não autorizado, usuário ou senha incorreta')