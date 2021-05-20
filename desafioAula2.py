# programa da entrevista sobre a administração do prefeito#
print("avaliação da administração do municipio de jatobá de dentro")
n = int(input("quantas pessoas serão entrevistadas? :"))
soma = 0
for i in range (n):
    nota = float(input("dê uma nota entre 0 e 10 para avaliação da administração do municipio: "))
    soma = soma + nota
media = soma / n
print("sua administração recebeu nota:", soma)
print("sua administração tem media de:", media)