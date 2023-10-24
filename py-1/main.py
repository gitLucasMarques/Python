#nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
#print(nums, end="")

#def repeat(nums):
# for i in nums:
#if i == 4:
#   return print(i, end="Acabou!")
#  else:
#     return print("Opção 2")
#repeat(nums)

#import sys
#print("Versão Python")
#print(sys.version)
#print(sys.version_info)

#Faça um programa em linguagem Python que converta metros para centímetros.
#med = int(input("Digite um valor em metros: "))
#print(med, "metros possuem",med * 100,"centímetros!")

#Faça um programa em Python que leia um valor inteiro
#e mostre a tabuada de 1 a 10 do valor lido.
#num = int(input("Digite um valor: "))
#print("Tabuada do", num)
#for i in range(1,11):
#  print(i,"X",num,"=",i*num)

#Faça um algoritmo em linguagem Python que receba duas notas
#e calcule a média aritmética e mostre o resultado.
#n1 = float(input("Nota 1: "))
#n2 = float(input("Nota 2: "))
#print("Média =", (n1+n2)/2)

#Fazer um algoritmo que ao receber o salário atual de um funcionário,
#calcule o valor do novo salário reajustado de acordo com a tabela abaixo:
#Salário < 500, Reajuste de 15%
#500 <= Salário <= 1000, Reajuste de 10%
#Salario > 1000, Reajuste de 5%
#from decimal import Decimal
#
#sal = float(input("Digite seu salário: R$ "))
#if sal < 500:
#  reaj = sal * 1.15
#else:
#if sal >= 500 or sal <= 1000:
# reaj = sal * 1.10
#else:
#   if sal > 1000:
#      reaj = sal * 1.05
#print("Seu novo salário é: R$", reaj)

#Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5.
#Os números obtidos devem ser impressos em sequência.
#for i in range(5,100):
#if i % 7 == 0 and i % 5 !=0 :
# print(i)
#else:
# continue

#Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado.
#Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).
#num = int(input("Digite um valor: "))
#soma = 0
#for i in range (1, num+1):
#  if i == num:
#    soma += i
#    print("A soma é:",soma)
#  else:
#    soma += i

#Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.
#num = int(input("Digite um número: "))
#if num < 0:
#  print("Número negativo!")
#else:
#  if num > 0:
#    print("Número positivo!")
#  else:
#    if num == 0:
#      print("Número neutro!")

#Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o resultado.
#Por exemplo, se o número é 2021 , então a saída deve ser 4
#num = int(input("Digite um número: "))
#i = 0
#while num != 0:
#  num //= 10
#  i+=1
#print("Este número possui", i, "dígitos!")

#Faça um programa em linguagem Python, que lê um número n
#e imprime os n primeiros números da sequência de Fibonacci.
#n = int(input("Digite um número: "))
#num0 = 0
#num1 = 1
#i = 0
#print(0)
#while i < n:
#  num2 = num0 + num1
#  num0 = num1
#  num1 = num2
#  i += 1
#  print(num0)

#Faça	uma	função	que calcule a	média	de	um	aluno	de	acordo	com	o	critério	definido
#neste	curso.	Além	disso,	 faça	uma	segunda	 função	que	informe	o	status	do	aluno	de
#cordo	com	a	tabela	a	seguir:
#Nota	acima	de	6	à “Aprovado”
#Nota	entre	4	e	6	à Conceito	“Verificação	Suplementar”
#Nota	abaixo	de	4	à Conceito	“Reprovado”

#def media(n1, n2):
#  med = (n1+n2)/2
#  if med > 6:
#    print("Aprovado!")
#  else:
#    if med >= 4 and med <= 6:
#      print("Verificação Suplementar")
#    else:
#      if med < 4:
#        print("Reprovado!")

#n1 = float(input("Digite a nota 1: "))
#n2 = float(input("Digite a nota 2: "))

#media(n1, n2)

