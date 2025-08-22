from cabecalho import exibir_cabecalho

exibir_cabecalho('DESAFIO 55', '22/08/2025')

preco = float(input('Digite o valor do produto: '))

pag = ('dinheiro', 'débito', 'crédito', 'pix' )

parc = 0

print('''OPÇÕES:
      [1] - DINHEIRO
      [2] - DÉBITO
      [3] - CRÉDITO
      [4] - PIX
      ''')

opcao = int(input('Qual a forma de pagamento desejada? '))-1

print(f'Escolheu: {(pag[opcao])}')

if opcao == 0 or opcao == 3:
    print(f'O valor com 10%: R$ {preco - preco * 10/100}')

elif opcao == 1:
    print(f'O VALOR COM 5%: R$ {preco - preco * 5/100:.2f}')

elif opcao == 2:
    parc = int(input('Quantas vezes você deseja parcelar? '))
    if parc == 2:
        print(f'O valor da sua compra total é {preco:.2f}')
        print(f'A sua parcela é R$ {preco / parc:.2f}')
    if parc == 3:
        print(f'O valor da sua compra total é {preco + preco * 20/100:.2f}')
        print(f'A sua parcela é R$ {preco / parc:.2f}')
    if parc > 3:
        print(f'O valor da sua compra total é {preco + preco * 30/100:.2f}')
        print(f'A sua parcela é R$ {preco / parc:.2f}')
            









"""

pagamento = input('Qual a forma de pagamento?(dinheiro/cartão1, cartão2, cartão3)').strip().lower()

if pagamento == 'dinheiro':
    desconto10 = preco * 10/100
    print(f'Pagamento à vista no dinheiro tem direito a 10% de desconto = R${desconto10:.2f},\n Valor atual fica R${preco - desconto10:.2f}')
else:
    if pagamento == 'cartão1':
        desconto5 = preco * 5/100
        print(f'Pagamento à vista no cartão tem direito a 5% de desconto = R${desconto5:.2f}, \n Valor atual fica R${preco - desconto5:.2f}')
    else:
        if pagamento == 'cartão2':
            print(f'Pagamento em até 2x no cartão, o valor fica R${preco}')
        else:
            if pagamento == 'cartão3':
                juros20 = preco * 20/100
                print(f'Pagamento em 3x ou mais, há juros de 20% = R${}')
"""
          
