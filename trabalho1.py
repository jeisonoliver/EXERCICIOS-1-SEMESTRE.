#questão escolhida 2, questão 3#
#programa do dado eletronico#
import random
nome1 = input("digite o nome do jogador 1")
print("o valor desses dados pertencem a:", nome1)
numeroDado = random.randint(1,6)
if numeroDado == 1:
    print("#########\n#       #\n#   *   #\n#       #\n#########")
elif numeroDado == 2:
    print("#########\n# *     #\n#       #\n#     * #\n#########")
elif numeroDado == 3:
    print("#########\n#*      #\n#   *   #\n#      *#\n#########")
elif numeroDado == 4:
    print("#########\n# *   * #\n#       #\n# *   * #\n#########")
elif numeroDado == 5:
    print("#########\n# *   * #\n#   *   #\n# *   * #\n#########")
elif  numeroDado == 6:
    print("#########\n# *   * #\n# *   * #\n# *   * #\n#########")

numeroDado1 = random.randint(1,6)
if numeroDado1 == 1:
    print("#########\n#       #\n#   *   #\n#       #\n#########")
elif numeroDado1 == 2:
    print("#########\n# *     #\n#       #\n#     * #\n#########")
elif numeroDado1 == 3:
    print("#########\n#*      #\n#   *   #\n#      *#\n#########")
elif numeroDado1 == 4:
    print("#########\n# *   * #\n#       #\n# *   * #\n#########")
elif numeroDado1 == 5:
    print("#########\n# *   * #\n#   *   #\n# *   * #\n#########")
elif  numeroDado1 == 6:
    print("#########\n# *   * #\n# *   * #\n# *   * #\n#########")

soma = numeroDado + numeroDado1

print("o valor dos dois dados somados é:", soma)

nome2 = input("digite o nome do segundo jogador")

print("o valor desses dados pertencem a:",nome2)

numeroDado2 = random.randint(1,6)

if numeroDado2 == 1:
    print("#########\n#       #\n#   *   #\n#       #\n#########")
elif numeroDado2 == 2:
    print("#########\n# *     #\n#       #\n#     * #\n#########")
elif numeroDado2 == 3:
    print("#########\n#*      #\n#   *   #\n#      *#\n#########")
elif numeroDado2 == 4:
    print("#########\n# *   * #\n#       #\n# *   * #\n#########")
elif numeroDado2 == 5:
    print("#########\n# *   * #\n#   *   #\n# *   * #\n#########")
elif  numeroDado2 == 6:
    print("#########\n# *   * #\n# *   * #\n# *   * #\n#########")

numeroDado3 = random.randint(1,6)
if numeroDado3 == 1:
    print("#########\n#       #\n#   *   #\n#       #\n#########")
elif numeroDado3 == 2:
    print("#########\n# *     #\n#       #\n#     * #\n#########")
elif numeroDado3 == 3:
    print("#########\n#*      #\n#   *   #\n#      *#\n#########")
elif numeroDado3 == 4:
    print("#########\n# *   * #\n#       #\n# *   * #\n#########")
elif numeroDado3 == 5:
    print("#########\n# *   * #\n#   *   #\n# *   * #\n#########")
elif  numeroDado3 == 6:
    print("#########\n# *   * #\n# *   * #\n# *   * #\n#########")

soma1 = numeroDado2 + numeroDado3

print("o valor dos dois dados somados é:",soma1)

if soma > soma1:
    print("parabéns",nome1,"voçê venceu!")
else: print("parabéns",nome2,"voçê voçê venceu!")