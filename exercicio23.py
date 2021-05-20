print("calculo do custo de energia de um ar condicionado no RN, ligado 8 horas por dia durante 1 mês")
custo = 0.34250
custoDoArCondicionado = 850 / 1000
quantidadeDeKW = custoDoArCondicionado * 8
custoDiario = quantidadeDeKW * custo
custoMensal = custoDiario * 30
print("o ar condicionado gasta",quantidadeDeKW,"KW por dia")
print("logo o consumo diario do ar é:", custoDiario )
print("logo em 30 dias o consumo é de:", custoMensal)