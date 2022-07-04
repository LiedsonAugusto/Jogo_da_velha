import random

def printJogo(matriz):
    print("")
    for i in range(len(matriz)):
        for c in range(len(matriz)):
            if c + 1 == len(matriz):
                print(matriz[i][c])
            else:
                print(matriz[i][c], end='   |')
        if i + 1 != len(matriz):
            print("----|----|----")
    print("")

def decisoesJogo(matriz, linha, coluna):
    print("")
    matriz[linha-1][coluna-1] = 'X'
    linhaPC = random.randint(0, 2)
    colunaPC = random.randint(0, 2)
    while 'X' in matriz[linhaPC][colunaPC] or 'O' in matriz[linhaPC][colunaPC]:
        linhaPC = random.randint(0, 2)
        colunaPC = random.randint(0, 2)
    matriz[linhaPC][colunaPC] = 'O'
    for i in range(len(matriz)):
        for c in range(len(matriz)):
            if c + 1 == len(matriz):
                print(matriz[i][c])
            else:
                print(matriz[i][c], end='   | ')
        if i + 1 != len(matriz):
            print("----|-----|----")
    print("")

def verificadorLinha():
    linha = int(input('Linha (1 a 3): '))
    while linha < 1 or linha > 3:
        linha = int(input('Por favor, digite entre 1 e 3: '))
    return linha

def verificadorColuna():
    coluna = int(input('Coluna (1 a 3): '))
    while coluna < 1 or coluna > 3:
        coluna = int(input('Por favor, digite entre 1 e 3: '))
    return coluna

def condicaoDeVitoria(matriz):
    if matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X' or matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X' or matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X' or matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X' or matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X' or matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X' or matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X' or matriz[0][2] == 'X' and matriz[1][1] == 'X' and matriz[2][0] == 'X':
        return 1
    else:
        return 0

def condicaoDeDerrota(matriz):
    if matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O' or matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O' or matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O' or matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O' or matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O' or matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'X' or matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O' or matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O':
        return 1
    else:
        return 0