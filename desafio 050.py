from random import choice

print('->' * 50)
jokenpo = input('Escolha pedra, papel ou tesoura: ').strip().lower()

comput = ['pedra', 'papel', 'tesoura']
npc = choice(comput)

if jokenpo == npc:
    print('EMPATE')
elif jokenpo == 'papel' and npc == 'pedra':
    print(f'Você ganhou!! {jokenpo} embrulha a {npc}')
elif jokenpo == 'pedra' and npc == 'tesoura':
    print(f'Você ganhou!!, {jokenpo} quebra a {npc}')
elif jokenpo == 'tesoura'and npc == 'papel':
    print(f'Você ganhou!!!, {jokenpo} corta o {npc}')
elif jokenpo == 'pedra' and npc =='papel':
    print(f'Você perdeu!!, escolhi {npc} e {npc} embrulha a {jokenpo}')
elif jokenpo == 'tesoura' and npc == 'pedra':
    print(f'Você perdeu!!, escolhi {npc} and {npc} quebra a {jokenpo}')
elif jokenpo == 'papel' and npc == 'tesoura':
    print(f'Você perdeu!!, escolhi {npc} and {npc} corta o {jokenpo}')
else:
    print('Opção Inválida, tente outra vez!')