#Leia	 do	 usuário	 o	 tempo	 em	 segundos	 e o	 escreva	 em	 horas,	 minutos	 e	 segundos.
#Utilize	 cinco	 métodos: para	 a	 leitura	 e	 escrita	 de	 dados e para	 obtenção	 de	 horas,
#minutos	e	segundos	a	partir	do	tempo	em	segundos.
#seg = float(input("Digite um número de segundos: "))
#aux = seg % 60
#min = (seg - aux) / 60
#hora = min / 60
#print("Corresponde a:\n", seg, "segundos\n", min, "minutos\n", hora, "horas")

#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.

#preco = float(input("Digite o preço da mercadoria: "))
#perc = float(input("Digite o percentual de desconto: "))
#valorDesc = preco * (1-(perc/100))
#valorNovo = preco - valorDesc
#print("Valor de Desconto: R$",valorNovo)
#print("Preço a pagar: R$",valorDesc)

#Escreva um programa que leia três números e que imprima o maior e o menor.
#a = int(input("Digite o valor de a: "))
#b = int(input("Digite o valor de b: "))
#c = int(input("Digite o valor de c: "))
#maior = a
#menor = a
#if b > c and b > a:
#  maior = b
#if c > a and c > b:
#  maior = c
#if b < c and b < a:
#  menor = b
#if c < b and c < a:
#  menor = c
#print("\nMaior:", maior,"\nMenor:",menor)

#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
#0,45 para viagens mais longas.
#dist = float(input("Digite a distâcia percorrida em KM: "))
#if dist <= 200:
#  preco = dist * 0.5
#else:
#  preco = dist * 0.45
#print("Valor da viagem: R$", preco)

#Modifique o programa para exibir os números de 1 a 100
#for i in range(1,101):
#  print(i, end=" ")

#Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
#O programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.
#i = 10
#while(i >= 0):
#  print(i, "!")
#  i -= 1
#print("Fogo!")

#Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário,
#mas, dessa vez, apenas os números ímpares
#num = int(input("Digite um número: "))
#for i in range(1, num):
#  if i % 2 == 1:
#    print(i, end=" ")

#Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até
#que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados,
#assim como a soma e a média aritmética
#num = 1
#soma = 0
#media = 0
#i = 0
#while num != 0:
#  num = int(input("Digite um valor (0 para): "))
#  i += 1
#  soma += num
#media = soma/(i-1)
#print("Qunatidade de números: ",i-1,"\nSoma: ",soma,"\nMédia Aritmética: ",media)


#Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se
#continua o mesmo caso seus dígitos sejam invertidos. Exemplos: 454, 10501
#s = input("Digite um número: ")
#i = 0
#f = len(s) - 1
#while f > i and s[i] == s[f]:
#  f -= 1
#  i += 1
#if s[i] == s[f]:
#  print("\nEste número é palíndromo!")
#else:
#  print("\nO número não é palíndromo!")


#Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
#l1 = input("Lista1: ")
#l2 = input("Lista2: ")
#l3 = l1 + " " + l2
#print("Lista3: ",l3)


#Escreva um programa que use inputs para solicitar ao
#usuário seu nome e, em seguida, faça um cumprimento.
#nome = input("Digite se nome: ")
#print("Olá,", nome,"!")


#Escreva um programa que solicite ao usuário as horas e o
#valor da taxa por horas para calcular o valor a ser pago por horas de serviço.
#horas = int(input("Digite a quantidade de horas: "))
#taxa = float(input("Digite o vaor da taxa por horas: "))
#print("Valor a ser pago: R$", horas*taxa)
#round para arrendondar os valores


#Escreva um programa que solicite ao usuário uma temperatura Celsius, converta para Fahrenheit, 
#e mostre a temperatura convertida.
#celsius = float(input("Digite a temperatura em ºC: "))
#print("Temperatura em Farenheit:", (celsius * 9/5) + 32, "ºF")


