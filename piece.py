import os
import pygame 

w_king = pygame.transform.scale(pygame.image.load(os.path.join("img", "w_king.png")),(87,87))
w_queen = pygame.transform.scale(pygame.image.load(os.path.join("img", "w_queen.png")),(87,87))
w_rook = pygame.transform.scale(pygame.image.load(os.path.join("img", "w_rook.png")),(87,87))
w_bishop = pygame.transform.scale(pygame.image.load(os.path.join("img", "w_bishop.png")),(87,87))
w_knight = pygame.transform.scale(pygame.image.load(os.path.join("img", "w_knight.png")),(87,87))
w_pawn = pygame.transform.scale(pygame.image.load(os.path.join("img", "w_pawn.png")),(87,87))



b_king = pygame.transform.scale(pygame.image.load(os.path.join("img", "b_king.png")),(87,87))
b_queen = pygame.transform.scale(pygame.image.load(os.path.join("img", "b_queen.png")),(87,87))
b_rook = pygame.transform.scale(pygame.image.load(os.path.join("img", "b_rook.png")),(87,87))
b_bishop = pygame.transform.scale(pygame.image.load(os.path.join("img", "b_bishop.png")),(87,87))
b_knight = pygame.transform.scale(pygame.image.load(os.path.join("img", "b_knight.png")),(87,87))
b_pawn = pygame.transform.scale(pygame.image.load(os.path.join("img", "b_pawn.png")),(87,87))


W = [w_king, w_queen, w_rook, w_bishop, w_knight, w_pawn]
B = [b_king, b_queen, b_rook, b_bishop, b_knight, b_pawn]


class Piece():
    
    img = -1
    rect = (0, 0, 700, 700)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):

        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []
        self.first = False
        self.king = False
        self.pawn = False
        self.rook_first = False
        self.rook = False
        self.queen = False
        self.bishop = False
        self.knight = False

    def isSelected(self):
        return self.selected

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)

    def draw(self, win):
        if self.color == "b":
            drwaThis = B[self.img]
        elif self.color == "w":
            drwaThis = W[self.img]

        if self.selected:
            moves = self.move_list
            for move in moves:
                x = int(self.startX + (move[1] * (self.rect[2] / 8)))
                y = int(self.startY + (move[0] * (self.rect[3] / 8)))
                pygame.draw.circle(win, (190, 190, 190), (x+44, y+44), 10)
        
        x = int(self.startX + (self.col * (self.rect[2] / 8)))
        y = int(self.startY + (self.row * (self.rect[3] / 8)))
        
        if self.selected:
            pygame.draw.rect(win, (238, 138, 138),(x, y, 87, 87))
        

        win.blit(drwaThis, (x, y))


class Bishop(Piece):
    img = 3
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.bishop = True

    def valid_moves(self, board):
        moves = []
        i = self.row
        j = self.col
        color = self.color
        
    #Down Right
        for _ in range(7):

            if i < 7 and j < 7:
                p = board[i+1][j+1]

                if p == 0:
                    moves.append((i + 1, j + 1))
                    
                    i += 1
                    j += 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i+1, j + 1))
                    break
                else:
                    break

            else:
                break 

        i = self.row
        j = self.col
    #Down Left
        for _ in range(7):
            if i < 7 and j > 0:
                p = board[i+1][j-1]
                if p == 0:
                    moves.append((i + 1, j - 1))
                    i += 1
                    j -= 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i+1, j - 1))
                    break
                else:
                    break

            else:
                break 

        i = self.row
        j = self.col

    #Up Right
        for _ in range(7):
            if i > 0 and j < 7:
                p = board[i-1][j+1]
                if p == 0:
                    moves.append((i - 1, j + 1))
                    i -= 1
                    j += 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i-1, j + 1))
                    break
                else:
                    break
            else:
                break 

        i = self.row
        j = self.col
    #Up Left
        for _ in range(7):
            if i > 0 and j > 0:
                p = board[i-1][j-1]
                if p == 0:
                    moves.append((i - 1, j - 1))
                    i -= 1
                    j -= 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i - 1, j - 1))
                    break
                else:
                    break
            else:
                break 

        return moves


