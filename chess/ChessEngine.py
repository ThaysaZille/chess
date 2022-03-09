import pandas as pd
import chess as ch #import library python
import random as rd

#board = ch.Board()   - criar uma nova instância do tabuleiro de xadrez
#board.legal_moves  - retorna uma lista dinâmica de bons movimentos
#board.legal_moves.count()  - retorna quantos movimentos 
#board.push(move)   - joga uma jogada (transforma o estado do tabuleiro)
#board.pop()        - remove a última jogada jogada
#board.piece_type_at(square)   - retorna o objeto de peça ch correspondente do quadrado 
#board.turn         - retorna um objeto de cor ch

#Função para a máquina (engine) :
class Engine:

    def __init__(self, board, maxDepth, color):
        self.board=board
        self.color=color
        self.maxDepth=maxDepth
    
    def getBestMove(self):   
        return self.engine(None, 1)

    def evalFunct(self):
        compt = 0
        #Soma os valores materiais
        for i in range(64):
            compt+=self.squareResPoints(ch.SQUARES[i])
        compt += self.mateOpportunity() + self.openning() + 0.001*rd.random()
        return compt

    def mateOpportunity(self):
        if (self.board.legal_moves.count()==0):
            if (self.board.turn == self.color):
                return -999
            else:
                return 999
        else:
            return 0

    #Faz a máquina se desenvolver nos primeiros movimentos
    def openning(self):
        if (self.board.fullmove_number<10):
            if (self.board.turn == self.color):
                return 1/30 * self.board.legal_moves.count()
            else:
                return -1/30 * self.board.legal_moves.count()
        else:
            return 0

    #Recebe como entrada (quadrado)
    def squareResPoints(self, square):
        pieceValue = 0
        if(self.board.piece_type_at(square) == ch.PAWN):
            pieceValue = 1
        elif (self.board.piece_type_at(square) == ch.ROOK):
            pieceValue = 5.1
        elif (self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue = 3.33
        elif (self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue = 3.2
        elif (self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue = 8.8

        if (self.board.color_at(square)!=self.color):
            return -pieceValue
        else:
            return pieceValue

        
    def engine(self, candidate, depth):
        
        #Nenhum movimento possível ou atingiu o máximo da pesquisa de movimentos
        if ( depth == self.maxDepth
        or self.board.legal_moves.count() == 0):
            return self.evalFunct()
        
        else:
            #Obtem a lista de movimentos bons para a posição atual
            moveListe = list(self.board.legal_moves)
            
            #initialise newCandidate
            newCandidate = None
            #(uneven depth means engine's turn)
            if(depth % 2 != 0):
                newCandidate = float("-inf")
            else:
                newCandidate = float("inf")
            
            #Análise do tabuleiro após movimentos
            for i in moveListe:

                #move i
                self.board.push(i)

                #Obtem o valor do movimento i (explorando as repercursões)
                value = self.engine(newCandidate, depth + 1) 

                #minmax algoritmo:
                #if maximizing (Turno do Jogador Máquina)
                if(value > newCandidate and depth % 2 != 0):
                    #precisa salvar o movimento jogado pela máquina
                    if (depth == 1):
                        move=i
                    newCandidate = value
                #if minimizing (Turno do Jogador Humano)
                elif(value < newCandidate and depth % 2 == 0):
                    newCandidate = value

                #(se o movimento anterior foi feito pela máquina fazer isto)
                if (candidate != None
                 and value < candidate
                 and depth % 2 == 0):
                    self.board.pop()
                    break
                #(se o movimento anterior foi feito pelo jogador humano fazer isto)
                elif (candidate != None 
                and value > candidate 
                and depth % 2 != 0):
                    self.board.pop()
                    break
                
                #Desfazer último movimento
                self.board.pop()

            #Retorna resultado
            if (depth>1):
                #valor de retorno de um movimento na árvore
                return newCandidate
            else:
                #retorna o movimento (somente no primeiro movimento)
                return move



  



            
            


        


        



            






        
        




        




    
    
