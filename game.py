import os
import pygame
from board import Board
pygame.init()
LEFT = 1
RIGHT = 0
rect = (0, 0, 700, 700)
turn = "w"
board = pygame.transform.scale(pygame.image.load(os.path.join("img", "board.png")), (700, 700))
bo = Board()

def redraw_gameWindow():
    
    global win
    win.blit(board, (0, 0))
    
    bo.draw(win)

    pygame.display.update()

def click(pos):

    """


    return: pos(x, y) in range 0-7 """

    x = pos[1]
    y = pos[0]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[0] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[1]
            i = int(divX / (rect[2] / 8))
            j =int (divY / (rect[3] / 8))
            return i, j
def main():
    global bo, turn
    clock = pygame.time.Clock()
    run = True
    press = 0
    while run:
        
        clock.tick(10)
         
        redraw_gameWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit
            
            if event.type == pygame.MOUSEMOTION:

                pass
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
                bo.update_moves(bo.board)
                turn = bo.select(i, j, turn)
                bo.update_moves(bo.board)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
                press += 1
                

                # print("Black is Check: ", bo.isCheck("b"))
                # print("White is Check: ", bo.checkMate("w"))

                
                
                
width = 700
heidth = 700
win = pygame.display.set_mode((width, heidth))
pygame.display.set_caption("Chess Game")
main()