#Reescreva seu programa de pagamento, para pagar ao funcionário 1.5 vezes o valor da taxa horária 
#de pagamento pelo tempo trabalhado acima de 40 horas
#horas = int(input("Digite a quantidade de horas: "))
#taxa = float(input("Digite o vaor da taxa por horas: "))
#if horas > 40:
#  taxa *= 1.5
#  print("Valor a ser pago: R$", horas*taxa)
#else:
#  print("Valor a ser pago: R$", horas*taxa)


#Reescreva seu programa de pagamento utilizando try e except, de forma que o programa consiga 
#lidar com entradas não numéricas graciosamente, mostrando uma mensagem e saindo do programa. A
#seguir é mostrado duas execuções do programa.
#try:
#  horas = int(input("Digite a quantidade de horas: "))
#  taxa = float(input("Digite o valor da taxa por horas: "))
#except:
#  print("Digite números! Tente novamente!")
#
#if horas > 40:
#  print("Valor a ser pago: R$", horas*taxa*1.5)
#else:
#  print("Valor a ser pago: R$", horas*taxa)


#Escreva um programa que peça por uma pontuação entre 0.0 e 1.0. 
#Se a pontuação for fora do intervalo, mostre uma mensagem de erro. 
#Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota usando a seguinte tabela:
#Pontuação Nota
#>= 0.9       A
#>= 0.8       B
#>= 0.7       C
#>= 0.6       D
#< 0.6        F

#try:
#  pont = float(input("Digite a pontuação: "))
#except:
#  print("Pontuação Inválida!")
#if pont >= 0 and pont <= 1.0:
#  if pont >= 0.9:
#    print("Nota A")
#  elif pont >= 0.8:
#    print("Nota B")
#  elif pont >= 0.7:
#    print("Nota C")
#  elif pont >= 0.6:
#    print("Nota D")
#  elif pont < 0.6:
#    print("Nota F")
#else:
#  print("Pontuação Inválida!")


#Reescreva seu programa de cálculo de pagamento com um
#1.5 o valor de hora de trabalho por hora extra, crie uma função chamada
#calculoPagamento que aceita dois parâmetros(horas e TaxaHora).
#def calculoPagamento(taxa, horas):
#  if horas > 40:
#    print("Valor a ser pago: R$", horas*taxa*1.5)
#  else:
#    print("Valor a ser pago: R$", horas*taxa)    
#try:
#  horas = int(input("Digite a quantidade de horas: "))
#  taxa = float(input("Digite o valor da taxa por horas: "))
#except:
# print("Digite números! Tente novamente!")
#calculoPagamento(taxa,horas)


#Reescreva o programa de notas do capítulo anterior usando a função computarNotas 
#que recebe a pontuação como parâmetro e retorna a nota como uma string.

#try:
#  pont = float(input("Digite a pontuação: "))
#except:
#  print("Pontuação Inválida!")
#def computarNotas(pont):
#  if pont >= 0 and pont <= 1.0:
#    if pont >= 0.9:
#      print("Nota A")
#    elif pont >= 0.8:
#     print("Nota B")
#    elif pont >= 0.7:
#      print("Nota C")
#    elif pont >= 0.6:
#      print("Nota D")
#    elif pont < 0.6:
#      print("Nota F")
#  else:
#    print("Pontuação Inválida!")
#computarNotas(pont)


#import random
#lista = [0] * 10
#
#for i in range(0,10):
#  lista[i] = random.random()
#  print(lista[i])
# 
#print("Max = ",max(lista))
#print("Min = ",min(lista))


#Escreva um programa que lê repetitivamente números até que o usuário digite “pronto”. 
#Quando “pronto” for digitado, mostre a soma total, a quantidade e a média dos números digitados. 
#Se o usuário digitar qualquer coisa que não seja um número, detecte o erro usando
#o try e o except e mostre na tela uma mensagem de erro e pule para o próximo número.
#
#soma = 0
#i = 0
#
#try:
#  num = 1
#  while num != 0:
#    num = float(input("Digite um número: "))
#    soma += num
#    i += 1
#    
#  media = soma / (i-1) 
#  print("\nSoma =",soma,"\nMédia =",media,"\nQuantidade de números =",i-1)
#except:
#  print('\nErro! Digite um valor ou "0"!')
#  num = 1
#  while num != 0:
#    num = float(input("Digite um número: "))
#    soma += num
#    i += 1
#    
#  media = soma / (i-1) 
#  print("\nSoma =",soma,"\nMédia =",media,"\nQuantidade de números =",i-1)


