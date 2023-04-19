#Código de Define posições------------------------------------------------------------------------------------


def define_posicoes(linha, coluna, orientacao, tamanho):
    lista=[]
    for i in range(tamanho):
        if orientacao=='vertical':
            coordenadas=[linha+i,coluna]
            lista.append(coordenadas)
        if orientacao=='horizontal':
            coordenadas=[linha, coluna+i]
            lista.append(coordenadas)
    return lista
        

#variáveis--------------------------------------------------------------------------------------------------


linha=2
coluna=4
orientacao='vertical'
tamanho=3
dicfrota={}
nomenavio='porta-aviões'

tabuleiro=[
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]
linha_jogador=1
coluna_jogador=1

#Código de Preenche frota--------------------------------------------------------------------------------------



def preenche_frota(dicfrota, nomenavio, linha, coluna, orientacao, tamanho):

    if nomenavio in dicfrota:

        x=dicfrota[nomenavio]
        x.append(define_posicoes(linha, coluna, orientacao, tamanho))

    if nomenavio not in dicfrota:

        dicfrota[nomenavio]=[]
        x=dicfrota[nomenavio]
        x.append(define_posicoes(linha, coluna, orientacao, tamanho))

    return dicfrota


print(preenche_frota(dicfrota, nomenavio, linha, coluna, orientacao, tamanho))


#Código Faz jogada-----------------------------------------------------------------------------------------------

def faz_jogada(tabuleiro, linha_jogador, coluna_jogador):
    if tabuleiro[linha_jogador][coluna_jogador]==1:
        tabuleiro[linha_jogador][coluna_jogador]='X'
    if tabuleiro[linha_jogador][coluna_jogador]==0:
        tabuleiro[linha_jogador][coluna_jogador]='-'
    
    return tabuleiro



tabuleiro=[
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]