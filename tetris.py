import pygame

pygame.init()

CELL_SIZE = 30
SCREEN_WIDTH = 15 * CELL_SIZE
SCREEN_HEIGHT = 20 * CELL_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris v 0.2')

# --- ОБНОВЛЕНИЕ: Цвета ---
BLACK = (10, 10, 10) # Цвет для игрового поля (почти черный)
DARK_GRAY = (40, 40, 40) # Цвет панели (серый)
WHITE = (255, 255, 255) # Цвет для линии (белый)
GIRD_COLOR = (50, 50, 50)
# --- Цвет для фигурки ---
YELLOW = (255, 215, 0)

# Кординаты кубиков нашей вигуры на сетки (X, Y)
# Пусть фигура появится сверху по центру: X = 4 и 5 столбец, Y = 0 и 1 строка
figure_blocks = [[4, 0], [5, 0], [4, 1], [5, 1]]

# Координата X, где заканчивается игровое поле (10 клеток * 30 пикселей = 300px)
GAME_WIDTH = 10 * CELL_SIZE

clock = pygame.time.Clock()
FPS = 60

FALL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(FALL_EVENT, 500)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == FALL_EVENT:
            for block in figure_blocks:
                block[1] += 1

    # --- Отрисовка зон ---
    # 1. Закрытие левой части (игрового поля)
    pygame.draw.rect(screen, BLACK, (0, 0, GAME_WIDTH, SCREEN_HEIGHT))

    # 2. Закрашиваем правую чать серым
    pygame.draw.rect(screen, DARK_GRAY, (GAME_WIDTH, 0, SCREEN_WIDTH - GAME_WIDTH, SCREEN_HEIGHT))

    # 3. Прорисовка сетки
    for x in range(0, GAME_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GIRD_COLOR, (x, 0), (x, SCREEN_HEIGHT))

    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GIRD_COLOR, (0, y), (GAME_WIDTH, y))

    # Проходим по кадому кубику в нашей фигуре и рисуем его.
    for block in figure_blocks:
        block_x = block[0] * CELL_SIZE
        block_y = block[1] * CELL_SIZE

        pygame.draw.rect(screen, YELLOW, (block_x + 1, block_y + 1, CELL_SIZE - 2, CELL_SIZE - 2))

    # 4. Риусую разделяющию белую линию
    pygame.draw.line(screen, WHITE, (GAME_WIDTH, 0), (GAME_WIDTH, SCREEN_HEIGHT), 3)

    pygame.display.flip()



pygame.quit()