#Escreva outro programa que pede por uma lista de números como mostrada acima e mostra, 
#no final, o máximo e o mínimo dos números ao invés da média.
#lista = [0]*10
#for i in range(0,10):
#  lista[i] = input("Valor: ")
#print("Máximo = ", max(lista),"\nMínimo = ", min(lista))


#def contagem():
#  palavra = input("Palavra: ")
#  letraA = input("Letra: ")
#  contagem = 0
#  for letra in palavra:
#    if letra == letraA:
#      contagem = contagem + 1  
#  print(contagem)
#
#contagem()

#help(str.startswith)

#data = 'Olá Mundo!'
#pesq = data.find('l')
#pesq1 = data.find("u", pesq)
#pesq2 = data[pesq:pesq1]
#print(pesq2)

#camelos = 42
#print('%d' % camelos) 


#Utilize o seguinte código em Python que guarda uma string:
#Use a função find e o fatiamento de strings para extrair a porção da string depois do sinal de dois pontos 
#e use a função float para converter a string extraída em um número de ponto flutuante.

#str = 'X-DSPAM-Confidence:0.8475' 

#pesq1 = str.find(':')
#pesq2 = str.find("5", pesq1)
#pesq3 = str[pesq1+1:pesq2]
#print(type(pesq3)) #str
#ext = float(pesq3)
#print(type(ext)) #float

#fhand = open('arq1.txt')

#ler = fhand.read()
#print(ler)

#line.startswith('From:') // Encontra as linhas que começam com "From:"
#line.rstrip()  // Tira a linha extra de cada print

#for line in fhand:
#  line  = line.rstrip()
#  if line.find('From') == -1: continue
#  print(line)

#count = 0
#for line in fhand:
#  count += 1
#print(count)

#fname = input("Digite o nome do arquivo: ")
#try:
#  fhand = open(fname)
#  ler = fhand.read()
#  print("\n")
#  print(ler)
#except:
#  print("Arquivo não existe:", fname)
#  exit()


#fout = open('arq1.txt', 'w')
#line1 = 'Olá Mundo!\n'
#fout.write(line1)
#fout.close()


#Escreva um programa que leia um arquivo e mostre o conteúdo deste (linha por linha),
#completamente em caixa alta. A execução do programa deverá ser a seguinte:
#fname = input("Digite o nome do arquivo: ")
#fhand = open(fname)
#ler = fhand.read()
#print(ler.upper())


#Escreva um programa que solicite um arquivo e então leia ele e procure por linhas 
#da forma: X-DSPAM-Confidence: 0.8475
#Quando encontrar uma linha que inicie com “X-DSPAM-Confidence:”
#separe a linha do texto para extrair o número de ponto flutuante que
#ela contém. Conte essas linhas e então compute o total de valores de
#Confiança de Spam nelas. Quando chegar no fim do arquivo, mostre a
#média de Confiança de Spam. 
#
#fname = input("Digite o nome do arquivo: ")
#
#try:
#  fhand = open(fname)
#  
#  count = 0
#  spam = 0
#  mediaSpam = 0
#
#  for line in fhand:
#   if line.startswith('X-DSPAM-Confidence:'):
#      count += 1
#      pesq1 = line.find(':')
#      pesq2 = line.find('\n',pesq1)
#      pesq3 = line[pesq1+1:pesq2]
#      spam += float(pesq3)
#      
#  mediaSpam = spam/count
#  print("\nMédia de Confiança de Spam: ",mediaSpam)
# 
#except:
#  print("Arquivo não encontrado: ", fname)


