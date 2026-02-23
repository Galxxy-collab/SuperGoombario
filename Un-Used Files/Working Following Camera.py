# --Deals with importing pygame--
import pygame as py

py.init()

# Set the camera offset
camera_offset_x = 0

# --Sets the resolution--
resolution_width = 1280
resolution_height = 720  # Running 720p currently
win = py.display.set_mode((resolution_width, resolution_height))

# --Player spawn position--
player_x_position = 50
player_y_position = 540

helicopter_graphic = py.image.load("../Images/Goombario-Character.png").convert_alpha()

helicopter_graphic = py.transform.scale(helicopter_graphic, (100, 100))

# --Player Size--
width = 25
length = 50

# --Player Velocity (AKA Speed)--
vel = 10
run_vel = 15

# --Acummlator variables--
jump = False
jc = 10
active = True


def block(posx, posy, width, height, r, g, b, x):
    py.draw.rect(win, (r, g, b), (posx, posy, width, height))  # This takes: window/surface, color, rect
    if player_x_position == 'x':
        return player_x_position
    else:
        return player_y_position

py.display.set_caption('Super Goombario')

# --Runs player's movements--
while active:
    py.time.delay(25)
    for event in py.event.get():
        if event.type == py.QUIT:
            active = False

    # --Gets what key the player has pressed--
    key = py.key.get_pressed()

    if player_x_position == 830 and key[py.K_d] or key[py.K_RIGHT] and player_x_position == 830:
        print("Moved")
        camera_offset_x += -10
    #else:
        #camera_offset_x = 0
    if player_x_position == 200 and key[py.K_a] or key[py.K_LEFT] and player_x_position == 200:
        camera_offset_x += 10

    # --Key D--
    if key[py.K_d] and player_x_position < 830 or key[py.K_RIGHT] and player_x_position < 830:
        if key[py.K_d] and key[py.K_LSHIFT] or key[py.K_RIGHT] and key[py.K_LSHIFT]:
            player_x_position += run_vel
        elif player_x_position < 830:
            player_x_position += vel

    # --Key A--
    if key[py.K_a] and player_x_position > 200 or key[py.K_LEFT] and player_x_position > 200:
        if key[py.K_a] and key[py.K_LSHIFT] or key[py.K_LEFT] and key[py.K_LSHIFT]:
            player_x_position -= run_vel
        elif player_x_position > 0:
            player_x_position -= vel

    if jump == False:
        # --Key S-- (But first determines if player is mid-air/jumping)
        if key[py.K_s] and player_y_position > 540 or key[py.K_DOWN] and player_y_position > 540:
            if key[py.K_s] and key[py.K_LSHIFT] or key[py.K_DOWN] and key[py.K_LSHIFT]:
                player_y_position += run_vel
            elif player_y_position > 540:
                player_y_position += vel

        # --Key W-- (But first determines if player is mid-air/jumping)
        if key[py.K_w] or key[py.K_UP] or key[py.K_SPACE]:
            jump = True


    # --Deals with the player jumping
    else:
        if jc >= -10:
            player_y_position -= (jc * abs(jc)) * (1 / 3)
            jc -= 1
        else:  # This will execute if our jump is finished
            jc = 10
            jump = False

    #camera_offset_x = resolution_width // 2 - player_x_position - width // 2

    win.fill((173, 216, 230))  # Fills the screen with blue

    py.draw.rect(win, (76, 12, 200), #THIS IS THE PLAYER!
                 (player_x_position, player_y_position, width, length))  # This takes: window/surface, color, rect
    py.draw.rect(win, (200, 76, 12), (0, 590, 10000, 500))  # This takes: window/surface, color, rect, (THIS IS THE FLOOR)

    #py.draw.rect(win, (200, 76, 12),
                 #(camera_offset_x, 590, 10000, 500))  # This takes: window/surface, color, rect, (THIS IS THE FLOOR)

    block((50 + camera_offset_x), 50, 100, 100, 0, 0, 0, player_x_position) #THIS IS THE BLACK BOX
    py.display.update()

    # --Prints player cord's, currently commeted out, cause reduces frames
    print(player_x_position,',',player_y_position)

    win.blit(helicopter_graphic, (50, 50))

py.quit()
