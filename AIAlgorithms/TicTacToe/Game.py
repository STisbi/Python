from AIAlgorithms.TicTacToe import Board
from AIAlgorithms.TicTacToe import Player

class Game():
    board = Board.Board()

    playerOne = None
    playerTwo = None

    def __init__(self):
        self.playerOne = Player.Player("X", True)
        self.playerTwo = Player.Player("O", True)

        self.RunGame()

    def RunGame(self):
        self.playerOne.turn = True

        while not self.board.IsFinished():
            self.board.PrintBoard()

            if self.board.PlaceSymbol(self.GetMove(), self.CurrentPlayer().GetSymbol()):
                self.EndTurn()
            else:
                print("That position is already taken.")

        self.board.PrintBoard()

        winner = self.board.GetWinner()

        if winner:
            print("The winner is {0}.".format(winner))
        else:
            print("The match was a draw.")

    def GetMove(self):
        position = []

        position = self.CurrentPlayer().Move()

        return position

    def CurrentPlayer(self):
        currentPlayer = None

        if self.playerOne.IsTurn():
            currentPlayer = self.playerOne
        else:
            currentPlayer = self.playerTwo

        return currentPlayer

    def EndTurn(self):
        if self.playerOne.IsTurn():
            self.playerOne.TurnEnd()
            self.playerTwo.TurnStart()
        else:
            self.playerTwo.TurnEnd()
            self.playerOne.TurnStart()
