media = float(input('Digite a sua média: '))

frequencia = int(input('Qual a sua frequência? '))

if media >= 7 or media >= 5 and frequencia >= 75:
    print('Aprovado')
else:
    print('Reprovado')