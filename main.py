import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title
pygame.display.set_caption("CCGEN")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)

# Font
font = pygame.font.Font(None, 36)

# Clock
clock = pygame.time.Clock()

# Card types
card_types = {
    1: "Visa",
    2: "Mastercard",
    3: "Amex",
    4: "JCB",
    5: "Discover",
    6: "Diners"
}

# Function to generate random CC numbers
def generate_cc_number():
    # Placeholder for CC number generation logic
    # Implement a suitable algorithm here
    return "XXXX-XXXX-XXXX-XXXX"

# Function to draw text
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Function to draw a pixelated rectangle
def draw_pixelated_rect(color, x, y, width, height, pixel_size=5):
    for i in range(height):
        for j in range(width):
            pygame.draw.rect(screen, color, (x + j * pixel_size, y + i * pixel_size, pixel_size, pixel_size))

# Function to draw the "CCGEN" title
def draw_ccgen_title():
    colors = [red, orange, yellow]
    x_offset = 10
    y_offset = 100
    for letter in "CCGEN":
        for i in range(4):
            for j in range(5):
                color_index = random.randint(0, len(colors) - 1)
                draw_pixelated_rect(colors[color_index], x_offset + j * 10, y_offset + i * 10, 5, 5)
        x_offset += 40

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen
    screen.fill(black)

    # Draw elements
    draw_ccgen_title()
    draw_text("[ By ! Vini and ! 777]", white, 250, 200)

    # Draw card type options
    y_offset = 250
    for i in range(1, 7):
        draw_text(f"[{i}] {card_types[i]}", white, 50, y_offset)
        y_offset += 40

    # Draw input prompt
    draw_text("Selecione o tipo ->", white, 50, y_offset + 40)
    pygame.draw.rect(screen, white, (400, y_offset + 40, 10, 10))

    # Generate a random CC number and display it
    cc_number = generate_cc_number()
    draw_text(cc_number, white, 50, 400)

    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
