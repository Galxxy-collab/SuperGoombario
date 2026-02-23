from Terrain_Tile_Calculator import *
from Terrain_Tile_Info import Spritesheet
from player import Player
################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 1280, 720
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
TARGET_FPS = 60
camera_x_offset = 0
################################# LOAD PLAYER AND SPRITESHEET###################################
spritesheet = Spritesheet('../Images/Terrain_Tile_Image.png')
player_img = spritesheet.parse_sprite('left_angle_plot.png')
player_rect = player_img.get_rect()
player = Player()

#################################### LOAD THE LEVEL #######################################
map = TileMap('Terrain_Binary_Map.csv', spritesheet )
player.position.x, player.position.y = map.start_x, map.start_y

################################# GAME LOOP ##########################
while running:
    dt = clock.tick(60) * .001 * TARGET_FPS
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = True

            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = True
                camera_x_offset -= 100
            elif event.key == pygame.K_SPACE:
                player.jump()




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = False
            elif event.key == pygame.K_SPACE:
                if player.is_jumping:
                    player.velocity.y *= .25
                    player.is_jumping = False


    ################################# UPDATE/ Animate SPRITE #################################
    player.update(dt, map.tiles)
    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((0, 180, 240)) # Fills the entire screen with light blue
    map.draw_map(canvas, camera_x_offset)
    player.draw(canvas)
    window.blit(canvas, (0,0))
    pygame.display.update()








