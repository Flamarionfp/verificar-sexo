print('Verificar Sexo')
nome = str(input('Digite seu nome: ')).title()
sexo = ''
if nome.endswith('a'):
    sexo = 'Feminino'
    print('Com base no meu algoritmo acredito que você é do sexo {}, certo?'.format(sexo))
    res = int(input('Digite 1 para sim ou 2 para não: '))
    while res != 1 and res != 2:
        print('Resposta inválida')
        res = int(input('Digite 1 para sim ou 2 para não: '))
    if res == 2:
        sexo = 'Masculino'
elif nome.endswith('o'):
        sexo = 'Masculino'
        print('Com base no meu algoritmo você é do sexo {}, certo?'.format(sexo))
        res = int(input('Digite 1 para sim ou 2 para não: '))
        while res != 1 and res != 2:
            print('Reposta inválida')
            res = int(input('Digite 1 para sim ou 2 não: '))
        if res == 2:
            sexo = 'Feminino'
else:
    sexo = str(input('Qual o seu sexo (F/M)? ')).strip().upper()
    while sexo != 'F' and sexo != 'M':
        print('Sexo inválido!')
        sexo = str(input('Qual o seu sexo (F/M)? ')).strip().upper()
    if sexo == 'F':
        sexo = 'Feminino'
    else:
        sexo = 'Masculino'
print('Nome: {}'.format(nome))
print('Sexo: {}'.format(sexo))
