matriz = [
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,1,1,1,1,3],
    [0,1,0,1,0,0,1,0,1,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,1,0,0,0,1,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,1,1,1,0,0,0,0,0,0],
    [2,1,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
]

matrizfeka = [row[:] for row in matriz]

coordenadasde5 = []

def entrada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 2:
                return (i, j)

def ewewe(matriz, matrizfeka, coordenadasde5):
    fila, columna = entrada(matriz)
    while matriz[fila][columna] != 3:
        if matriz[fila-1][columna] == 1:
            matrizfeka[fila][columna] = 4
            if ((matriz[fila][columna+1] == 1) or (matriz[fila][columna-1] == 1) or (matriz[fila+1][columna] == 1)):
                matrizfeka[fila][columna] = 5
                coordenadasde5.append((fila, columna))
            fila -= 1
        elif matriz[fila][columna+1] == 1:
            matrizfeka[fila][columna] = 4
            if ((matriz[fila-1][columna] == 1) or (matriz[fila][columna-1] == 1) or (matriz[fila+1][columna] == 1)):
                matrizfeka[fila][columna] = 5
                coordenadasde5.append((fila, columna))
            columna += 1
        elif matriz[fila][columna-1] == 1:
            matrizfeka[fila][columna] = 4
            if ((matriz[fila-1][columna] == 1) or (matriz[fila][columna+1] == 1) or (matriz[fila+1][columna] == 1)):
                matrizfeka[fila][columna] = 5
                coordenadasde5.append((fila, columna))
            columna -= 1
        elif matriz[fila+1][columna] == 1:
            matrizfeka[fila][columna] = 4
            if ((matriz[fila-1][columna] == 1) or (matriz[fila][columna+1] == 1) or (matriz[fila][columna-1] == 1)):
                matrizfeka[fila][columna] = 5
                coordenadasde5.append((fila, columna))
            fila += 1
        else:
            break
    matrizfeka[fila][columna] = 4

def iwiwi(matriz, matrizfeka, coordenadasde5):
    while coordenadasde5:
        fila, columna = coordenadasde5.pop(0)
        matrizfeka[fila][columna] = 4
        while True:
            opciones = []
            if matriz[fila-1][columna] == 1 and matrizfeka[fila-1][columna] not in [4,5]:
                opciones.append((fila-1, columna))
            if matriz[fila+1][columna] == 1 and matrizfeka[fila+1][columna] not in [4,5]:
                opciones.append((fila+1, columna))
            if matriz[fila][columna-1] == 1 and matrizfeka[fila][columna-1] not in [4,5]:
                opciones.append((fila, columna-1))
            if matriz[fila][columna+1] == 1 and matrizfeka[fila][columna+1] not in [4,5]:
                opciones.append((fila, columna+1))
            if not opciones:
                break
            fila, columna = opciones[0]
            matrizfeka[fila][columna] = 4

ewewe(matriz, matrizfeka, coordenadasde5)
iwiwi(matriz, matrizfeka, coordenadasde5)

if __name__ == "__main__":
    main()