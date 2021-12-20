import pygame
from pygame.constants import K_SPACE, MOUSEBUTTONDOWN
import game

pygame.init()

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Chess")

pics = {}

sq = 8
size_h = size_w = 800
sq_size = size_h // sq

win = pygame.display.set_mode((size_h, size_w))


def loading_pics():
    '''
    функция загружает картинки фигур
    '''
    pieces = ['pawn_b', 'pawn_w', 'castle_b', 'castle_w', 
    'bishop_b', 'bishop_w', 'knight_b', 'knight_w',
    'queen_b', 'queen_w', 'king_b', 'king_w']
    # _b - black , _w - white
    for piece in pieces:
        pics[piece] = pygame.image.load(piece + ".png")


def actions(win, g): 
    '''
    функция отображает фигуры и доску
    параметры:
    win - window (наше открывающееся окно)
    g - game.py (ссылка на документ) 
    '''
    chessboard(win)
    pieces_blit(win, g.ch_b)


def chessboard(win): 
    '''
    функция строит доску по заданным параметрам, цвет выбирается в формате RGB
    длина и ширина столбцов и строк рассчитана по формуле size_h // sq
    -------------
    параметры:
    win - window (наше открывающееся окно)
    -------------
    row - строка
    col - столбец
    pygame.draw.rect - рисует прямоугольник по заданным параметрам
    colors - двухцветный массив, используемый для отображения доски
    '''
    colors = [pygame.Color(160, 160, 160, 255), pygame.Color(88, 78, 67, 255)]
    for row in range(sq):
        for col in range(sq):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(win, color, pygame.Rect(col*sq_size, row*sq_size,\
                sq_size, sq_size))


def pieces_blit(win, ch_b): 
    '''
    функция отображает фигуры на доске по заданным параметрам, вставляя фигуру
    на заданную область pygame.Rect(20+col*sq_size,20+row*sq_size, sq_size, 
    sq_size)
    -------------
    параметры:
    win - window (наше открывающееся окно)
    сh_b - chessboard
    '''
    for row in range(sq):
        for col in range(sq):
            piece = ch_b[row][col]
            if piece != '-':
                win.blit(pics[piece], pygame.Rect(25+col*sq_size,\
                    20+row*sq_size, sq_size, sq_size))


run = True
g = game.state() 
loading_pics() #загрузка картинок
selection = () #выбирает область нажатия
last2 = [] #записывает два последних клика


while run: 
    '''
    здесь начинается так называемый игровой цикл. для какого-либо поступившего
    события по примеру нажатия на крестик или нажатие клавиши. event.button == 1
    означает, что программа срабатывает на нажатие левой кнопки мыши
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
            exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            
            mouse = pygame.mouse.get_pos()
            col = mouse[0] // sq_size
            row = mouse[1] // sq_size

            if selection == (row, col):
                selection = ()
                last2 = []
            else:
                selection = (row, col)
                last2.append(selection)
            if len(last2) == 2:
                move = game.Moving(last2[0], last2[1], g.ch_b)
                g.move_piece(move)
                selection = ()
                last2 = []
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                g.undo_step()
    
    g.checkmate()
    actions(win, g)       
    pygame.display.flip()

pygame.quit()
