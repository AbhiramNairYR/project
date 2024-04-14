import pygame
from sys import exit
import sqlite3

pygame.init()
screen = pygame.display.set_mode((575, 425))
pygame.display.set_caption('2D Library')
clock = pygame.time.Clock()
test_font = pygame.font.SysFont('Comic Sans MS', 50)
game_active = True
start_time = 0

# Connect to the SQLite database
conn = sqlite3.connect('library_database.db')
c = conn.cursor()

# Create a table to store book information if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY, title TEXT, book_type TEXT, summary TEXT)''')

# Sample data insertion
c.execute("INSERT INTO books (title, book_type, summary) VALUES ('Animals Encyclopedia', 'Encyclopedia', 'Info on animals')")

conn.commit()

library_surface = pygame.image.load('pygame_file/libreary1.png').convert()

player_surface = pygame.image.load('pygame_file/Player_Downsprite1.png').convert_alpha()
player_surface = pygame.transform.rotozoom(player_surface,0,1.3)
player_rectangle = player_surface.get_rect(midbottom=(80, 425))
player_speed = 10

# Function to display text
text = False
def display_text(str):
    text_surface = test_font.render(str,False,'white','black')  # White color
    text_surface = pygame.transform.rotozoom(text_surface, 0, 0.25)
    screen.blit(text_surface, (100,100))


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

                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    text=True

                if event.key == pygame.K_SPACE or event.key == pygame.K_BACKSPACE:
                    text=False


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                player_rectangle.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(library_surface, (0, 0))

        if text:
            # Query SQLite database to retrieve book information
            c.execute("SELECT * FROM books WHERE title='Animals Encyclopedia'")
            book_info = c.fetchone()
            if book_info:
                display_text(f'Book: {book_info[1]} Type: {book_info[2]} Summary: {book_info[3]}')

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
