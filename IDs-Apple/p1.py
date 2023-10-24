fname = input('Aqruivo: ')
fhand = open(fname)

for line in fhand:
  print(line.strip())