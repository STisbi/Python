class Board():
    board = [[None, None, None], [None, None, None], [None, None, None]]

    winner = None

    def __init__(self):
        pass

    def PrintBoard(self):
        for row in self.board:
            for position in row:
                print("{0} ".format(position), end=' ')
            print()

    def PlaceSymbol(self, position, symbol):
        success = False

        if self.board[position[0]][position[1]] is None:
            self.board[position[0]][position[1]] = symbol
            success = True

        return success

    def IsFinished(self):
        finished = False
        draw     = True

        transposedBoard = [*zip(*self.board)]

        # Check the rows for a match
        for row in self.board:
            if self.IsSame(row):
                finished = True
                self.winner = row[0]
                break
            if not self.IsFull(row):
                draw = False

        # Check the columns for a match
        for column in transposedBoard:
            if self.IsSame(column):
                finished = True
                self.winner = column[0]
                break

        # Check the diagonals
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] is not None:
            finished = True
            self.winner = self.board[1][1]

        if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] is not None:
            finished = True
            self.winner = self.board[1][1]

        if draw:
            finished = True

        return finished

    def IsSame(self, row):
        return all((symbol == row[0] and symbol is not None) for symbol in row)

    def IsFull(self, row):
        return all((symbol is not None) for symbol in row)

    def GetWinner(self):
        return self.winner
