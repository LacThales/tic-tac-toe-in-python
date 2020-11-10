import sys #para sair do programa

explicacao = '''
//// Sobre o jogo: ////
Automaticamente você será o 1º Jogador e começará sendo o X, mas pode optar por ser o 2º Jogador (e ser o O (bola)), só deixar seu amigo começar jogando :D.
Quando for sua vez, digite o número correspondente à linha e coluna no tabuleiro para fazer sua jogada nela.
Por exemplo, digamos que você queira jogar na linha 1, coluna 1, você começara no canto superior esquerdo.
     |     |     
  X  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
    '''

tabuleiro= [    [0,0,0],
                [0,0,0],
                [0,0,0] 
            ]

def start():

    print(explicacao)
    while True:
        comecar = int(input("Digite 1 para iniciar o jogo: "))
        if comecar == 1:
            global tabuleiro
            #----------------------- tabuleiro em formato de matriz, sempre com 0, para sempre que reiniciar, poder posicionar o X(xis) e o O(bola) novamente -----------------------
            tabuleiro= [ [0,0,0],
                         [0,0,0],
                         [0,0,0] 
                        ]
            jogo()
        else:
            print("Escrita inválida, reinicie o jogo.")
            sys.exit(0) # ---------- sair do jogo -----------

def show():
    #----------------------- OBS.: range até 3 pois o jogo se baseia em um quadrado 3x3 -----------------------
    #----------------------- Linha. -----------------------
    #----------------------- Os jogadores no cód sempre serão alternados de 1 e -1, mesmo que no print apareça player 1 e 2 -------------------------
    for linha in range(0, 3):
         #----------------------- Coluna -----------------------
        for coluna in range(0, 3):
            if tabuleiro[linha][coluna] == 0:
                print(" _ ", end=' ') #----------------------- End=' ' para fazer com que o print do tabuleiro fique um do lado do outro 3x3 _ _ _ -----------------------
            elif tabuleiro[linha][coluna] == 1:
                print(" X ", end=' ')
            elif tabuleiro[linha][coluna] == -1:
                print(" O ", end=' ')
        print()

def jogo():
    chances=0
    while vencedor() == 'continue':
        print("\nPlayer ", chances%2 + 1, ' :D ')
        show()
        linha  = int(input("Digite uma linha: "))
        if linha > 3 or linha < -2:
            print("Linha inválida.")
            break
        coluna = int(input("Digite uma coluna: "))
        if coluna > 3 or coluna < -2:
            print("Coluna inválida.")
            break
        if tabuleiro[linha-1][coluna-1] == 0:
            # -------- Uma obs sobre o if a seguir: se vc digitar linha 0, aparecerá na 3º linha, se digitar linha -1, aparecerá na 2º linha e se digitar -2, aparecerá na 1º linha -------
            if(chances%2+1)==1:
                tabuleiro[linha-1][coluna-1]=1 #----- Player 1 ------
            else:
                tabuleiro[linha-1][coluna-1]=-1 #----- Player 2 ------
        else:
            print("Lugar ocupado.") # ---------- se o player oponente digitar um lugar ocupado aparecerá essa mensagem, e será voltado uma jogada ----------
            chances -=1

        if vencedor() == 1:
            print("Player ", chances%2 + 1," venceu! :D ")
            start() # ------ reiniciar o game -------
        chances +=1

def vencedor():

    #----------------------- Verificar as linhas -----------------------
    for linha in range(0, 3):
        verif_venc = tabuleiro[linha][0]+tabuleiro[linha][1]+tabuleiro[linha][2]
        #----------------------- Sempre comparando com as somas = 3 pois o jogo acaba assim que somar 3 lados seguidos e certos -----------------------
        if verif_venc==3 or verif_venc ==-3:
            return 1 #------------------------ Retornar 1 para vencedor e então ir para a linha 71 -----------------------
    #----------------------- Verificar as colunas -----------------------
    for coluna in range(0, 3):
        verif_venc = tabuleiro[0][coluna]+tabuleiro[1][coluna]+tabuleiro[2][coluna]
        if verif_venc==3 or verif_venc ==-3:
            return 1
    #----------------------- Diagonal não usei for pois ele pega 1 por 1 no range -----------------------
    #----------------------- Verificar as diagonais -----------------------
    diagonal_e = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2] 
    diagonal_d = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if diagonal_e==3 or diagonal_e==-3: 
        return 1
    if diagonal_d==3 or diagonal_d==-3:
        return 1
    return 'continue' #---------------- serve para que caso n haja vencedor o jogo continue rodando -------------------
start()
