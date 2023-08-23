#15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades dos funcionários de 4 setores da empresa. Para isso, ele te forneceu os seguintes dados:
#{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
# 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 #'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
# 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
#COPIAR CÓDIGO
#Sabendo que cada setor tem 10 funcionários, construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

#Funções

def calculoMediaIdadesPorSetor(lista):
  for setor, idades in lista.items():
    mediaSetor = round(sum(idades)/len(idades))
    mediasSetores[setor] = mediaSetor
  return mediasSetores

def calculoMediaGeral(mediasSetores):
  mediaGeral = round(sum(mediasSetores.values())/len(mediasSetores))
  return mediaGeral

def calculoNumeroPessoasComIdadeAcimaDaMedia(lista):
  nrPessoasComIdadeAcimaDaMediaGeral = 0
  for setor, idades in lista.items():
    for idades in idades:
      if idades > mediaGeral:
        nrPessoasComIdadeAcimaDaMediaGeral += 1
  return nrPessoasComIdadeAcimaDaMediaGeral

def imprimirResultados():
  for setor, media_idades in mediasSetores.items():
    print(f'{setor} Media idades = {media_idades}')
  print(f'\nMedia geral das idades {mediaGeral}' )
  print(f'\nNúmero de pessoas acima da media geral de idade =   {nrPessoasComIdadeAcimaDaMediaGeral}')


#Declaração de Variáveis
lista ={'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
mediasSetores = {}
#Processamento dos dados
mediasSetores = calculoMediaIdadesPorSetor(lista)
mediaGeral = calculoMediaGeral(mediasSetores)
nrPessoasComIdadeAcimaDaMediaGeral = calculoNumeroPessoasComIdadeAcimaDaMedia(lista)
imprimirResultados()  


