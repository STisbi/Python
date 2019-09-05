class Player():
    symbol = None
    isHuman = True
    turn = False

    def __init__(self, symbol, isHuman):
        self.symbol = symbol
        self.isHuman = isHuman
        self.turn = False

    def GetSymbol(self):
        return self.symbol

    def IsTurn(self):
        return self.turn

    def TurnStart(self):
        self.turn = True

    def TurnEnd(self):
        self.turn = False

    def Move(self):
        position = []

        if self.isHuman:
            position = self.GetUserInput()
        else:
            pass

        return position

    def GetUserInput(self):
        position = [int(x) for x in input("Enter position for move as (row, column) integers. Ex: 0 2\nMove: ").split()]

        return position