class Knight(Piece):
    img = 4
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.knight = True

    def valid_moves(self, board):
        i = self.row
        j = self.col
        color = self.color
        moves= []

        #Down Right
        if i < 7 and j < 6:
            p = board[i + 1][j + 2]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i + 1,j + 2))
        if i < 6 and j < 7:
            p = board[i + 2][j + 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i + 2, j + 1))
        #Down Left    
        if i < 7 and j > 1:
            p = board[i + 1][j - 2]
            if p == 0 or (p != 0 and p.color != color):
                 moves.append((i + 1, j - 2))
        if i < 6 and j > 0:
            p = board[i + 2][j - 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i + 2, j - 1))
        #Up Right
        if i > 0 and j < 6:
            p = board[i - 1][j + 2]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i - 1, j + 2))
        if i > 1 and j < 7:
            p = board[i - 2][j + 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i - 2, j + 1))
        #Up Left
        if i > 0 and j > 1:
            p = board[i - 1][j - 2]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i - 1, j - 2))
        if i > 1 and j > 0:
            p = board[i - 2][j - 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i - 2, j - 1))
        return moves


class King(Piece):
    img = 0
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.rook_first = True
        self.king = True

    def valid_moves(self, board):

        moves = []
        i = self.row
        j = self.col
        color = self.color
        #Down
        if i < 7:
            p = board[i + 1][j]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i + 1, j))
        #Left
        if j > 0:
            p = board[i][j - 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i, j - 1))
        #Right
        if j < 7:
            p = board[i][j + 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i, j + 1))
        #Up
        if i > 0:
            p = board[i - 1][j]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i - 1, j))     
        #Down Left
        if i < 7 and j > 0:
            p = board[i + 1][j - 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i + 1, j - 1))  
        #Down Right
        if i < 7 and j < 7:
            p = board[i + 1][j + 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i + 1, j + 1)) 
        #Up Left
        if i > 0 and j > 0:
            p = board[i - 1][j - 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i - 1, j - 1)) 
        #Up Right
        if i > 0 and j < 7:
            p = board[i - 1][j + 1]
            if p == 0 or (p != 0 and p.color != color):
                moves.append((i - 1, j + 1)) 
        #Castle
        if self.first and self.rook_first:
            p = board[i][j - 2]
            c = board[i][j + 2]
            if p == 0:
                moves.append((i, j - 2))
            if c == 0:
                moves.append((i, j + 2))
        return moves


class Queen(Piece):
    img = 1
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.queen = True
    def valid_moves(self, board):
        moves = []
        i = self.row
        j = self.col
        color = self.color
    #Down Right
        for _ in range(7):

            if i < 7 and j < 7:
                p = board[i+1][j+1]

                if p == 0:
                    moves.append((i + 1, j + 1))
                    
                    i += 1
                    j += 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i+1, j + 1))
                    break
                else:
                    break

            
        i = self.row
        j = self.col
    #Down Left
        for _ in range(7):
            if i < 7 and j > 0:
                p = board[i+1][j-1]
                if p == 0:
                    moves.append((i + 1, j - 1))
                    i += 1
                    j -= 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i+1, j - 1))
                    break
                else:
                    break

        i = self.row
        j = self.col

    #Up Right
        for _ in range(7):
            if i > 0 and j < 7:
                p = board[i-1][j+1]
                if p == 0:
                    moves.append((i - 1, j + 1))
                    i -= 1
                    j += 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i-1, j + 1))
                    break
                else:
                    break

        i = self.row
        j = self.col
    #Up Left
        for _ in range(7):
            if i > 0 and j > 0:
                p = board[i-1][j-1]
                if p == 0:
                    moves.append((i - 1, j - 1))
                    i -= 1
                    j -= 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i - 1, j - 1))
                    break
                else:
                    break
        i = self.row
        j = self.col
    #Right
        for _ in range(7):
            if j < 7:
                p = board[i][j + 1]
                if p == 0:
                    moves.append((i,j + 1))
                    j += 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i, j + 1))
                    break
                else:
                    break
        i = self.row
        j = self.col
        
    #Left
        for _ in range(7):
            if j > 0:
                p = board[i][j - 1]
                if p == 0:
                    moves.append((i, j - 1))
                    j -= 1
                    continue
                elif p.color != color:
                    moves.append((i, j - 1))
                    break
            
        i = self.row
        j = self.col
    #Down
        for _ in range(7):
            if i < 7:
                p = board[i + 1][j]
                if p == 0:
                    moves.append((i + 1,j))
                    i += 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i + 1, j))
                    break
                else:
                    break

            
        i = self.row
        j = self.col
    #Up
        for _ in range(7):
            if i > 0:
                p = board[i - 1][j]
                if p == 0:
                    moves.append((i - 1,j))
                    i -= 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i - 1, j))
                    break
 
        return moves


