# Crie um programa que faça o computador jogar Jokenpô com você.

from typing import Optional
from random import randint
from time import sleep
    
def jokenpo():     
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    pc = randint(0, 2)
    print(''' Suas Opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA ''')
    jogador = int(input('Qual é a sua jogada:'))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('-=' * 11)
    print('O COMPUTADOR JOGOU {}'.format(itens[pc]))
    print('VOÇE JOGOU {}'.format(itens[jogador]))
    print('-=' * 11)

    if pc == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVALIDA')
    elif pc == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
        else :
            print('JOGADA INVALIDA')
    elif pc == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
        else :
            print('JOGADA INVALIDA')
    print('---------------------------------------------------------------')
    opçao = int(input('\033[1;31m Outra rodada ?\n1.Sim\n2.Não\033[m\n'))
    
    if opçao == 1 :
        jokenpo()
    else:
        print('Saindo...')
if __name__ == '__main__' :
    jokenpo()











