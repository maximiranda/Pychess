from piece import Bishop, Queen, King, Knight, Rook, Pawn
import copy
# ALGEBRAIC NOTATION
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = ["1", "2", "3", "4", "5", "6", "7" , "8"]
squeres = [ i+j for j in numbers for i in letters]
coor_squeres = [(i, j) for i in range(7, -1, -1) for j in range(8)]
board_coor = dict(zip(squeres, coor_squeres))
game = []
movement = 1


class Board():
    
    def __init__(self):
        


        self.board = [[0 for _ in range(8)] for x in range(8)]

        self.board[0][0]= Rook(0,0, "b")
        self.board[0][1]= Knight(0,1,"b")
        self.board[0][2]= Bishop(0,2, "b")
        self.board[0][3]= Queen(0, 3, "b")
        self.board[0][4]= King(0, 4, "b")
        self.board[0][5]= Bishop(0,5, "b")
        self.board[0][6]= Knight(0,6, "b")
        self.board[0][7]= Rook(0,7, "b")

        self.board[1][0]= Pawn(1,0, "b")
        self.board[1][1]= Pawn(1,1,"b")
        self.board[1][2]= Pawn(1,2, "b")
        self.board[1][3]= Pawn(1, 3, "b")
        self.board[1][4]= Pawn(1, 4, "b")
        self.board[1][5]= Pawn(1,5, "b")
        self.board[1][6]= Pawn(1,6, "b")
        self.board[1][7]= Pawn(1,7, "b")


        self.board[7][0]= Rook(7,0, "w")
        self.board[7][1]= Knight(7,1,"w")
        self.board[7][2]= Bishop(7,2, "w")
        self.board[7][3]= Queen(7, 3, "w")
        self.board[7][4]= King(7, 4, "w")
        self.board[7][5]= Bishop(7,5, "w")
        self.board[7][6]= Knight(7,6, "w")
        self.board[7][7]= Rook(7,7, "w")

        self.board[6][0]= Pawn(6,0, "w")
        self.board[6][1]= Pawn(6,1,"w")
        self.board[6][2]= Pawn(6,2, "w")
        self.board[6][3]= Pawn(6, 3, "w")
        self.board[6][4]= Pawn(6, 4, "w")
        self.board[6][5]= Pawn(6,5, "w")
        self.board[6][6]= Pawn(6,6, "w")
        self.board[6][7]= Pawn(6,7, "w")

    def draw(self, win):
        

        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win)

    
    def select(self, row, col, color):
        global game
        prev = 0
        castling = False
        old_board = copy.deepcopy(self.board)
        old_game = copy.copy(game)
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    if self.board[i][j].selected:
                            prev = (i, j)
        if self.board[row][col] != 0:
            if self.board[row][col].color == color:
                if self.board[row][col].selected:
                    self.reset_select()
                    return color
                elif prev != 0:
                    self.reset_select()
                    return color
                else:
                    self.board[row][col].selected = True
                    return color
            else:
                if prev !=0:
                    if self.board[prev[0]][prev[1]].color == color:
                        #CAPTURE
                        selected = (row, col)
                        moves = self.board[prev[0]][prev[1]].move_list
                            
                        if selected in moves:
                            self.move(prev, selected, castling, color)
                            # print(self.is_check(color))
                            self.check_mate(color)
                            if self.is_check(color):
                                self.board = old_board
                                game = old_game
                                
                                self.reset_select()
                                return color
                            else:
                                
                                self.reset_select()
                                return self.change_turn(color)
                        else:
                            self.reset_select()
                            return color
                    else:
                        self.reset_select()
                        return color
                else:
                    self.reset_select()
                    return color
        else:
            if prev != 0:
                if self.board[prev[0]][prev[1]].color == color:
                    selected = (row, col)
                    moves = self.board[prev[0]][prev[1]].move_list
                    #KINGSIDE CASTLING
                    castling = True
                    if self.board[prev[0]][prev[1]].king and selected == (prev[0], prev[1] + 2):
                        moves = self.board[prev[0]][prev[1]].move_list
                        if (row, col) in moves:
                            self.move((prev[0], prev[1] + 3),(row, col - 1), castling, color)
                            self.move(prev, selected, castling, color)
                            self.check_mate(color)
                            if self.is_check(color):
                                self.board = old_board
                                self.reset_select()
                                game = old_game
                                return color
                            else:
                                self.reset_select()
                                return self.change_turn(color)
                    #QUEENSIDE CASTLING
                    castling = True
                    if self.board[prev[0]][prev[1]].king and selected == (prev[0], prev[1] - 2):
                        moves = self.board[prev[0]][prev[1]].move_list
                        if (row, col) in moves:
                            self.move((prev[0], prev[1] - 4),(row, col + 1), castling, color)
                            self.move(prev, selected, castling, color)
                            self.check_mate(color)
                            if self.is_check(color):
                                self.board = old_board
                                self.reset_select()
                                game = old_game
                                return color
                            else:
                                self.reset_select()
                                return self.change_turn(color)
                    if selected in moves:
                        self.move(prev, selected,castling, color)
                        self.check_mate(color)
                        if self.is_check(color):
                            self.board = old_board
                            self.reset_select()
                            game = old_game
                            return color
                        else:
                            self.reset_select()
                            return self.change_turn(color)
                    else:
                        self.reset_select()
                        return color
                else:
                    self.reset_select()
                    return color
            else:
                self.reset_select()
                return color
                


    def update_moves(self, board):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(board)


    def move(self, start, end, castling, color):

        global game
 
        old_board = copy.deepcopy(self.board)
        if self.board[end[0]][end[1]] != 0:
            self.board[end[0]][end[1]]= self.board[start[0]][start[1]]
        
            self.board[end[0]][end[1]].row = end[0]
            self.board[end[0]][end[1]].col = end[1]

            if self.board[start[0]][start[1]].first:
                self.board[start[0]][start[1]].first = False
            
            if self.board[start[0]][start[1]].rook:
                color = self.board[start[0]][start[1]].color
                king_pos = self.find_king(color)
                self.board[king_pos[0]][king_pos[1]].rook_firts = False
            self.board[start[0]][start[1]] = 0
            #ALGEBRAIC NOTATION
            #CAPTURE

            if self.is_check(self.change_turn(color)):
                for key, value in board_coor.items():
                    if value == start:
                        star_col = key
                for key, value in board_coor.items():
                    if value == end:
                        if self.board[end[0]][end[1]].queen:
                            game.append("Qx"+key+"+")
                        if self.board[end[0]][end[1]].rook and not castling:
                            game.append("Rx"+key+"+")
                        if self.board[end[0]][end[1]].bishop:
                            game.append("Bx"+key+"+")
                        if self.board[end[0]][end[1]].knight:
                            game.append("Nx"+key+"+")
                        if self.board[end[0]][end[1]].pawn:
                            game.append(star_col[0]+"x"+key+"+")    
            else:
                for key, value in board_coor.items():
                    if value == start:
                        star_col = key
                for key, value in board_coor.items():
                    if value == end:
                        if self.board[end[0]][end[1]].queen:
                            game.append("Qx"+key)
                        if self.board[end[0]][end[1]].rook and not castling:
                            game.append("Rx"+key)
                        if self.board[end[0]][end[1]].bishop:
                            game.append("Bx"+key)
                        if self.board[end[0]][end[1]].knight:
                            game.append("Nx"+key)
                        if self.board[end[0]][end[1]].pawn:
                            game.append(star_col[0]+"x"+key)

        else:
            self.board[end[0]][end[1]]= self.board[start[0]][start[1]]
            self.board[end[0]][end[1]].row = end[0]
            self.board[end[0]][end[1]].col = end[1]

            if self.board[start[0]][start[1]].first:
                self.board[start[0]][start[1]].first = False
            
            if self.board[start[0]][start[1]].rook:
                color = self.board[start[0]][start[1]].color
                king_pos = self.find_king(color)
                self.board[king_pos[0]][king_pos[1]].rook_firts = False
            self.board[start[0]][start[1]] = 0
            #ALGEBRAIC NOTATION
            #MOVEMENT
            if self.is_check(self.change_turn(color)):
                for key, value in board_coor.items():
                    if value == end:

                        if self.board[end[0]][end[1]].queen:
                            game.append("Q"+key+"+")
                        if self.board[end[0]][end[1]].rook and not castling:
                            game.append("R"+key+"+")
                        if self.board[end[0]][end[1]].bishop:
                            game.append("B"+key+"+")
                        if self.board[end[0]][end[1]].knight:
                            game.append("N"+key+"+")
                        if self.board[end[0]][end[1]].pawn:
                            game.append(key+"+")
                        if self.board[end[0]][end[1]].king:
                            if self.board[end[0]][end[1]].col == start[1] + 2:
                                game.append("O-O+")
                            elif self.board[end[0]][end[1]].col == start[1] - 2:
                                game.append("O-O-O+")
                            else:
                                game.append("K"+key)
            else:
                for key, value in board_coor.items():
                    if value == end:

                        if self.board[end[0]][end[1]].queen:
                            game.append("Q"+key)
                        if self.board[end[0]][end[1]].rook and not castling:
                            game.append("R"+key)
                        if self.board[end[0]][end[1]].bishop:
                            game.append("B"+key)
                        if self.board[end[0]][end[1]].knight:
                            game.append("N"+key)
                        if self.board[end[0]][end[1]].pawn:
                            game.append(key)
                        if self.board[end[0]][end[1]].king:
                            if self.board[end[0]][end[1]].col == start[1] + 2:
                                game.append("O-O")
                            elif self.board[end[0]][end[1]].col == start[1] - 2:
                                game.append("O-O-O")
                            else:
                                game.append("K"+key)
            






    def reset_select(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False
    
    def is_check(self, color):
        """ return True if any king is in check"""
        
        self.update_moves(self.board)
        king_pos = self.find_king(color)
        danger = self.danger_moves()
        
        if danger != 0:
            if king_pos in danger:
                # print("CHECK")
                return True
        return False

                # print("call")

    
    
    def check_mate(self, color):
        king_pos = self.find_king(color)
        danger = self.danger_moves()
        king = self.board[king_pos[0]][king_pos[1]]
        avialalbe_moves = []

        if self.is_check(color):
            for move in  danger:
                if  not move in king.move_list:
                    avialalbe_moves.append(move)
            if avialalbe_moves == 0:
                pieces_moves = self.all_valid_moves(color)
                if pieces_moves in danger:
                    print("not mate")
                else:
                    print("CHECK MATE")
                    return True

            else:
                return False

        elif avialalbe_moves == 0:
            print("DRAW")
            return False

        else:
            return False
    
    def change_turn(self, turn):
        if turn == "b":
            return "w"
        if turn == "w":
            return "b"

    def find_king(self, color):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    if self.board[i][j].king:
                        if self.board[i][j].color == color:
                            return (i, j)

    def danger_moves(self):
        moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                        for move in self.board[i][j].move_list:
                            moves.append(move)

        return moves




        # match = dict(zip(range(1, (movement + 2) // 2), game))
        # print(match)

    def all_valid_moves(self, color):
        moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    if self.board[i][j] == color:
                        moves.append(self.board[i][j].move_list)
        return moves