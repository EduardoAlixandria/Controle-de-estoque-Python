#-------- Inicio das Variaveis Gerais -------
lista_peca=[]
codigo_peca=0

#-------- Fim das Variaveis Gerais -------

#-------- Início de cadastrarPeça() -----
def cadastrarPeça(codigo):
   print('Bem-Vindo ao menu de Cadastro de Peça')
   print('Código da Peça: {:0>3}' .format(codigo))
   peca = input("Digite o NOME da peça: ")
   fabricante = input("Digite o FABRICANTE da peça: ")
   valor = float(input("Digite o VALOR (R$) da peça: "))
   dicionario_peca={'Código' : codigo,
                    'Peça' : peca,
                    'Fabricante' : fabricante,
                    'Valor' : valor}
   lista_peca.append(dicionario_peca.copy())

#-------- Fim de cadastrarPeça() -----

#-------- Início de consultarPeca() -----
def consultarPeca():
   print('Bem-Vindo ao menu de Consulta de Peça')
   while True:
       opcao_Mconsulta = input('\n Escolha a opção desejada: \n' +
                                '1- Consultar Todas as Peças\n' +
                                '2- Consultar Peças por Código \n' +
                                '3- Consultar Peças por Fabricante\n' +
                                '4- Retornar\n' +
                                '=>')
       if opcao_Mconsulta == '1':
           print('Voçe escolheu a opção consultar TODAS as peças!')
           for peca in lista_peca: #Vai mostrar toda a lista de peças
             print('-------------------------------')
             for key, value in peca.items(): #Varre os conjuntos chave e valor do dicionario peca
               print('{}: {}' .format(key,value))
             print('-------------------------------')
       elif opcao_Mconsulta == '2':
           print('Voçe escolheu a opção consultar peças por CÓDIGO!')
           valor_desejado = int(input('Digite o CÓDIGO desejado: '))
           for peca in lista_peca:
              if peca['Código'] == valor_desejado: #O valor do campo código desse dicionario é igual o valor desejado
                  print('-------------------------------')
                  for key, value in peca.items():  # Varre os conjuntos chave e valor do dicionario peca
                      print('{}: {}'.format(key, value))
              print('-------------------------------')
       elif opcao_Mconsulta == '3':
           print('Voçe escolheu a opção cconsultar peças por FABRICANTE!')
           valor_desejado = input('Digite o FABRICANTE desejado: ')
           for peca in lista_peca:
               if peca['Fabricante'] == valor_desejado:  # O valor do campo código desse dicionario é igual o valor desejado
                   print('-------------------------------')
                   for key, value in peca.items():  # Varre os conjuntos chave e valor do dicionario peca
                       print('{}: {}'.format(key, value))
               print('-------------------------------')
       elif opcao_Mconsulta == '4':
           return  #Retorna ao menu anterior
       else:
           print('Opção Inválida. Tente Novamente')
           continue  # Volta ao inicio do laço


#-------- Fim de consultarPeca() -----

#-------- Início de removerpeca() -----
def removerPeca():
   print('Bem-Vindo ao menu de Remover Peça')
   valor_desejado=int(input('Digite o código do produto a ser removido: '))
   for peca in lista_peca:
       if peca['Código'] == valor_desejado:
        lista_peca.remove(peca)
        print('Peça removida com sucesso!')

#-------- Fim de removerPeca() -----

#-------- Início de Main -----
print('Bem-Vindo ao sistema de controle de estoque da bicicletaria do João Alixandria')
while True:
    opcao_Mprincipal = input('\n Escolha a opção desejada: \n' +
                                 '1- Cadastrar Peça\n' +
                                 '2- Consultar Peça(s) \n' +
                                 '3- Remover Peça\n' +
                                 '4- Sair\n' +
                                 '=>')
    if opcao_Mprincipal == '1':
        codigo_peca=codigo_peca+1
        cadastrarPeça(codigo_peca)
    elif opcao_Mprincipal == '2':
        consultarPeca()
    elif opcao_Mprincipal == '3':
        removerPeca()
    elif opcao_Mprincipal == '4':
        break #Encerra o programa
    else:
        print('Opção Inválida. Tente Novamente')
        continue #Volta ao inicio do laço

#-------- Fim de Main -----
