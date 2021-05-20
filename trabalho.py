#questão escolhida 1, questão 2#
#programa do dado eletronico#
import random
numeroDado = random.randint(1,6)
print(numeroDado)
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
print("fim do programa")