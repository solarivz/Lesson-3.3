import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("./img/foto.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("./img/target.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(2, 255), random.randint(1, 255), random.randint(3, 255))

hits = 0  # счетчик попаданий

font = pygame.font.Font(None, 36)  # шрифт для отображения счета

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1  # увеличиваем счетчик попаданий
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # отображаем счет на экране
    text = font.render(f"Hits: {hits}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()  # исправленная строка

pygame.quit()