#Às vezes, quando os programadores estão entediados ou querem um pouco de diversão, 
#eles adicionam um Easter Egg inofensivo em seus programas. Modifique o programa que solicita 
#um arquivo ao usuário para que ele mostre uma mensagem engraçada quando o usuário deigitar no 
#nome do arquivo “na na boo boo”. O programa deve se comportar normalmente para todos os outros 
#arquivos que existem e que não existem.
#
#fname = input("Digite o nome do arquivo: ")
#
#try:
#  if fname == 'na na boo boo':
#    print('NA NA BOO BOO PRA VOCÊ TAMBÉM!')
#    
#  fhand = open(fname)
#  count = 0
#  
#  for line in fhand:
#    count += 1
#  print('Há',count,'linhas de assunto em',fname)
#
#except:
#  print('Arquivo não pôde ser aberto:',fname)


#Escreva uma função chamada corte que recebe uma lista e a modifica, removendo o primeiro e o último 
#elemento, e retorna None. Depois escreva uma função chamada meio que recebe uma lista e retorna uma nova 
#lista que contém todos, menos o primeiro e o último elemento.
#
#lista = []
#listaAux = []
#aux = 0
#
#def corte(lista):
#  del lista[0]
#  del lista[-1]
#listaAux = lista
#  print("Lista Corte: ",listaAux)
# 
#
#while aux != 'ok':
#  aux = input("Elemento da lista: ")
#  if aux == 'ok':
#    corte(lista)
#  else:
#    lista.append(aux)


#Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por linha. Para cada linha, 
#separe-a em uma lista de palavras usando a função split. Para cada palavra, cheque se esta palavra já 
#existe na lista. Caso não exista, adicione ela. Quando o programa terminar de verificar, ordene e imprima 
#estas palavras em ordem alfabética.
#
#fname = input("Nome do arquivo: ")
#
#listaPalavras = []
#palav = []
#
#try:
#  fhand = open(fname)
#  for line in fhand:
#    palavras = line.split()
#    for palavra in palavras:
#      if palavra in listaPalavras:
#        continue
#      listaPalavras.append(palavra)
#  listaPalavras.sort()  
#  print(listaPalavras)
#  
#except:
#  print("Arquivo não encontrado:",fname)


#Escreva um programa que leia uma caixa de email, e quando você encontrar uma linha que 
#comece com “De”, você vai separar a linha em palavras usando a função split. Nós estamos 
#interessados em quem envia a mensagem, que é a segunda palavra na linha que começa com From.
#De stephen.marquard@uct.ac.za Sáb Jan 5 09:14:16 2008
#Você vai analisar a linha que começa com From e irá pôr para imprimir na tela a segunda 
#palavra (para cada linha do tipo), depois o programa também deverá contar o número de linhas 
#que começam com “De” e imprimir em tela o valor final desse contador.
#
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


#Reescreva o programa que solicita o usuário uma lista de números e prints e imprime em tela 
#o maior número e o menor número quando o usuário digitar a palavra “feito”. Escreva um programa 
#para armazenar as entradas do usuário em uma lista e use as funções max() e min() para computar 
#o número máximo e o mínimo depois que o laço for completo.
#
#num = 0
#listaNum = []
#
#while num != 'feito':
#  num = input("Digite um número: ")
#  if num == 'feito':
#    print("Maior:",max(listaNum))
#    print("Menor:",min(listaNum))
#  else:
#    listaNum.append(num)


#Escreva um programa que leia as palavras em words.txt e as armazena como chaves em um dicionário. 
#Não importa quais são os valores. Então, você pode usar o operador in como uma maneira rápida de 
#verificar se uma string está no dicionário.
#
#fname = input("Arquivo: ")
#
#palavras = []
#fhand = open(fname)
#trad2port = dict()
#i = 0
#
#for lines in fhand:
#  palavras = lines.split()
#  for palavra in palavras:
#    #print("palavra =",palavra)
#    trad2port[palavra] = i
#    i += 1
#    #print('trad2port[',palavra,'] =',trad2port[palavra],"\n\n")
#
#aux = input("Encontre uma palavra: ")
#if aux in trad2port:
#print("True!\ntrad2port = ",trad2port[aux])



