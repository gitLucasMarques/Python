#palavra = 'brontosaurus'
#d = dict()
#for c in palavra:
#  if c not in d:
#    d[c] = 1
#  else:
#    d[c] = d[c] + 1
#print(d)
#
#word = 'brontosaurus'
#d = dict()
#for c in word:
#  d[c] = d.get(c,0) + 1
#print(d)


#fname = input("Arquivo: ")
#count = 0
#try:
#  fhand = open(fname)
#  print("\nEmails:")
#  for line in fhand:
#    words = line.split()
#    for word in words:
#      if word == 'From':
#        print(words[1])
#        count += 1
#      continue
#  print('\nContador de linhas com começo "From":',count)
#except:
#  print("Arquivo não encontrado:",fname)

#http://data.pr4e.org/romeo.txt

#import urllib.request
#
#fname = input('Site: ')
#fhand = urllib.request.urlopen(fname)
#
#linhas = 0
#palavrasLinha = 0
#caracteres = 0
#
#for line in fhand:
#  if caracteres >= 3000:
#    break
#  linhas += 1
#  print(line.decode().strip())
#  words = line.decode().split()
#  for word in words:
#    if caracteres >= 3000:
#      break
#    palavrasLinha  += 1
#    for char in word:
#      caracteres += 1
#      if caracteres >= 3000:
#        break
#      continue
#      
#print('\nLinhas =',linhas)
#print('\nPalavras =',palavrasLinha)
#print('\nCaracteres =',caracteres)

help(str.find)