class Rook(Piece):
    img = 2

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.rook = True


    def valid_moves(self, board):
        i = self.row
        j = self.col
        color = self.color
        moves= []
        #Right
        for _ in range(7):
            if j < 7:
                p = board[i][j + 1]
                if p == 0:
                    moves.append((i,j + 1))
                    j += 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i, j + 1))
                    break
                else:
                    break
        i = self.row
        j = self.col
        #Left
        for _ in range(7):
            if j > 0:
                p = board[i][j - 1]
                if p == 0:
                    moves.append((i,j - 1))
                    j -= 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i, j - 1))
                    break
                else:
                    break
            
        i = self.row
        j = self.col
        #Down
        for _ in range(7):
            if i < 7:
                p = board[i + 1][j]
                if p == 0:
                    moves.append((i + 1,j))
                    i += 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i + 1, j))
                    break
                else:
                    break
            
        i = self.row
        j = self.col
        #Up
        for _ in range(7):
            if i > 0:
                p = board[i - 1][j]
                if p == 0:
                    moves.append((i - 1,j))
                    i -= 1
                    continue
                if p != 0 and p.color != color:
                    moves.append((i - 1, j))
                    break
                else:
                    break
            

        return moves


class Pawn(Piece):
    img = 5

    def __init__(self, row, col, color):

        super().__init__(row, col, color)
        self.first = True
        self.pawn = True

    def valid_moves(self, board):
        i = self.row
        j = self.col
        color = self.color
        moves= []

        if color == "b":
            if self.first:
                
                if i < 7:
                    p = board[i + 1][j]
                    c = board[i + 2][j]
                    if p == 0:
                        moves.append((i + 1, j))
                        if c == 0:
                            moves.append((i + 2, j))
                if j > 0:
                    p = board[i + 1][j - 1]
                    if p != 0 and p.color != color:
                        moves.append((i + 1, j - 1))
                if j < 7:
                    p = board[i + 1][j + 1]
                    if p != 0 and p.color != color:
                        moves.append((i + 1, j + 1))
            else:
                if i < 7:
                    p = board[i + 1][j]
                    if p == 0:
                        moves.append((i + 1, j))
                if j > 0 and i < 7:
                    p = board[i + 1][j - 1]
                    if p != 0 and p.color != color:
                        moves.append((i + 1, j - 1))
                if j < 7 and i < 7:
                    p = board[i + 1][j + 1]
                    if p != 0 and p.color != color:
                        moves.append((i + 1, j + 1))
            # if i == 4:
            #     if j > 0:
            #         p = board[i][j-1]
            #         if p.pawn:
            #             pass
            if i == 7:
                print("turn into another piece")

            return moves

        if color == "w":
            if self.first:
                
                if i > 0:
                    p = board[i - 1][j]
                    c = board[i - 2][j]
                    if p == 0:
                        moves.append((i - 1, j))
                        if c == 0:
                            moves.append((i - 2, j))
                if j > 0:
                    p = board[i - 1][j - 1]
                    if p != 0 and p.color != color:
                        moves.append((i - 1, j - 1))
                if j < 7:
                    p = board[i - 1][j + 1]
                    if p != 0 and p.color != color:
                        moves.append((i - 1, j + 1))
            else:
                if i > 0:
                    p = board[i - 1][j]
                    if p == 0:
                        moves.append((i - 1, j))
                if j > 0 and i > 0:
                    p = board[i - 1][j - 1]
                    if p != 0 and p.color != color:
                        moves.append((i - 1, j - 1))
                if j < 7 and i > 0:
                    p = board[i - 1][j + 1]
                    if p != 0 and p.color != color:
                        moves.append((i - 1, j + 1))
            if i == 0:
                print("turn into another piece")

            return moves
