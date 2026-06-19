#Nesse projeto eu irei desenvolver o jogo "Campo minado" que rodará no terminal.
''' Como funciona: Será apresentado um campo de acordo com as medidas que o jogador informar e com a quantidade de bombas que ele quiser,
    esse campo não apresentará as bombas e nem os espaços limpos, ele sera ocultado por quadrados, o campo com as informações de localização
    das bombas só será informado se o jogador usar a trapaça.
    
    Regras: a linha e a coluna serão dadas em uma única linha e irá representar as coordenadas escolhidas. Se for uma bomba, o jogador perde, se
    não for, será revelado a qauntidade bombas nas 8 posições adjacentes, se o quantidade for nula, as 8 posições serão reveladas. Caso algumas das
    posições também tiver 8 posições livres ao seu redor, essas também serão reveladas, e assim sucessivamente.
    O jogador vence se restar apenas bombas e todas as posições vazias tiverem sidas escolhidas.'''


import random  #Importar random para fazer a escolha das bombas
def geracao_campo(numero):#primeira função feita, ela irá gerar o campo que o jogador irá ver.
    matriz_visivel=[] #chamaremos de matriz visível 
    for linhas in range(numero):
        matriz_visivel.append(['▪'] * numero ) #as posições serão mostradas com um quadrado 
        
    return matriz_visivel #retornamos a matriz 

def invisivel(numero, bombas):#segunda função será a parte que o jogador não irá ver, onde ficará a informação das bombas

    matriz_invisivel = [] #chamaremos de matriz invisivel 
    for i in range(numero):
        matriz_invisivel.append(['□'] * numero)
    
    coordenadas = [(i,j) for i in range(numero) for j in range(numero)] #criamos outra matriz para servir de base
    coordenadas_escolhidas = random.sample(coordenadas, bombas) #escolhemos onde será as coordenadas

    for i, j in coordenadas_escolhidas: #onde foi as coordenadas na matriz de base, será na matriz invisivel
        matriz_invisivel[i][j] = '●' #essa bolinha representa a bomba
        
    return matriz_invisivel #retornamos a matriz
        
def exibicao_campo(matriz_visivel, matriz_invisivel, numero):#terceira função irá exibir o campo com a numeração das linhas e colunas
    colunas = [x for x in range(1, numero+1)] #criamos a numeração das colunas
    for coluna in colunas: #colocamos os numeros
        if coluna == numero:
            print(coluna, end='\n')
        elif coluna == 1:
            print('#', end= ' ')
            print(coluna, end=' ')
        else:
            print(coluna, end=' ')
            
    linha = 1 #fazemos o mesmo com as linhas
    for linhas in range(len(matriz_visivel)):
        print(linha, end= ' ')
        for letras in range(len(matriz_visivel[linhas])):
            if letras == numero-1:
                print(matriz_visivel[linhas][letras], end='\n')
            else:
                print(matriz_visivel[linhas][letras], end=' ')
        linha += 1

def bombas_adjacentes(matriz_invisivel, coordenada_x, coordenada_y, numero):#quarta função irá conferir a quantidade de bombas adjacentes
    contador_bomba=0 
    ''''dado que as 8 posições adjacentes podem varias de 1 colunas, 1 linha ou estar na mesma coluna ou na mesma linha,
        fazemos duas repetições com numeros de -1 a 1'''
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i==0 and j==0:
                continue
            analise_x= coordenada_x + i
            analise_y= coordenada_y + j

            if 0<=analise_x<numero and 0<=analise_y<numero:
                if matriz_invisivel[analise_x][analise_y]== '●': #se for uma bomba, adicionamos ao contador de bomba
                    contador_bomba+=1
    
    return contador_bomba #retornamos o contador de bombas