#Escreveremos um programa em Python para ler as linhas do arquivo, quebrá-las
#em uma lista de palavras e, então, contar a ocorrência de cada palavra presente no
#texto, usando um dicionário.
#try:
#  fname = input("Arquivo: ")
#except:
#  print("Arquivo não encontrado:",fname)  
#
#fhand = open(fname)
#d = dict()
#for linhas in fhand:
#  palavras = linhas.split()
#  for palavra in palavras:
#    if palavra not in d:
#      d[palavra] = d.get(palavra,0)
#    d[palavra] += 1
#print(d)
#
#lst = list(d.keys())
#print(lst,'\n')
#lst.sort()
#for key in lst:
#  print(key,d[key])


#Escreva um programa que categorize cada mensagem de e-mail de acordo com o dia em que a
#mensagem foi enviada. Para isso, procure por linhas que comecem com “From”, depois procure 
#pela terceira palavra e mantenha uma contagem de ocorrência para cada dia da semana. No final
#do programa, mostre em tela o conteúdo do seu dicionário (a ordem não interessa).
#Linha exemplo: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
#try:
#  fname = input("Arquivo: ")
#except:
#  print("Arquivo não encontrado:",fname)
#
#d = dict()
#fhand = open(fname)
#
#for linhas in fhand:
#  words = linhas.split()
#  for i in range(len(words)):
#    if words[i] == 'From':
#      d[words[2]] = d.get(words[2],0) + 1
#    continue
#print(d)


#Escreva um programa que leia um registro de mensagens, construa um histograma, utilizando um 
#dicionário, para contar quantas mensagens chegaram em cada endereço de email e mostre em tela o
#dicionário.
#
#try:
#  fname = input('Arquivo: ')
#except:
#  print("Arquivo não encontrado:",fname)
#
#d = dict()
#fhand = open(fname)
#
#for line in fhand:
#  words = line.split()
#  for i in range(len(words)):
#    if words[i] == 'From':
#      d[words[1]] = d.get(words[1],0) + 1
#    continue
#print(d,'\n')
#
#lst = list(d.keys())
#lst.sort()
#for key in lst:
#  print(key, d[key])


#Adicione linhas de código no programa abaixo para identificar quem possui mais mensagens no arquivo. 
#Após todo o dado ser lido e todo o dicionário ser criado, procure no dicionário, utilizando um laço máximo, 
#quem tem o maior número de mensagens e mostre em tela quantas mensagens essa pessoa tem.
#
#try:
#  fname = input('Arquivo: ')
#  fhand = open(fname)
#  d = dict()
#
#  for line in fhand:
#    words = line.split()
#    for i in range(len(words)):
#      if words[i] == 'From':
#        d[words[1]] = d.get(words[1],0) + 1
#      continue
#  #print(d,'\n')
#
#  max = 0
#  email = []
#
#  for k in d:
#    if d[k] > max:
#      email.append(k)
#      max = d[k]
#    continue
#  print(min(email),max)
#  
#except:
#  print("Arquivo não encontrado:",fname)


#Esse programa grava o domínio de email (ao invés do endereço) de onde a mensagem foi enviada ao 
#invés de quem o email veio. No final do programa, mostre em tela o conteúdo do seu dicionário.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
#fname = input('Arquivo: ')
#
#fhand = open(fname)
#d = dict()
#
#for line in fhand:
#  words = line.split()
#  for word in words:
#    if word == 'From':
#      aux = words[1]
#      email = aux[aux.find('@'):aux.find(" ")]
#      d[email] = d.get(email,0) + 1
#print(d)


