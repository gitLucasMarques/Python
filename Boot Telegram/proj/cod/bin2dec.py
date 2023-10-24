print('Tamanho do binário: ', end="")
tam = int(input())

print('bin = ', end="")
bin = str(input())

while len(bin) != tam:
  print('O número binário tem mais/menos de ' + str(tam) + ' dígitos. Tente novamente!')
  print('bin = ', end="")
  bin = str(input())

aux = str(bin)
for i in aux:
  if int(i) == 0 or int(i) == 1:
    continue
  else:
    print('Há dígitos diferentes de 0 e 1 no binário.')

dec = 0
for i in aux:
  dec = (dec * 2) + int(i)

print('dec =', dec)
