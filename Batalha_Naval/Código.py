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
coluna=9
orientacao='horizontal'
tamanho=2
dicfrotas={}
nomenavio='porta-aviões'

tabuleiro_jogo=[
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



#Código Faz jogada-----------------------------------------------------------------------------------------------

def faz_jogada(tabuleiro_jogo, linha_jogador, coluna_jogador):
    if tabuleiro_jogo[linha_jogador][coluna_jogador]==1:
        tabuleiro_jogo[linha_jogador][coluna_jogador]='X'
    if tabuleiro_jogo[linha_jogador][coluna_jogador]==0:
        tabuleiro_jogo[linha_jogador][coluna_jogador]='-'
    
    return tabuleiro_jogo




#Código Posiciona Frota-----------------------------------------------------------------------------------------
def posiciona_frota(dicfrotas):
    tabuleiro_inicial=[
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for navio in dicfrotas:
        coordenadas=dicfrotas[navio]

        for i in range(len(coordenadas)):
            coordenadas1=coordenadas[i]

            for n in range(len(coordenadas1)):
                coordenadas2=coordenadas1[n]
                tabuleiro_inicial[coordenadas2[0]][coordenadas2[1]]=1
    
    return tabuleiro_inicial
    
#Código da função Afundados---------------------------------------------------------------------------------------

def afundados(dicfrotas, tabuleiro_jogo):
    navios_afundados=0
    for navio in dicfrotas:
        coordenada=dicfrotas[navio]
        for i in range(len(coordenada)):
            coordenada1=coordenada[i]
            c=1
            for n in range(len(coordenada1)):
                coordenada2=coordenada1[n]
                
                

                for j in range(len(coordenada2)):
                    if tabuleiro_jogo[coordenada2[0]][coordenada2[1]]!='X':
                        c=0
                
                if n==len(coordenada1)-1 and c==1:
                    navios_afundados+=1
        return navios_afundados        
                    
#Código função posição válida----------------------------------------------------------------------------------------------
def posicao_valida(dicfrotas,linha,coluna,orientacao,tamanho):

    v=True
    x=define_posicoes(linha, coluna, orientacao, tamanho)
    for navios in dicfrotas:
            coordenada=dicfrotas[navios]
            for j in range(len(coordenada)):
                coordenada1=coordenada[j]

                for n in range(len(coordenada1)):

                    
                    for i in range(len(x)):
                        if x[i] in coordenada1:
                            v=False
    for i in range(len(x)):
        c=x[i]
        if c[0]>9 or c[0]<0:
            v=False
        if c[1]>9 or c[1]<0:
            v=False
    return v
