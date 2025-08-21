nota = float(input('Digite a sua nota: '))
print('<>'* 50)
trabalhoExtra = input('Você tem um trabalho extra?(sim/não) ').strip().lower()
print('<>' * 50)

if nota >= 7 or trabalhoExtra == 'sim':
    print('APROVADO!')
else:
    print('REPROVADO')
