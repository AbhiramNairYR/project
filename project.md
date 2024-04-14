import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((575, 425))
pygame.display.set_caption('Library')
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame_file/pygame_font.h', 50)
game_active = True
start_time = 0

library_surface = pygame.image.load('pygame_file/libreary1.png').convert()

player_surface = pygame.image.load('pygame_file/Player_Downsprite1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 425))
player_speed = 10

# Function to display text
text = 'sdfsd'


def display_text(text):
    text_surface = test_font.render(str(text), False, ('white'))  # White color
    text_rect = text_surface.get_rect(center=(screen.get_width() // 10, screen.get_height() // 10))
    screen.blit(text_surface, text_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_rectangle.y -= player_speed

                if event.key == pygame.K_DOWN:
                    player_rectangle.y += player_speed

                if event.key == pygame.K_LEFT:
                    player_rectangle.x -= player_speed

                if event.key == pygame.K_RIGHT:
                    player_rectangle.x += player_speed

                if event.key == pygame.K_a or event.key == pygame.K_RSHIFT:
                    print('book: animals\ntype: encyclodedia\nsummary:info on animals')  # Check for Shift key

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                player_rectangle.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(library_surface, (0, 0))

        # Boundaries
        if player_rectangle.left < 0:
            player_rectangle.left = 0
        elif player_rectangle.right > screen.get_width():
            player_rectangle.right = screen.get_width()
        if player_rectangle.top < 0:
            player_rectangle.top = 0
        elif player_rectangle.bottom > screen.get_height():
            player_rectangle.bottom = screen.get_height()

        screen.blit(player_surface, (player_rectangle))

    else:
        screen.fill((94, 129, 162))

    pygame.display.update()
    clock.tick(60)