def bombas_cascatas(matriz_invisivel, matriz_visivel, coordenada_x, coordenada_y, numero):#quinta função fará o efeito cascata das bombas adjacentes
    cx= coordenada_x
    cy= coordenada_y
    
    total_bombas= bombas_adjacentes(matriz_invisivel, coordenada_x, coordenada_y, numero) #vemos o número de bombas
    
    if total_bombas>0:
        matriz_visivel[cx][cy]= str(total_bombas) #se for maior que 0, apenas substituimos 
    
    else: #se não houver bombas, começamos a checagem 
        lista_analise= [(cx, cy)]    #fazemos uma lista de coordenadas a serem analisadas, começando com a que a gente ja conferiu   
        while len(lista_analise)>0: #repetitivo, porém necessário 
            coordenadas_analisadas= lista_analise.pop(0) #retiramos da lista com o pop que também retorna o item retirado, permitindo analisar
            analise_x= coordenadas_analisadas[0]
            analise_y= coordenadas_analisadas[1]
            
            if matriz_visivel[analise_x][analise_y]!='▪': #se essa coordenada já tiver sido analisada, pulamos 
                continue
            total_bombas= bombas_adjacentes(matriz_invisivel, analise_x, analise_y, numero)
            
            if total_bombas>0:
                matriz_visivel[analise_x][analise_y]= str(total_bombas) #repetimos o processo
            else:
                matriz_visivel[analise_x][analise_y]= '0' #se for 0, colocamos 0 e começamos a conferir as posições adjacentes também
                
                for i in [-1,0,1]: #mesma lógica
                    for j in [-1,0,1]:
                        if i==0 and j==0:
                            continue
                        nx= analise_x + i
                        ny= analise_y + j
                        
                        if 0<=nx<numero and 0<=ny<numero:
                            lista_analise.append([nx, ny]) #adicionamos as coordenadas na lista para serem analisadas 
    
    return matriz_visivel  #retornamos a matroz visivel atualizada           

def trapaca(matriz_visivel, matriz_invisivel, numero):#sexta função será a trapaça que mencionamos 
    #faremos a mesma coisa do jogo normal, so que adicionando não só a numeração como também a própria matriz invisível ao lado (também numerada)
    colunas = [x for x in range(1, numero+1)]
    for coluna in colunas:
        if coluna == numero:
            print(coluna, end='       ')
            for coluna in colunas:
                if coluna==numero:
                    print(coluna, end='\n')
                elif coluna==1:
                    print('#', end=' ')
                    print(coluna, end=' ') 
                else:
                    print(coluna, end= ' ')
        elif coluna == 1:
            print('#', end= ' ')
            print(coluna, end=' ')
        else:
            print(coluna, end=' ')
            
    linha = 1
    for linhas in range(len(matriz_visivel)):
        print(linha, end= ' ')
        for letras in range(len(matriz_visivel[linhas])):
            if letras == numero-1:
                print(matriz_visivel[linhas][letras], end='       ')
            else:
                print(matriz_visivel[linhas][letras], end=' ')
        
        print(linha, end= ' ')
        for letras in range(len(matriz_invisivel[linhas])):
            if letras== numero-1:
                print(matriz_invisivel[linhas][letras], end='\n')
            else:
                print(matriz_invisivel[linhas][letras], end=' ')
             
        linha+=1

def jogo(geracao_campo, invisivel, exibicao_campo, trapaca, bombas_adjacentes, bombas_cascatas):#sétima função rodará todo o jogo e as outras funções
    #aqui pedimos as informações ao jogador
    print('           Campo Minado          ')
    nome= input('Seu nome:').title()
    numero = int(input("Medida do campo:"))
    bombas = int(input(f"N° de bombas (Máx:{int(0.5*(numero**2))}):"))

    #vamos chamar as funções de campo visivel e invisivel fora da repetição, já que elas serão constantememte atualizadas
    #colocamos em variáveis  
    dados_campo= invisivel(numero, bombas)
    dados_visuais= geracao_campo(numero) 

    while True: #repetição até acabar a partida 
        
        if nome== 'Dev': #se o nome do jogador for dev, ele receberá a trapaça
            trapaca(dados_visuais, dados_campo, numero)
        else:
            exibicao_campo(dados_visuais, dados_campo, numero) #se não, apenas o campo normal
        try: #tratamento de dados para caso sejam colocados valores errados 
            linha_coluna= input('L C:').split()
            coordenada_x= int(linha_coluna[0])-1
            coordenada_y= int(linha_coluna[1])-1
        except (ValueError, IndexError):
            print('Digite números Válidos.')
            continue
        if not (0<=coordenada_x<numero and 0<=coordenada_y<numero): #se estiver fora do mapa, não será contabilizado 
            print('Coordenadas fora do mapa.')
            continue 

        if dados_campo[coordenada_x][coordenada_y]== '●': #se uma bomba for escolhida, o jogo acaba 
            print('Você Perdeu!')
            break
        else:
            bombas_cascatas(dados_campo, dados_visuais, coordenada_x, coordenada_y, numero) #se não, chamamos a bomba cascata que por si só já chamará a bombas adjacentes
                
            for linha in dados_visuais:
                quadrados= linha.count('▪') #contamos quantos quadrados tem no tabuleiro
            
            if quadrados==bombas:#se esse numero for igual ao numero de bombas, so restaram bombas, então o jogador venceu
                print('Você venceu!')
                break

#por fim, chamamos a função final
jogo(geracao_campo, invisivel, exibicao_campo, trapaca, bombas_adjacentes, bombas_cascatas)