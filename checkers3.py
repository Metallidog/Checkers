class Square:
    def __init__(self, color, loc, d, token):
        self.color = color
        self.loc = loc
        self.dir = d
        self.token = token
        self.avail_moves = {}

    def fill_avail_moves(self, board):
        """Looks at all checkers and decides if there's a move available.
           If there is, it stores the available move in a dict hashed to a
           flag that's True if the move is jump, or False if it's an open space.
           It also capitalizes the checker that can move and lower cases the ones that cannot."""
        for x in (7,9):
            if (self.loc+(x*self.dir))//8 == (self.loc//8)+self.dir: #checks if adding 7 or 9 ends up on the correct row
                look_sq = board[self.loc + (self.dir*x)] #the square that's beeing looked at
                if look_sq.color ==' ': #if there's an open space
                    self.color=self.color.upper()
                    self.avail_moves[self.loc+(self.dir*x)] = False #adds move to dict False flag means no jump
                elif look_sq.dir == self.dir * -1: #if there's an opponnent's checker
                    if (look_sq.loc+(x*self.dir))//8 == (look_sq.loc//8)+self.dir: #makes sure not looking off the board
                        look_2 = self.loc+(self.dir*x*2)
                        if look_2>=0 and look_2<64:
                            if board[look_2].color == ' ':
                                self.avail_moves[self.loc+(self.dir*x*2)]=True #adds move to dict. True flag means it's a jump
                                self.color=self.color.upper()
                if not self.avail_moves: #make sure there isn't already an avail_move
                    self.color=self.color.lower()

    def availMoves(self, board):
        self.avail_move = {}
        self.fill_avail_moves(board)  

class King(Square):
    def __init__(self, color, loc, d, token):    
        Square.__init__(self, color, loc, d, token)
        print self.color


                    
class Board:
    def __init__(self):
        '''Builds the initial board'''
        self.board = []
        checker = 'r'
        d = 1
        loc = 0
        token = True
        for row in range(8):
            moveable = row%2
            if row>2: 
                checker = ' '
                d = 0
                token = False
            if row>4: 
                checker = 'b'
                d = -1
                token = True
            for col in range(8):
                self.board.append([Square(checker,loc, d, token),Square('+',loc, 0, False)][moveable])
                moveable = not moveable
                loc += 1
                
    def moveableCheckers(self):
        '''Cycles through all board squares calls Square.availMoves() on them
           to determine if the piece can be moved.'''
        for checker in self.board:
            if checker.token:
                checker.availMoves(self.board)
        for x in self.board: print x.loc, x.avail_moves 
       
    def display_board(self):
        for pos, loc in enumerate(self.board):
            if pos%8==0: print '\n'
            if loc.color == '+': print ' .   ',
            else: print '{}{:<2}  '.format(loc.color, pos),
        #for pos, loc in enumerate(self.board):
        #    if pos%8==0: print '\n'
        #    print '{}  '.format(loc.color),
        print
        
    def move_token(self, from_sq, to_sq):
        if to_sq not in self.board[from_sq].avail_moves: 
            return None
        if self.board[from_sq].avail_moves[to_sq]:  #if jump flag is True
            jumped_loc = ((to_sq-from_sq)/2)+from_sq #calculate jumped checker location
            self.board[jumped_loc] = Square(' ', jumped_loc, 0, False) #replace with empty object	    
        self.board[to_sq], self.board[from_sq] = self.board[from_sq], self.board[to_sq] #swap objects from square -> to square
        self.board[to_sq].loc, self.board[from_sq].loc = self.board[from_sq].loc, self.board[to_sq].loc #swap loc attributes
        if (self.board[to_sq].loc > 55 and self.board[to_sq].dir == 1) or \
           (self.board[to_sq].loc<8 and self.board[to_sq].dir == -1):
            #self.board[to_sq].king = True
            color, loc=self.board[to_sq].color, self.board[to_sq].loc
            print color, loc
            self.board[to_sq] = King(color, loc, 0, True)
        self.moveableCheckers()
        self.display_board()

    
        
    
if __name__=='__main__':
    b = Board()
    b.moveableCheckers()
    b.display_board()
    while True:
        f = int(raw_input('from '))
        t = int(raw_input('to '))
        b.move_token(f, t)
