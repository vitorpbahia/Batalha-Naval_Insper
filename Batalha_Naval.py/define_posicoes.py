def define_posicoes(linha, coluna, orientacao, tamanho):
    lista=[]
    for i in range(tamanho):
        if orientacao=='vertical':
            x=[linha+i,coluna]
            lista.append(x)
        if orientacao=='horizontal':
            x=[linha, coluna+i]
            lista.append(x)
    return lista
        




x= define_posicoes(2,4,'vertical', 3)
print(x)