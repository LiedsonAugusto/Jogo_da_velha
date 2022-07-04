import funcoes as fj
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print("------------------------")
print("    * JOGO DA VELHA *    ")
print("------------------------")

fj.printJogo(matriz)

while True:
    if (fj.condicaoDeVitoria(matriz)):
        print('PARABÉNS, VOCÊ VENCEU!!')
        break
    elif (fj.condicaoDeDerrota(matriz)):
        print('QUE PENA, VOCÊ PERDEU :(')
        break
    else:
        linha = fj.verificadorLinha()
        coluna = fj.verificadorColuna()
        while 'X' in matriz[linha-1][coluna-1] or 'O' in matriz[linha-1][coluna-1]:
            print('Por favor, poupe seu tempo e digite em um local onde não tenha nada')
            linha = fj.verificadorLinha()
            coluna = fj.verificadorColuna()
        
        fj.decisoesJogo(matriz, linha, coluna)
