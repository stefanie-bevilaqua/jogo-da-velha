#__________________________Jogo__da__Velha__________________________________

#A variável "jogar" permite ao usuário escolher
#continuar jogando indefinidamente ou sair do programa
#__________________________________________________________
jogar = str(input('Digite J para jogar ou S para sair: '))
while jogar == 'J':  
#_________________________Início__do__jogo__________________________________
#Temos a função "tabuleiro", com uma matriz 3x3, permitindo que o tabuleiro
#seja impresso no decorrer do código, de forma atualizada a cada jogada
    print ("_____________________________________________")
    print ("Sejam bem-vindos ao Jogo da Velha!")
    print ("Preparados??? Lá vamos nós!!!")
    posiçao = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
    def tabuleiro():
        print(' ',posiçao[2][0],' | ' ,posiçao[2][1], ' | ' ,posiçao[2][2], '')
        print("----+-----+----")
        print(' ',posiçao[1][0],' | ' ,posiçao[1][1], ' | ' ,posiçao[1][2],'')
        print("-----+-----+----")
        print(' ',posiçao[0][0],' | ' ,posiçao[0][1], ' | ' ,posiçao[0][2], '')
    tabuleiro()
#===================================================================================
#_________________Mostrando__a__jogada__no__tabuleiro_______________________
#As funções "jogada_X" e "jogada_O" armazenam o valor da respectiva jogada,
#caso seja um valor válido, será impresso no tabuleiro, do contrário,
#o programa pedirá a posição até que seja um valor válido.   
#A variável "casaVazia" verifica se a posição escolhida está sendo ocupada ou não

    def jogada_X():
       casaVazia = True
       while casaVazia:
          jogada_X = str(input('Digite a posição onde X vai jogar: '))
          if jogada_X == '1':
             if posiçao[0][0] != 'O' and posiçao[0][0] != 'X':
                posiçao[0][0] = 'X'
                casaVazia= False
          elif jogada_X == '2':
             if posiçao[0][1] != 'O' and posiçao[0][1] != 'X':
                posiçao[0][1] = 'X'
                casaVazia= False
          elif jogada_X == '3':
             if posiçao[0][2] != 'O' and posiçao[0][2] != 'X':
                posiçao[0][2] = 'X'
                casaVazia= False
          elif jogada_X == '4':
             if posiçao[1][0] != 'O' and posiçao[1][0] != 'X':
                posiçao[1][0] = 'X'
                casaVazia= False
          elif jogada_X == '5':
             if posiçao[1][1] != 'O' and posiçao[1][1] != 'X':
                posiçao[1][1] = 'X'
                casaVazia= False
          elif jogada_X == '6':
             if posiçao[1][2] != 'O' and posiçao[1][2] != 'X':
                posiçao[1][2] = 'X'
                casaVazia= False
          elif jogada_X == '7':
             if posiçao[2][0] != 'O' and posiçao[2][0] != 'X':
                posiçao[2][0]= 'X'
                casaVazia= False
          elif jogada_X == '8':
             if posiçao[2][1] != 'O' and posiçao[2][1] != 'X':
                posiçao[2][1] = 'X'
                casaVazia= False
          elif jogada_X == '9':
             if posiçao[2][2] != 'O' and posiçao[2][2] != 'X':
                posiçao[2][2] = 'X'
                casaVazia= False

          if casaVazia:
             print('Posição inválida! Jogue novamente!')
             
          tabuleiro()
          
    def jogada_O():
       casaVazia = True
       while casaVazia:
          jogada_O = str(input('Digite a posição onde O vai jogar: '))
          if jogada_O == '1':
             if posiçao[0][0] != 'O' and posiçao[0][0] != 'X':
                posiçao[0][0] = 'O'
                casaVazia= False
          elif jogada_O == '2':
             if posiçao[0][1] != 'O' and posiçao[0][1] != 'X':
                posiçao[0][1]= 'O'
                casaVazia= False
          elif jogada_O == '3':
             if posiçao[0][2] != 'O' and posiçao[0][2] != 'X':
                posiçao[0][2] = 'O'
                casaVazia= False  
          elif jogada_O == '4':
             if posiçao[1][0] != 'O' and posiçao[1][0] != 'X':
                posiçao[1][0] = 'O'
                casaVazia= False
          elif jogada_O == '5':
             if posiçao[1][1] != 'O' and posiçao[1][1] != 'X':
                posiçao[1][1] = 'O'
                casaVazia= False
          elif jogada_O == '6':
             if posiçao[1][2] != 'O' and posiçao[1][2] != 'X':
                posiçao[1][2] = 'O'
                casaVazia= False
          elif jogada_O == '7':
             if posiçao[2][0] != 'O' and posiçao[2][0] != 'X':
                posiçao[2][0]= 'O'
                casaVazia= False
          elif jogada_O == '8':
             if posiçao[2][1] != 'O' and posiçao[2][1] != 'X':
                posiçao[2][1]= 'O'
                casaVazia= False
          elif jogada_O == '9':
             if posiçao[2][2] != 'O' and posiçao[2][2] != 'X':
                posiçao[2][2] = 'O'
                casaVazia= False

          elif casaVazia:
             print('Posição inválida! Jogue novamente!')

          tabuleiro()