#Leia e analise as linhas com “From” e retire os endereços dessas linhas. Conte o número de 
#mensagens de cada pessoa usando um dicionário. Depois de todos os dados serem lidos, mostre a 
#pessoa com mais envios criando uma lista de tuplas (contagem, email) do dicionário. Então, 
#ordene a lista em ordem reversa e mostre a pessoa na primeira posição.
#
#fname = input('Arquivo: ')
#
#fhand = open(fname)
#d = dict()
#
#for lines in fhand:
#  if lines.startswith('From'):
#    words = lines.split()
#    d[words[1]] = d.get(words[1],0) + 1
#  continue
#  
#email = list() 
#
#for key, val in list(d.items()):
#  email.append((val,key))
#      
#email.sort(reverse = True)
#
#for key, val in email[:1]:
#  print(val,int(key/2))


#Esse programa conta a distribuição de horas no dia para cada uma das mensagens. Você pode retirar 
#a hora da linha com “From” achando a string de horário e então separando ela em partes usando o
#caractere “:” (dois pontos). Uma vez acumuladas as contagens para cada hora, mostre os valores, 
#um por linha, ordenados por hora como segue abaixo: 
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
#fname = input('Arquivo: ')
#
#fhand = open(fname)
#d = dict()
#aux = list()
#
#for line in fhand:
#  words = line.split()
#  for word in words:
#    if word == 'From':
#      aux = words[5]
#     time = aux[:aux.find(':')]
#      d[time] = d.get(time,0) + 1
#    continue
#
#timeofday = list()
#
#for key, val in list(d.items()):
#  timeofday.append((key,val))
#
#timeofday.sort()
#
#print('\nHorários:\tQuantidade:')
#for key, val in timeofday[:]:
#  print(key,'\t\t\t\t',val)


#import re
#s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
#lst = re.findall('\S+@\S+', s)
#print(lst)

#Escreva um programa simples para simular a operação do comando grep em Unix. Peça ao usuário para entrar 
#com uma expressão regular e conte o número de linhas que se igualam à expressão digitada:
#$ python grep.py
#Digite uma expressão regular: ^Autor
#mbox.txt teve 1798 linhas que se igualam a ^Autor
#
#import re 
#
#fname = input("Arquivo: ")
#exp = input('Digite uma expressão regular: ')
#fhand = open(fname)
#count = 0
#
#for line in fhand:
#  line = line.rstrip()
#  x = re.findall(exp,line)
#  if len(x) > 0:
#    count += 1
#
#print(fname,'teve',count,'linhas que se igualam a',exp)

#---------------------HTTP/Python-------------------------------------#
#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/mbox.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)
#while True:
#  data = mysock.recv(512)
#  if len(data) < 1:
#    break
#  print(data.decode(),end='')
#mysock.close()


#--------------------------------UrlLib----------------------------------#
#import urllib.request
#fname = input("Site: ")
#fhand = urllib.request.urlopen(fname)
#for line in fhand:
#  print(line.decode()) #.line.decode().strip()


#-------------------------ANÁLISE DE HTML USANDO BEAUTIFULSOUP----------------#
#import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
#import ssl
#
# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE
#
#url = input('Enter - ')
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
#  print(tag.get('href', None))


#Altere o programa de soquete socket1.py pR pedir ao usuário a URL para que então possa ler qualquer 
#página da web.Você pode usar split('/') para quebrar a URL em suas componentes para que então possa 
#extrair o nome do hospedeiro para que o soquete connect chame. Adicione tratamento de erro usando try 
#e except para lidar com a condição do usuário digitar uma URL formatada incorretamente ou uma não 
#existente
#
#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#try:
#  site = input('Site: ')
#  aux = site[site.find('h'):site.find(':')]
#  if aux == 'http' or aux == 'https':
#    host = site[site.find('/')+2:site.find('/',site.find('/')+4)]
#    mysock.connect((host, 80))
#
#    url = 'GET '+site+' HTTP/1.0\r\n\r\n'
#    cmd = url.encode()
#    mysock.send(cmd)
#
#  while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#      break  
#    print(data.decode(),end='')
#  mysock.close()
#
#except:
#  print('URL formatada incorretamente!')


