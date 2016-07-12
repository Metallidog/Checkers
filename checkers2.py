class Square:
    def __init__(self, color, loc):
        self.color = color
        self.loc = loc
        self.king = False
        self.checkerAtts()
        
    def checkerAtts(self):
        """Changes the square attributes after every move"""
        self.token = True
        if self.color in ('r', 'R'):
            self.dir = 1
        elif self.color in ('b', 'B') :
            self.dir = -1
        else:
            self.dir = None
            self.token = False
            self.avail_moves = None
            


    def fill_avail_moves(self, board):
        for x in (7,9):
            if (self.loc+(x*self.dir))//8 == (self.loc//8)+self.dir: #checks if adding 7 or 9 ends up on the correct row
                look_sq = board[self.loc + (self.dir*x)] #the square that's beeing looked at
                if look_sq.color ==' ': #if there's an open space
                    self.color=['','R','B'][self.dir]
                    self.avail_moves[self.loc+(self.dir*x)] = False #adds move to dict False flag means no jump
                elif look_sq.dir == self.dir * -1: #if there's an opponnent's checker
                    if (look_sq.loc+(x*self.dir))//8 == (look_sq.loc//8)+self.dir: #makes sure not looking off the board
                        if board[self.loc+(self.dir*x*2)].color == ' ':
                            self.avail_moves[self.loc+(self.dir*x*2)]=True #adds move to dict. True flag means it's a jump
                            self.color=['','R','B'][self.dir]
                if not self.avail_moves: #make sure there isn't already an avail_move
                    self.color=['','r','b'][self.dir]

    def availMoves(self, board):
        """Looks at all checkers and decides if there's a move available.
           If there is, it stores the available move in a dict hashed to a
           flag that's True if the move is jump, or False if it's an open space.
           It also capitalizes the checker that can move and lower cases the ones that cannot."""
        self.avail_moves = {}
        if self.king:
            temp = self.dir
            for dirs in (1, -1):
                if self.loc > 55:
                    dirs = -1
                elif self.loc < 8:
                    dirs = 1
                self.dir = dirs
                self.fill_avail_moves(board)
            self.dir = temp
            print self.avail_moves
        else:
            self.fill_avail_moves(board)
        
        
    
                    
class Board:
    def __init__(self):
        '''Builds the initial board'''
        self.board = []
        checker = 'r'
        loc = 0
        for row in range(8):
            moveable = row%2
            if row>2: checker = ' '
            if row>4: checker = 'b'
            for col in range(8):
                self.board.append([Square(checker,loc),Square('+',loc)][moveable])
                moveable = not moveable
                loc += 1
                
    def moveableCheckers(self):
        '''Cycles through all board squares calls Square.availMoves() on them
           to determine if the piece can be moved.'''
        for checker in self.board:
            if checker.token:
                checker.availMoves(self.board)
       
    def display_board(self):
        for pos, loc in enumerate(self.board):
            if pos%8==0: print '\n'
            print '{}{}  '.format(loc.color, pos),
        for pos, loc in enumerate(self.board):
            if pos%8==0: print '\n'
            print '{}  '.format(loc.color),
        print
        
    def move_token(self, from_sq, to_sq):
        if to_sq not in self.board[from_sq].avail_moves: return None
        self.board[to_sq].color = self.board[from_sq].color #moves checker to new location
        if self.board[from_sq].avail_moves[to_sq]:  #if jump flag is True
            jumped = self.board[((to_sq-from_sq)/2)+from_sq] #checker to be removed
            jumped.color = ' '
            jumped.checkerAtts()
        self.board[from_sq].color = ' '
        self.board[to_sq].checkerAtts()
        self.board[from_sq].checkerAtts()
        if (self.board[to_sq].loc > 55 and self.board[to_sq].dir == 1) or (self.board[to_sq].loc<8 and self.board[to_sq].dir == -1):
            self.board[to_sq].king = True
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
