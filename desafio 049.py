preco_produto = float(input('Digite o valor do produto: '))
tipoPagamento = input('Qual o tipo de pagamento? ').strip().lower()


if preco_produto and tipoPagamento == 'dinheiro' or tipoPagamento == 'cheque':
    desconto10 = preco_produto * 10/100
    print(f'Você ganhou um desconto de 10%, \no desconto fica R${desconto10:.2f}')
    print(f'O atual valor do produto fica R${preco_produto - desconto10:.2f}')
elif preco_produto and tipoPagamento == 'cartão':
    avista = input('A compra é à vista?(sim/não)').strip().lower()
    if avista == 'sim':
        desconto5 = preco_produto * 5/100
        print(f'Você ganhou um desconto de 5%, \no desconto fica R${desconto5:.2f}')
        print(f'O atual valor do produto fica R${preco_produto - desconto5:.2f} ')
    if avista == 'não':
        duasVezes = input('Duas vezes no cartão?(sim/não) ')
        print(f'O valor do produto continua R${preco_produto:.2f}')









