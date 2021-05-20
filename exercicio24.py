print("vamos calcular a média de suas notas!")
valorMedia = float(input("qual a media para aprovação na sua instituição?"))
quantidadeNotas = int(input("primeiro informe quantas notas voçê vai calcular :"))
i = 1
soma = 0
while i <= quantidadeNotas:
    nota = float(input("digite uma nota:"))
    soma = soma + nota
    i = i + 1
print("agora que temos as notas vamos calcular sua media e saber se foi aprovado ou não")
media = (soma / quantidadeNotas)
print("sua média foi",media)
if media >= valorMedia:
    print("parabéns voçê foi aprovado")
else:
    print("é uma pena! mas voçê foi reprovado.")