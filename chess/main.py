import ChessEngine as ce
import chess as ch

class Main:

    def __init__(self, board=ch.Board):
        self.board=board

    #play human move (Movimento do Jogador Humando)
    def playHumanMove(self):
        try:
            print(self.board.legal_moves)
            print("""Para desfazer seu último movimento, digite "des".""")
            #Escolher o movimento do jogador humano
            play = input("Seu movimento: ")
            if (play=="des"):
                self.board.pop()
                self.board.pop()
                self.playHumanMove()
                return
            self.board.push_san(play)
        except:
            self.playHumanMove()

    #(Movimento do Jogador Máquina) Engine move
    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())  #Pega o melhor movimento para a jogada

    #Inicia um jogo
    def startGame(self):
        #Escolher a cor do jogador humano
        color=None
        while(color!="b" and color!="w"):
            color = input("""Jogador escolha o lado do tabuleiro Black ou White (Digite "b" ou "w"): """)
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("""Escolha á profundidade: """))
        if color=="b":
            while (self.board.is_checkmate()==False):
                print("A máquina esta pensando...")
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())    
        elif color=="w":
            while (self.board.is_checkmate()==False):
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("A máquina esta pensando...")
                self.playEngineMove(maxDepth, ch.BLACK)
            print(self.board)
            print(self.board.outcome())
        #Reseya o Tabuleiro
        self.board.reset
        #Star em outro jogo
        self.startGame()

#Criar uma instância e dar start
newBoard= ch.Board()
game = Main(newBoard)
bruh = game.startGame()
