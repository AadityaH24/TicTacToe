# Tictactoe game in python


class game:
    def __init__(self):
        self.board ={ 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
        self.chars = ["X","O"]
        print("Start")
        self.turn(0)

    def turn(self,charIndex):
        
        self.printBoard()
        print("Player " + self.chars[charIndex])
        self.getMove(self.chars[charIndex])
        if(self.checkWin() == None):
            if(self.checkDraw()):
                print("Draw")
                exit()
            self.turn(charIndex^1)
            
        else:
            print("Winner is: " + self.checkWin())

    def checkWin(self):
        # Check diagonals
        if(self.board[1] == self.board[5] == self.board[9] and self.board[1] != ' '):
            return self.board[5]
        elif(self.board[3] == self.board[5] == self.board[7] and self.board[3] != ' '):
            return self.board[5]
        # Check rows
        elif(self.board[1] == self.board[2] == self.board[3] and self.board[1] != ' '):
            return self.board[1]
        elif(self.board[4] == self.board[5] == self.board[6] and self.board[4] != ' '):
            return self.board[4]
        elif(self.board[7] == self.board[8] == self.board[9] and self.board[7] != ' '):
            return self.board[7]
        # Check columns
        elif(self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' '):
            return self.board[1]
        elif(self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' '):
            return self.board[2]
        elif(self.board[3] == self.board[6] == self.board[9] and self.board[3] != ' '):
            return self.board[3]
        else:
            return None

    def checkDraw(self): #If game not won and all positions filled
        if(self.checkWin() == None):
            for i in self.board:
                if(self.board[i] == ' '):
                    return False
            return True


    def place(self,pos,char):
        self.board[pos] = char

    def getMove(self,char): # Get move from player and play the move if possible
        pos = int(input("Enter position: "))
        if(self.board[pos] == ' '):
            self.place(pos,char)
        else:
            print("Invalid move. Reselect")
            self.getMove(char)


    def printBoard(self):
        print("----------------")
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print("----------------")


game()