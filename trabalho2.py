#questão escolhida 3, questão 4#
import random
nome = input("olá jogador, qual o seu nome?")
escolha = int(input("escolha um numero entre 0 e 1"))
PC1 = random.randint(0,1)
PC2 = random.randint(0,1)
if PC1 == PC2 == escolha:
    print("o jogo está empatado")
if PC1 == PC2 != escolha:
    print("parabéns",nome,"voçê venceu!")
if PC1 != PC2 == escolha:
    print("O jogador 1 venceu")
if PC2 != PC1 == escolha:
    print("O jogador 2 venceu")
print("fim do programa")