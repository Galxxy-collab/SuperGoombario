import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Collision System")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
player_y_speed = 0  # Vertical speed for jumping

# Set up object
object_size = 50
object_x = width // 2 - object_size // 2
object_y = height // 2 - object_size // 2

object_rect = pygame.Rect(object_x, object_y, object_size, object_size)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player horizontally
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Update player rect
    player_rect.x = player_x

    # Apply gravity and jump mechanics
    player_y_speed += 0.5
    player_y += player_y_speed

    # Check for collision with the object
    if player_rect.colliderect(object_rect):
        # Adjust player position to be on top of the object
        player_y = object_rect.y - player_size
        player_y_speed = 0  # Reset vertical speed

    # Check for collision with the ground
    if player_y > height - player_size:
        player_y = height - player_size
        player_y_speed = 0

    # Update player rect
    player_rect.y = player_y

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, red, player_rect)
    pygame.draw.rect(screen, red, object_rect)

    # Update display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
