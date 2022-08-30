


inicial = [0, 2, 3, 1, 6, 4, 8, 7 ,5]
final = [1, 2, 3, 8, 0, 4, 7, 6, 5]
L = []
#Proximidade
pontos = 0
melhor = []
#Variavel que ira se deslocar
variavelPadrao = 0
#Posicao
position = 0
#Variavel para deslocar
backup = 0

no = []
actual = 0
p = 0
movimentos = []
up = True
down = True
left = True
right = True

while True:


    #UP
    if inicial.index(variavelPadrao) - 3 >= 0 and inicial.index(variavelPadrao) - 3 <= 8 and up == True:
        position = inicial.index(variavelPadrao) - 3
        data = inicial.copy()
        backup = position
        data[backup] = 0
        data[inicial.index(variavelPadrao)] = inicial[position]
        L.append(data)
        pontos = 0
        for i in range(9):
            if data[i] == final[i]:
                pontos += 1
        melhor.append(pontos)

    else:
        L.append(-1)
        melhor.append(-1)
        
    #DOWN 
    if inicial.index(variavelPadrao) + 3 >= 0 and inicial.index(variavelPadrao) + 3 <= 8 and down == True:
        position = inicial.index(variavelPadrao) + 3
        data = inicial.copy()
        backup = position
        data[backup] = 0
        data[inicial.index(variavelPadrao)] = inicial[position]
        L.append(data)
        pontos = 0
        for i in range(9):
            if data[i] == final[i]:
                pontos += 1
        melhor.append(pontos)
    else:
        L.append(-1)
        melhor.append(-1)
    #LEFT
    if inicial.index(variavelPadrao) - 1 >= 0 and inicial.index(variavelPadrao) - 1 <= 8 and inicial.index(variavelPadrao) - 1 != 2  and inicial.index(variavelPadrao) - 1 != 5 and left == True:
        position = inicial.index(variavelPadrao) - 1
        data = inicial.copy()
        backup = position
        data[backup] = 0
        data[inicial.index(variavelPadrao)] = inicial[position]
        L.append(data)
        pontos = 0
        for i in range(9):
            if data[i] == final[i]:
                pontos += 1
        melhor.append(pontos)
    else:
        L.append(-1)
        melhor.append(-1)
    #RIGHT
    if inicial.index(variavelPadrao) + 1 >= 0 and inicial.index(variavelPadrao) + 1 <= 8 and inicial.index(variavelPadrao) + 1 != 3 and inicial.index(variavelPadrao) + 1 != 6 and right == True:
        position = inicial.index(variavelPadrao) + 1
        data = inicial.copy()
        backup = position
        data[backup] = 0
        data[inicial.index(variavelPadrao)] = inicial[position]
        L.append(data)
        pontos = 0
        for i in range(9):
            if data[i] == final[i]:
                pontos += 1
        melhor.append(pontos)
    else:
        L.append(-1)
        melhor.append(-1)

    up = True
    down = True
    left = True
    right = True
    print("L:",L)
    noPosition = melhor.index(max(melhor))
    no.append(L[noPosition])

    if noPosition == 0:
        movimentos.append("U")
        down = False
    if noPosition == 1:
        movimentos.append("D")
        up = False
    if noPosition == 2:
        movimentos.append("L")
        right = False
    if noPosition == 3:
        movimentos.append("R")
        left = False

    inicial = no[p]
    p += 1
    L.clear()
    melhor.clear()
    print(no)
    print("-=-=-=-=-=-=-=")
    if inicial == final:
        break

print(no.pop())
