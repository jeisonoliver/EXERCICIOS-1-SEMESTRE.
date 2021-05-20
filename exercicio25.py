import random

print("seja bem vindo ao jogo de dados eletronico")
print("vamos sortear números aleatorios que vão corresponder a voçê humano, e a maquina! ")
i = input("deseja jogar?(S/N)")
pontosHumano = 0
pontosMaquina = 0
empate = 0
while i == "S":
    dadoHumano = random.randint(1, 6)
    print("o valor da face do dado correspondente ao jogador é", dadoHumano)
    dadoMaquina = random.randint(1, 6)
    print("o valor da face do dado correspondente a maquina é", dadoMaquina)
    if dadoHumano > dadoMaquina:
        print("parabéns voçê venceu!")
        pontosHumano = pontosHumano + 1
    elif dadoHumano == dadoMaquina:
        print("o jogo terminou empate!")
        empate = empate + 1
    else:
        print("infelizmente voçê perdeu!")
        pontosMaquina = pontosMaquina + 1
    i = input("deseja jogar novamente?(S/N)")
print("O jogador fez", pontosHumano, "pontos\nA maquina fez", pontosMaquina,"pontos \nO jogo ficou empatado", empate, "vezes")
print("obrigado por jogar nosso joguinho!")