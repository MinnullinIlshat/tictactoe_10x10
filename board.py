import pygame, sys
import numpy as np

WIDTH = 600
HEIGHT = 600
LINES_WIDTH = 2 # линии разделения (толщина)
BOARD_ROWS = 10 # количество строк
BOARD_COLS = 10 # количество столбцов
SQUARE_SIZE = WIDTH // BOARD_COLS

CIRCLE_RADIUS = SQUARE_SIZE//3 # радиус круга
CIRCLE_WIDTH = 5 # толщина круга
CROSS_WIDTH = 7
SPACE = SQUARE_SIZE//4

BG_COLOR = (255, 255, 255) # цвет фона
LINES_COLOR = (150, 150, 150) # цвет линий разделения
CIRCLE_COLOR = (0, 255, 0)
CROSS_COLOR = (0, 0, 255)

pygame.init()
# display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Обратные крестики нолики')
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS)) # таблица из нулей

def draw_lines():
    for i in range(SQUARE_SIZE, WIDTH + 1, SQUARE_SIZE):
        pygame.draw.line(screen, LINES_COLOR, (i, 0), (i, HEIGHT), LINES_WIDTH)
    for i in range(SQUARE_SIZE, HEIGHT + 1, SQUARE_SIZE):
        pygame.draw.line(screen, LINES_COLOR, (0, i), (WIDTH, i), LINES_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), 
                        int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                            (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                            (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)


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

def all_the_same(values):
    # проверяет все ли элементы в списке одинаковые
    return len(set(values)) == 1

def check_vertical_combo(player):
    for row in range(BOARD_ROWS - 5):
        for col in range(BOARD_COLS):
            if board[row][col] != player:
                continue
            values = [board[row+i][col] for i in range(5)]
            if all_the_same(values):
                draw_vertical_winning_line(row, col, player)
                return True 
    return False

def check_horizontal_combo(player):
    for col in range(BOARD_COLS - 5):
        for row in range(BOARD_ROWS):
            if board[row][col] != player:
                continue
            values = [board[row][col+i] for i in range(5)]
            if all_the_same(values):
                draw_horizontal_winning_line(row, col, player)
                return True 
    return True
            

def check_asc_diagonal(player):
    for row in range(5, BOARD_ROWS):
        for col in range(BOARD_COLS - 5):
            if board[row][col] != player:
                continue 
            values = [board[row+i][col-i] for i in range(5)]
            if all_the_same(values):
                draw_asc_diaginal(row, col, player)
                return True 
    return False

def check_desc_diagonal(player):
    for row in range(BOARD_ROWS - 5):
        for col in range(BOARD_COLS - 5):
            if board[row][col] != player:
                continue 
            values = [board[row+i][col+i] for i in range(5)]
            if all_the_same(values):
                draw_desc_diagonal(row, col, player)
                return True
    return False 

def check_win(player):
    """проверяет есть ли комбинации для победы"""
    global game_over
    if any((check_vertical_combo(player),
        check_horizontal_combo(player),
        check_asc_diagonal(player),
        check_desc_diagonal(player),)):
        game_over = True
    else: return False 
    return True 

def draw_vertical_winning_line(row, col, player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
    start = (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE)
    end = (start[0], start[1] + SQUARE_SIZE * 5)
    pygame.draw.line(screen, color, start, end, 15)
    
def draw_horizontal_winning_line(row, col, player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
    start = (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE//2)
    end = (start[0] + SQUARE_SIZE * 5, start[1])
    pygame.draw.line(screen, color, start, end, 15)

def draw_asc_diaginal(row, col, player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
    

def draw_desc_diagonal(row, col, player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
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

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                #check_win(player)
                player = 1 if player == 2 else 2
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()