# programa da entrevista sobre a administração do prefeito#
print("avaliação da administração do municipio de jatobá de dentro")
soma = 0
pessoas = 0
i = input("deseja responder a pesquisa? (S/N):")
i = i.upper()
if i == "N":
    print("OK! obrigado pela atenção!")
elif i == "S":
    while i == "S":
        pessoas += 1
        print("voçê é o entrevistado de número:",pessoas)
        nota = float(input("dê uma nota entre 0 e 10 para avaliação da administração do municipio: "))
        soma = soma + nota
        i = input("deseja responder a pesquisa? (S/N):")
        i = i.upper()
    media = soma / pessoas
print("sua administração recebeu nota:", soma)
print("sua administração tem media de:", media)