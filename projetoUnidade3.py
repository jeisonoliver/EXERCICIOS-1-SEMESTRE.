veiculo = {}

clientes = {}

resp = "9"
while resp.lower() != "0":
      print()
      print("***************************************")
      print("******* locadora de automoveis ********")
      print("***************************************")
      print("**** Menu de funções do programa: *****")
      print("***************************************")
      print("****** 1. Cadastrar veículo ***********")
      print("****** 2. Consultar veículo ***********")
      print("****** 3. Alterar veículo *************")
      print("****** 4. Excluir veículo *************")
      print("****** 5. Alugar veículo **************")
      print("****** 6. Devolver veículo ************")
      print("****** 7. obter lista de locatarios ***")
      print("****** 0. Encerrar programa ***********")
      print("***************************************")
      resp = input("Escolha sua opção: ")

      if resp == "1":
        placa = input("Qual a placa do veículo a cadastrar? Ex: (XXX-0000):")
        marca = input("Qual a marca do veículo? ")
        modelo = input("Qual o modelo ou nome do veículo? ")
        ano = input("Qual o ano de fabricação do veículo? ")
        diaria = float(input("Qual o valor da diária? "))
        veiculo[placa] = [marca, modelo, ano, diaria, True]
        print("Veículo de placa %s foi cadastrado com sucesso"%placa)

      elif resp == '2':
        placa = input("Qual a placa do veículo a consultar? Ex: (XXX-0000):")
        if placa in veiculo:
            print()
            print('Placa  :', placa)
            print('Marca  :', veiculo[placa][0])
            print('Modelo :', veiculo[placa][1])
            print('Ano    :', veiculo[placa][2])
            print('Diária : R$ %.2f' % veiculo[placa][3])
            if veiculo[placa][4]:
                print('Status: Veículo disponível')
            else:
                print('Status: Veículo não disponível')
        else:
            print('Veículo %s não está cadastrado!' % placa)
      elif resp == '3':
          placa = input("Qual a placa do veículo a alterar? ")
          if placa in veiculo:
              print()
              print("Qual item deseja alterar?")
              print("a. Marca")
              print("b. Modelo")
              print("c. Ano")
              print("d. Valor da diária")
              print("e. Disponibilidade")
              item = input("Escolha um item: ")
              item = item.lower()
              if item == 'a':
                  marca = input("Qual a marca do veículo? ")
                  veiculo[placa][0] = marca
              elif item == 'b':
                  modelo = input("Qual o modelo do veículo? ")
                  veiculo[placa][1] = modelo
              elif item == 'c':
                  ano = input("Qual o ano do veículo? ")
                  veiculo[placa][2] = ano
              elif item == 'd':
                  diaria = float(input("Qual o valor da diária? "))
                  veiculo[placa][3] = diaria
              elif item == 'e':
                  veiculo[placa][4] = not (veiculo[placa][4])
              else:
                  print("Item informado não é válido")
              print("Veículo %s alterado com sucesso" % placa)
          else:
              print('Veículo %s não está cadastrado!' % placa)
      elif resp == '4':
          placa = input("Qual a placa do veículo que você deseja excluir? ")
          if placa in veiculo:
              print()
              print("Veículo localizado:")
              print()
              print('Placa  :', placa)
              print('Marca  :', veiculo[placa][0])
              print('Modelo :', veiculo[placa][1])
              print('Ano    :', veiculo[placa][2])
              print('Diária : R$ %.2f' % veiculo[placa][3])
              if veiculo[placa][4]:
                  print('Status: Veículo disponível')
              else:
                  print('Status: Veículo não disponível')
              confirma = input("Confirma a exclusão do veículo (s/n)? ")
              confirma = confirma.lower()
              if confirma == 's':
                  del veiculo[placa]
                  print("Veículo %s excluído com sucesso" % placa)
              else:
                  print("Veículo %s continua no cadastro" % placa)
          else:
              print('Veículo %s não está cadastrado!' % placa)
      elif resp == '5':
        placa = input("Qual a placa do veículo a alugar? ")
        if placa in veiculo:
          if veiculo[placa][4]:
            print()
            print('Status: Veículo disponível')
            print('Placa  :', placa)
            print('Marca  :', veiculo[placa][0])
            print('Modelo :', veiculo[placa][1])
            print('Ano    :', veiculo[placa][2])
            print('Diária : R$ %.2f'%veiculo[placa][3])
            confirma = input('Confirma locação (s/n)? ')
            if confirma.lower() == 's':
              veiculo[placa][4] = False
              CPF = input('qual o CPF do locatario?:')
              nome = input("qual o nome do locatario?:")
              telefone = input("qual o telefone para contato?:")
              email = input("qual o email do locatario?:")
              clientes[CPF] = [nome, telefone, email, placa]
              diarias = input('qual a quantidade de diarias? ')
              print ("veiculo alugado com sucesso!")
            else:
              print('Ok, temos outros modelos disponíveis')
          else:
            print('Status: Veículo não disponível')
        else:
          print('Veículo %s não está cadastrado!'%placa)
      elif resp == '6':
        placa = input("Qual a placa do veículo a devolver? ")
        if placa in veiculo:
          if not(veiculo[placa][4]):
            print()
            qdeDiarias = float(input("Qual diárias a cobrar? "))
            valor = qdeDiarias * veiculo[placa][3]
            print("Valor da locação: R$ %.2f"%valor)
            veiculo[placa][4] = True
            print("Veículo %s foi devolvido"%placa)
            print("Obrigado por usar nossos serviços")
          else:
            print('Status: Veículo não está alugado')
        else:
          print('Veículo %s não está cadastrado!'%placa)
      elif resp == '7':