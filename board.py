import pygame, sys
import numpy as np

pygame.init()
# display
WIDTH = 600
HEIGHT = 600
LINES_WIDTH = 2 # линии разделения (толщина)
# colors
BG_COLOR = (255, 255, 255) # цвет фона
LINES_COLOR = (150, 150, 150) # цвет линий разделения

BOARD_ROWS = 10 # количество строк
BOARD_COLS = 10 # количество столбцов

CIRCLE_COLOR = (0, 255, 0)
CIRCLE_RADIUS = 20 # радиус круга
CIRCLE_WIDTH = 5 # толщина круга

CROSS_COLOR = (0, 0, 255)
CROSS_WIDTH = 7
SPACE = 12

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Обратные крестики нолики')
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS)) # таблица из нулей

def draw_lines():
    for i in range(60, 601, 60):
        pygame.draw.line(screen, LINES_COLOR, (i, 0), (i, 600), LINES_WIDTH)
    for i in range(60, 601, 60):
        pygame.draw.line(screen, LINES_COLOR, (0, i), (600, i), LINES_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 60 + 30), 
                        int(row * 60 + 30)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 60 + SPACE, row * 60 + 60 - SPACE), 
                            (col * 60 + 60 - SPACE, row * 60 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 60 + SPACE, row * 60 + SPACE), 
                            (col * 60 + 60 - SPACE, row * 60 + 60 - SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    """"помечает ячейку меткой игрока/пк"""
    board[row][col] = player

def available_square(row, col):
    """проверяет доступность ячейки"""
    return board[row][col] == 0

def is_board_full():
    # проверяет заполнена ли доска
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False 
    return True

def check_win(player):
    global game_over
    game_over = True
    pass

def draw_vertical_winning_line(col, player):
    pass

def draw_horizontal_winning_line(row, player):
    pass 

def draw_asc_diaginal(player):
    pass 

def draw_desc_diagonal(player):
    pass 

def restart():
    global player
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()

player = 1
game_over = False

# основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_row = mouseY // 60
            clicked_col = mouseX // 60

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                check_win(player)
                player = 1 if player == 2 else 2
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()