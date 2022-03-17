import sys
print(" Seja bem vindo ao jogo da velha!")
regras = " Você é 0 e o computador é 1. Vá adicionando na matriz e tente formar uma linha vertical ou horizontal. Boa sorte! "
print(regras)

primeira_rodada = 0
segunda_rodada = 0
terceira_rodada = 0 

matriz = [ [], [], [] ], [ [], [], [] ], [ [], [], [] ]
print(matriz)
#primeira sequência
primeira_rodada = int(input('Digite linha e coluna = '))
if primeira_rodada == 11:
   matriz[0][0].append([0])
   matriz[1][1].append([1])
   print(matriz)
   segunda_rodada = int(input('Digite linha e coluna = '))
   if segunda_rodada == 12:
      matriz[0][1].append([0])
      matriz[0][2].append([1])
      print(matriz)
      terceira_rodada = int(input('Digite linha e coluna = '))
      if terceira_rodada != 21:
        matriz[2][0].append([1])
        print(matriz)
        print('Computador venceu') 
      elif terceira_rodada == 21:
        matriz[2][0].append([0])
        matriz[1][0].append([1])
        print(matriz)
        print('99% chance de empate')
        sys.exit()
#segunda sequência
if primeira_rodada == 11:
    matriz[0][0].append([0])
    matriz[1][1].append([1])
    print(matriz)
    segunda_rodada = int(input('Digite linha e coluna = '))
    if segunda_rodada == 13:
        matriz[0][2].append([0])
        matriz[0][1].append([1])
        print(matriz)
        terceira_rodada = int(input('Digite linha e coluna = '))
        if terceira_rodada != 21:
            matriz[2][0].append([1])
            print(matriz)
            print('Computador venceu')
        elif terceira_rodada == 21:
            matriz[2][0].append([0])
            matriz[2][1].append([1])
            print(matriz)
            print('99% de chance de empate')
elif primeira_rodada == 12:
   matriz[0][1].append([0])
   matriz[1][1].append([1])
   print(matriz) 
elif primeira_rodada == 13:
   matriz[0][3].append([0])
   matriz[0][0].append([1])
   print(matriz) 
elif primeira_rodada == 21:
   matriz[0][1].append([0])
   matriz[1][1].append([1])
   print(matriz) 
elif primeira_rodada == 22:
   matriz[1][1].append([0])
   matriz[0][2].append([1])
   print(matriz)
else:
    print("sem valor correspondente")
#elif primeira rodada = 23
#elif primeira rodada = 31
#elif primeira rodada = 32
#elif primeira rodada = 33