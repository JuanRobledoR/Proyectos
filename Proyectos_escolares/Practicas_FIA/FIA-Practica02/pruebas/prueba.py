def entrada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 2:
                return (i, j)

def ewewe(matriz, matrizfeka, coordenadasde5):
    fila, columna = entrada(matriz)
    while matriz[fila][columna] != 3:
        if fila > 0 and matriz[fila-1][columna] == 1:
            matrizfeka[fila][columna] = 4
            if ((columna < len(matriz[0])-1 and matriz[fila][columna+1] == 1) or 
                (columna > 0 and matriz[fila][columna-1] == 1) or 
                (fila < len(matriz)-1 and matriz[fila+1][columna] == 1)):
                matrizfeka[fila][columna] = 5
                coordenadasde5.append((fila, columna))
            fila -= 1
        elif columna < len(matriz[0])-1 and matriz[fila][columna+1] == 1:
            matrizfeka[fila][columna] = 4
            if ((fila > 0 and matriz[fila-1][columna] == 1) or 
                (columna > 0 and matriz[fila][columna-1] == 1) or 
                (fila < len(matriz)-1 and matriz[fila+1][columna] == 1)):
                matrizfeka[fila][columna] = 5
                coordenadasde5.append((fila, columna))
            columna += 1
        elif columna > 0 and matriz[fila][columna-1] == 1:
            matrizfeka[fila][columna] = 4
            if ((fila > 0 and matriz[fila-1][columna] == 1) or 
                (columna < len(matriz[0])-1 and matriz[fila][columna+1] == 1) or 
                (fila < len(matriz)-1 and matriz[fila+1][columna] == 1)):
                matrizfeka[fila][columna] = 5
                coordenadasde5.append((fila, columna))
            columna -= 1
        elif fila < len(matriz)-1 and matriz[fila+1][columna] == 1:
            matrizfeka[fila][columna] = 4
            if ((fila > 0 and matriz[fila-1][columna] == 1) or 
                (columna < len(matriz[0])-1 and matriz[fila][columna+1] == 1) or 
                (columna > 0 and matriz[fila][columna-1] == 1)):
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
        
        original_fila, original_columna = fila, columna
        
        # Explorar en una dirección (por ejemplo, arriba)
        current_fila, current_columna = original_fila, original_columna
        while current_fila > 0 and matriz[current_fila-1][current_columna] == 1 and matrizfeka[current_fila-1][current_columna] not in [4, 5]:
            current_fila -= 1
            matrizfeka[current_fila][current_columna] = 4

        # Explorar en otra dirección (por ejemplo, abajo)
        current_fila, current_columna = original_fila, original_columna
        while current_fila < len(matriz)-1 and matriz[current_fila+1][current_columna] == 1 and matrizfeka[current_fila+1][current_columna] not in [4, 5]:
            current_fila += 1
            matrizfeka[current_fila][current_columna] = 4

        # Explorar a la izquierda
        current_fila, current_columna = original_fila, original_columna
        while current_columna > 0 and matriz[current_fila][current_columna-1] == 1 and matrizfeka[current_fila][current_columna-1] not in [4, 5]:
            current_columna -= 1
            matrizfeka[current_fila][current_columna] = 4

        # Explorar a la derecha
        current_fila, current_columna = original_fila, original_columna
        while current_columna < len(matriz[0])-1 and matriz[current_fila][current_columna+1] == 1 and matrizfeka[current_fila][current_columna+1] not in [4, 5]:
            current_columna += 1
            matrizfeka[current_fila][current_columna] = 4


def main():
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

    ewewe(matriz, matrizfeka, coordenadasde5)
    iwiwi(matriz, matrizfeka, coordenadasde5)

    for row in matrizfeka:
        print(row)

if __name__ == "__main__":
    main()