#========================================================================
#____________________Verificando__vencedor!_________________________
#Foi criado um while True para a “jogada_O()” e “jogada_X()”,
#contendo as formas que os jogadores tem de ganhar.
#Temos um contador de jogadas que inicia em 0, se no final for ==9,
#significa que todas as casas estão preenchidas e não temos um vencedor.
    contaJogadas = 0
    while True:
        jogada_O()
        contaJogadas = contaJogadas + 1
        horizontal3 = [posiçao[2][0],posiçao[2][1],posiçao[2][2]]
        horizontal2 = [posiçao[1][0],posiçao[1][1],posiçao[1][2]]
        horizontal1 = [posiçao[0][0],posiçao[0][1],posiçao[0][2]]
        vertical1 = [posiçao[2][0],posiçao[1][0],posiçao[0][0]]
        vertical2 = [posiçao[2][1],posiçao[1][1],posiçao[0][1]]
        vertical3 = [posiçao[2][2],posiçao[1][2],posiçao[0][2]]
        diagonal1 = [posiçao[2][0],posiçao[1][1],posiçao[0][2]]
        diagonal2 = [posiçao[2][2],posiçao[1][1],posiçao[0][0]]

        
        if horizontal1 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif horizontal1 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif horizontal2 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif horizontal2 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif horizontal3 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif horizontal3 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif vertical1 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif vertical1 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif vertical2 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif vertical2 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif vertical3 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif vertical3 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif diagonal1 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif diagonal1 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif diagonal2 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif diagonal2 == ['O','O','O']:
          print ('O Ganhou!')
          break
        else:
           if contaJogadas==9:
              print('Que pena... Deu velha! Ninguém ganhou!')
              break
        
        jogada_X()
        contaJogadas = contaJogadas + 1
        horizontal3 = [posiçao[2][0],posiçao[2][1],posiçao[2][2]]
        horizontal2 = [posiçao[1][0],posiçao[1][1],posiçao[1][2]]
        horizontal1 = [posiçao[0][0],posiçao[0][1],posiçao[0][2]]
        vertical1 = [posiçao[2][0],posiçao[1][0],posiçao[0][0]]
        vertical2 = [posiçao[2][1],posiçao[1][1],posiçao[0][1]]
        vertical3 = [posiçao[2][2],posiçao[1][2],posiçao[0][2]]
        diagonal1 = [posiçao[2][0],posiçao[1][1],posiçao[0][2]]
        diagonal2 = [posiçao[2][2],posiçao[1][1],posiçao[0][0]]
        
        if horizontal1 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif horizontal1 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif horizontal2 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif horizontal2 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif horizontal3 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif horizontal3 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif vertical1 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif vertical1 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif vertical2 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif vertical2 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif vertical3 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif vertical1 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif diagonal1 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif diagonal1 == ['O','O','O']:
          print ('O Ganhou!')
          break
        elif diagonal2 == ['X','X','X']:
          print ('X Ganhou!')
          break
        elif diagonal2 == ['O','O','O']:
          print ('O Ganhou!')
          break
        else:
           if contaJogadas==9:
              print('Que pena... Deu velha! Ninguém ganhou!')
              break
#======================================================================
#________________________Finalizando______________________
#A variável "jogar" permite ao usuário continuar jogando indefinidamente
#(porém os pontos do jogo anterior não serão levados em consideração) ou sair do jogo.
    print (" ")
    print ("________________________________________________")
    jogar = str(input('Digite J para jogar ou S para sair: '))
else:
    print ("Okay! Bye!")
#======================================================================
