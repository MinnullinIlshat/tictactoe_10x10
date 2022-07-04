import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600

BG_COLOR = (255, 255, 255)
LINES_COLOR = (150, 150, 150)
LINES_WIDTH = 2
BOARD_ROWS = 10
BOARD_COLS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Обратные крестики нолики')
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines():
    for i in range(60, 601, 60):
        pygame.draw.line(screen, LINES_COLOR, (i, 0), (i, 600), LINES_WIDTH)
    for i in range(60, 601, 60):
        pygame.draw.line(screen, LINES_COLOR, (0, i), (600, i), LINES_WIDTH)

def mark_square(row, col, player):
    """"помечает ячейку меткой игрока/пк"""
    board[row][col] = player

def available_square(row, col):
    """проверяет доступность ячейки"""
    return board[row][col] == 0

draw_lines()

# основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

    pygame.display.update()