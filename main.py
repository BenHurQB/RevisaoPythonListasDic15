#15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades dos funcionários de 4 setores da empresa. Para isso, ele te forneceu os seguintes dados:
#{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
# 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 #'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
# 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
#COPIAR CÓDIGO
#Sabendo que cada setor tem 10 funcionários, construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

lista ={'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
somaIdadeSetorA = somaIdadeSetorB = somaIdadeSetorC = somaIdadeSetorD = 0
for chave, valor in lista.items():
  if chave == 'Setor A':
    somaIdadeSetorA = sum(lista['Setor A'])
  elif chave == 'Setor B':
    somaIdadeSetorB = sum(lista['Setor B'])
  elif chave == 'Setor C':
    somaIdadeSetorC = sum(lista['Setor C'])
  else:
    somaIdadeSetorD = sum(lista['Setor D'])
mediaIdadeSetorA = somaIdadeSetorA / 10
mediaIdadeSetorB = somaIdadeSetorB / 10
mediaIdadeSetorC = somaIdadeSetorC / 10
mediaIdadeSetorD = somaIdadeSetorD / 10
mediaGeral = (mediaIdadeSetorA + mediaIdadeSetorB + mediaIdadeSetorC + mediaIdadeSetorD) / 4
nrPessoasComIdadeAcimaDaMediaGeral = 0
for chave, valor in lista.items():
   for valor in valor:
      if valor > mediaGeral:
          nrPessoasComIdadeAcimaDaMediaGeral += 1
print(f'\nMedia Idades por Setor\n')
print(f'\nSetor A = {mediaIdadeSetorA}')
print(f'\nSetor B = {mediaIdadeSetorB}')
print(f'\nSetor C = {mediaIdadeSetorC}')
print(f'\nSetor D = {mediaIdadeSetorD}')
print(f'\nMedia Geral = {mediaGeral}')
print(f'\nNr de pessoas com idade acima da media geral = {nrPessoasComIdadeAcimaDaMediaGeral}')