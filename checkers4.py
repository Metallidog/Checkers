class EmptySq():
    def __init__(self, loc):
        self.color = '.'
        self.loc = loc

    @property
    def square_num(self):
        return self.loc[0]*8 + x[1] + 1

class Checker():
    def __init__(self, color, direction):
        self.color = color
        self.dir = direction

    def info(self):
        ''' Creates a readable format for board display '''
        print 'loc={}: moves = '.format(self.square_num),
        for x in self.avail_moves:
            print x[0]*8 + x[1] + 1,
        print 
   
    @property
    def square_num(self):
        return self.loc[0]*8 +self.loc[1]+1    

class Board():
    def __init__(self):
        self.board = []
        self.checker_list = []
        self.boardInitBuild()

    def boardInitBuild(self):
        ''' Initializes starting board '''

        def place_checkers():
            '''
                Using location of the square, makes a decision
                of which object to place on the board.
                Creates initial list of pieces on the board
                via checker_list.
            '''
            if 2<row<5 or not(row+col)%2:
                return EmptySq((row, col))
            else:
                checker = Checker('r', 1) if row<3 else Checker('b', -1)
                checker.loc = (row,col)
                self.checker_list.append(checker)
                return checker

        for row in range(8):
            self.board.append([])
            for col in range(8):
                self.board[row].append(place_checkers())

    def availMoves(self):
        def onBoardTest(loc_tup):
            ''' Determines if the sqaure is valid '''
            return False if -1 in loc_tup or 8 in loc_tup else True

        def lookForJump(look):
            pass

        def lookOneStep(checker):     
            r,c = checker.loc      
            for look in ((r+checker.dir, c-1), (r+checker.dir, c+1)):
                if onBoardTest(look):
                    look_at_square = self.board[look[0]][look[1]]
                    if look_at_square.color=='.':
                        checker.avail_moves.append(look) 
                    elif look_at_square.color != checker.color:
                        lookForJump(look)            
           
        for checker in self.checker_list:
            checker.avail_moves = []
            lookOneStep(checker)

    def display_board(self):
        ''' Displays info about the current state of the board '''
        for checker in self.checker_list:
            if checker.avail_moves:
                    checker.info()
                    checker.color = checker.color.upper()
            else:
                checker.color = checker.color.lower()                               
        
        count = 1
        for row in self.board:
            for sq in row:
                print '{:>4}'.format(sq.color+str(count)),
                count += 1
            print

def move():
    not_valid = True
    while not_valid:
        from_sq = raw_input("From >")
        to_sq = raw_input("To>")
        not_valid = False
            

if __name__=='__main__':
    b = Board()
    b.availMoves()
    b.display_board()
    move()
    
