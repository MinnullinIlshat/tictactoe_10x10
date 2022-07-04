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

CIRCLE_COLOR = (0, 255, 0)
BLUE = (0, 0, 255)

BOARD_ROWS = 10 # количество строк
BOARD_COLS = 10 # количество столбцов

CIRCLE_RADIUS = 20 # радиус круга
CIRCLE_WIDTH = 5 # толщина круга

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
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 60 + 30), int(row * 60 + 30)),
                                    CIRCLE_RADIUS, CIRCLE_WIDTH)

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


draw_lines()

player = 1

# основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_row = mouseY // 60
            clicked_col = mouseX // 60

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                player = 1 if player == 2 else 2
                draw_figures()

    pygame.display.update()