#Altere seu programa de soquete para que ele conte o número de caracteres que recebeu e pare de 
#mostrar qualquer texto depois que mostrar 3000 caracteres. O programa deve recuperar o documento 
#inteiro e contar o número total de caracteres e mostrar o resultado da contagem no final do documento.
#http://data.pr4e.org/romeo.txt
#
#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#j = 0
#try:
#  site = input('Site: ')
#  aux = site[site.find('h'):site.find(':')]
#  if aux == 'http' or aux == 'https':
#    j += 1
#    host = site[site.find('/')+2:site.find('/',site.find('/')+4)]
#    mysock.connect((host, 80))
#
#    url = 'GET '+site+' HTTP/1.0\r\n\r\n'
#    cmd = url.encode()
#    mysock.send(cmd)
#  
#  d = dict()
#  c = dict()
#  i = 0
#  k = 0
#  sum = 0
#  
#  while True:
#    data = mysock.recv(3000)
#    words = data.decode().split()
#        
#    if sum >= 3000:
#      break
#    if len(data) < 1:
#      break  
#    for word in words:
#      if sum >= 3000:
#        break
#      for char in word:
#         if sum >= 3000:
#           break
#          d[char] = d.get(char,0) + 1
#          i += 1
#      print(data.decode(),end='')
#
#    for word in words:
#      k += 1
#      if word == 'Content-Type:':
#        aux = words[k+1:]
#        for elem in aux:
#          for elem1 in elem:
#            c[elem1] = c.get(elem1,0) + 1
#            sum += c[elem1]
#            
#    #print('\n\nQuantidade de caracteres de assunto:',sum-i)
#    print('\nQuantidade de caracteres total:',sum)
#    mysock.close()
#
#except:
#  if j == 0:
#    print('\nURL formatada incorretamente!')


#Use UrlLib para replicar o exercício anterior recuperando um documento de uma URL
#import urllib.request
#fname = input('Site: ')
#fhand = urllib.request.urlopen(fname) 
#for line in fhand:
#  print(line.decode().strip())


#Use UrlLib para mostrar até 3000 caracteres em um documento de uma URL
#http://data.pr4e.org/mbox-short.txt
#http://data.pr4e.org/romeo.txt
#
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


#Altere o programa urllinks.py para extrair e contar as tags de parágrafos (p) do 
#documento de HTML recuperado e mostrar a contagem dos parágrafos como uma saída do 
#seu programa.Não mostre o conteúdo, apenas conte-os. Teste seu programa em várias 
#páginas da web pequenas e também em algumas maiores.
#
#import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
#import ssl
#
# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE
#
#url = input('Enter - ')
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#
#count = 0
# Retrieve all of the anchor tags
#tags = soup('p')
#for tag in tags:
#  count += 1
#print('Quantidade de parágrafos na página:',count)


#Criar senhas aleaoerias em Python
#import random
#
#lower = 'abcdefghijklmopqrstuvwxyz'
#upper = lower.upper()
#symbols = '(){}[]_-=+*&$#@!<>:;'
#numbers = '0123456789'
#
#all = lower + upper + symbols + numbers
#tam = 16
#
#password = ''.join(random.sample(all,tam))
#print('Senha:',password)


#Altere um dos arquivos geojson.py ou geoxml.py para que a saída do programa mostre os dois caracteres 
#referentes ao código do país dos dados recebidos. Adicione teste(s) de erro para que o programa não retorne 
#um traceback em caso de não haver código de país. Uma vez que o programa esteja funcionando, procure por 
#“Atlantic Ocean” e confirme que o programa pode lidar com localizações que não pertencem a nenhum país.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    try: 
      tree = ET.fromstring(data)
      #status = tree.findall('status').text
      
      #if status == 'OK':
      print(data.decode())
  
      results = tree.findall('result')
      lat = results[0].find('geometry').find('location').find('lat').text
      lng = results[0].find('geometry').find('location').find('lng').text
      location = results[0].find('formatted_address').text

        #type = results[0].find('type').text
        #if type ==;
        
      print('lat', lat, 'lng', lng)
      print(location)
      #break
    except: 
      print('==== Failure To Retrieve ====')