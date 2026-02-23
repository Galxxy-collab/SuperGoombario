'''
-------------------------------------------------------------------------------
Name:  Level_4.py

Purpose: Creates a level featuring custom graphics, collisions, and enemies. The level design involves drawing elements on the screen, managing player interactions, and implementing game mechanics

Author: Super Goombario Team (Michael Mondaini, Eric Ardelean, Rikaysh Bidani)

Course Code: ICS4U1

Created:  01/18/2023
------------------------------------------------------------------------------
'''

# -- Imports necessary pygame module for the program --
import pygame.sprite

def play_level_4():

    # -- Importing necessary variables for the program --
    import pygame as py
    import os
    import time
    import random
    import sys
    from Level_4 import play_level_4
    from Menu import main_menu

    # -- Set necessary variables to global status for program execution within the function --
    global player_walking_state
    global player_idle_state
    global player_jumping_state
    global enemy_walking_state
    global game_over_menu_counter
    global player_lives

    # -- Define variables required for program execution --
    camera_offset_x = 0
    enemy_walking_state = 0
    player_walking_state = 0
    player_jumping_state = 0
    player_idle_state = 0
    player_lives = 3
    game_over_menu_counter = 0
    player_can_move = True
    jump = [False]
    jump_counter = 12
    jump_counter2 = 12
    active = True
    player_facing_right = True
    player_dead = False
    global_player_x_position = 210
    player_x_position = 210
    player_y_position = 345
    player_ground_position = 345
    ground_height = 345
    player_dead_next_round = False
    velocity = 10
    run_velocity = 15
    player_idle_list = [1, 1, 1]

    # -- Initialize Pygame --
    py.init()
  
    # -- Set program window resolution --
    resolution_width = 1280
    resolution_height = 720  # Running 720p currently

    # -- Create Pygame screen for displaying graphics based on program resolution --
    win = py.display.set_mode((resolution_width, resolution_height))

    # -- Report successful attempt to play the level and write to text file --
    file_path = os.path.join("Entry Attempts/Level 1 Attempts.txt")
    with open(file_path, "w") as data_save_table:
        data_save_table.write("0") 

    # -- Walk Animations (Player) --
    player_walk_animation_1 = py.image.load(
        os.path.join('Images/Player Animations/Walk Animations/Goombario_Walk_1.png')).convert_alpha()
    player_walk_animation_1 = py.transform.scale(player_walk_animation_1, (128, 128))
    player_walk_animation_2 = py.image.load(
        os.path.join('Images/Player Animations/Walk Animations/Goombario_Walk_2.png')).convert_alpha()
    player_walk_animation_2 = py.transform.scale(player_walk_animation_2, (128, 128))
    player_walk_animation_3 = py.image.load(
        os.path.join('Images/Player Animations/Walk Animations/Goombario_Walk_3.png')).convert_alpha()
    player_walk_animation_3 = py.transform.scale(player_walk_animation_3, (128, 128))

    # -- Run Animations (Player) --
    player_run_animation_1 = py.image.load(
        os.path.join('Images/Player Animations/Run Animations/Run 1.png')).convert_alpha()
    player_run_animation_1 = py.transform.scale(player_run_animation_1, (128, 128))
    player_run_animation_2 = py.image.load(
        os.path.join('Images/Player Animations/Run Animations/Run 2.png')).convert_alpha()
    player_run_animation_2 = py.transform.scale(player_run_animation_2, (128, 128))
    player_run_animation_3 = py.image.load(
        os.path.join('Images/Player Animations/Run Animations/Run 3.png')).convert_alpha()
    player_run_animation_3 = py.transform.scale(player_run_animation_3, (128, 128))

    # -- Jump Animations (Player) --
    player_jump_animation_1 = py.image.load(
        os.path.join('Images/Player Animations/Jump Animations/Player_Jump_3.png')).convert_alpha()
    player_jump_animation_1 = py.transform.scale(player_jump_animation_1, (90, 128))
    player_jump_animation_2 = py.image.load(
        os.path.join('Images/Player Animations/Jump Animations/Player_Jump_3.png')).convert_alpha()
    player_jump_animation_2 = py.transform.scale(player_jump_animation_2, (95, 128))
    player_jump_animation_3 = py.image.load(
        os.path.join('Images/Player Animations/Jump Animations/Player_Jump_3.png')).convert_alpha()
    player_jump_animation_3 = py.transform.scale(player_jump_animation_3, (90, 128))

    # -- Idle Animations (Player) --
    player_idle_animation_1 = py.image.load(
        os.path.join('Images/Player Animations/Idle Animations/Idle 1.png')).convert_alpha()
    player_idle_animation_1 = py.transform.scale(player_idle_animation_1, (128, 128))
    player_idle_animation_2 = py.image.load(
        os.path.join('Images/Player Animations/Idle Animations/Idle 2.png')).convert_alpha()
    player_idle_animation_2 = py.transform.scale(player_idle_animation_2, (128, 128))
    player_idle_animation_3 = py.image.load(
        os.path.join('Images/Player Animations/Idle Animations/Idle 3.png')).convert_alpha()
    player_idle_animation_3 = py.transform.scale(player_idle_animation_3, (128, 128))

    # -- Idle Animations (Player) --
    player_fall_animation_1 = py.image.load(
        os.path.join('Images/Player Animations/Fall Animations/Fall 1.png')).convert_alpha()
    player_fall_animation_1 = py.transform.scale(player_fall_animation_1, (128, 128))

    # -- Walk Animations (Enemy) --
    enemy_walk_animation_1 = py.image.load(
        os.path.join('Images/Enemy Animations/Walking Animations/Wallking 1.png')).convert_alpha()
    enemy_walk_animation_1 = py.transform.scale(enemy_walk_animation_1, (100, 100))
    enemy_walk_animation_2 = py.image.load(
        os.path.join('Images/Enemy Animations/Walking Animations/Wallking 2.png')).convert_alpha()
    enemy_walk_animation_2 = py.transform.scale(enemy_walk_animation_2, (100, 100))
    enemy_walk_animation_3 = py.image.load(
        os.path.join('Images/Enemy Animations/Walking Animations/Wallking 3.png')).convert_alpha()
    enemy_walk_animation_3 = py.transform.scale(enemy_walk_animation_3, (100, 100))

    # -- Sound Effects --
    player_footsteps_sound = pygame.mixer.Sound(os.path.join("Sounds/Sound Effects/Player Footsteps.mp3"))
    player_jump_sound = pygame.mixer.Sound(os.path.join("Sounds/Sound Effects/Player Jump.mp3"))
    player_die_sound = pygame.mixer.Sound(os.path.join("Sounds/Sound Effects/Player Die.mp3"))
    game_music = pygame.mixer.Sound(os.path.join("Sounds/Music/Level 1 Background Music.mp3"))
    enemy_death_sound = pygame.mixer.Sound(os.path.join("Sounds/Sound Effects/Enemy Die.mp3"))
    game_music.set_volume(0.5)
    game_music.play(-1)

    # -- Retrieve player's current amount of lives from text file --
    with open("Entry Attempts/Temp_Lives_File", "r") as data_save_table:
        data_list = data_save_table.readlines()
        player_lives = int(data_list[0])

    # -- Function to draw a block and handle player positions --
    def block(posx, posy, width, height, r, g, b, x):
        #Draw a rectangle on the window with given parameters
        py.draw.rect(win, (r, g, b), (posx, posy, width, height))
        if player_x_position == 'x':  # This condition seems incorrect; likely should be `x`
            return player_x_position
        else:
            return player_y_position

    # -- Sets program title --
    py.display.set_caption('Super Goombario')

    # -- Define Player class for drawing the player and handling animations --
    class Player(py.sprite.Sprite):
        
        #Initializes the player
        def __init__(self):
            py.sprite.Sprite.__init__(self)
            self.images = []
            self.img = py.image.load(os.path.join('Images/Player Animations/Goombario Character.png')).convert_alpha()
            self.img = py.transform.scale(self.img, (128, 128))
            self.images.append(self.img)
            self.image = self.images[0]
            self.mask = py.mask.from_surface(self.img)
            self.rect = self.image.get_rect()
            self.width = self.image.get_width()
            self.height = self.image.get_height()

        #Method to update the player's image if they are facing another direction
        def update_image(self, player_facing_right, player_walk_animation_1, player_walk_animation_2,
                         player_walk_animation_3):
            if not player_facing_right:
                global player_walk_animation_flipped_1, player_walk_animation_flipped_2, player_walk_animation_flipped_3

                player_walk_animation_1 = py.transform.flip(player_walk_animation_1, True, True)
                player_walk_animation_2 = py.transform.flip(player_walk_animation_2, True, True)
                player_walk_animation_3 = py.transform.flip(player_walk_animation_3, True, True)

        # Method to return the player's x value
        def player_x(self):
            return self.rect.x

        # Method to return the player's y value
        def player_y(self):
            return self.rect.y

        # Method to handle the player walking animation
        def player_walking(self, player_walking, player_facing_right, is_running):
            global player_walking_state

            if is_running:

                if player_walking and player_walking_state == 1 and jump_counter == 12:
                    player_footsteps_sound.play()

                if player_walking and player_walking_state < 5 and jump_counter == 12:
                    self.image = player_run_animation_1
                    
                    if not player_facing_right:
                        self.image = py.transform.flip(player_run_animation_1, True, False)
                    player_walking_state += 1
              
                elif player_walking and player_walking_state >= 5 and player_walking_state < 10 and jump_counter == 12:
                    self.image = player_run_animation_2
                    
                    if not player_facing_right:
                      self.image = py.transform.flip(player_run_animation_2, True, False)
                    player_walking_state += 1

                elif player_walking and player_walking_state >= 10 and player_walking_state < 14 and jump_counter == 12:
                    self.image = player_run_animation_3
                    
                    if not player_facing_right:
                      self.image = py.transform.flip(player_run_animation_3, True, False)
                    player_walking_state += 1

                elif player_walking and player_walking_state == 14 and jump_counter == 12:
                    self.image = player_run_animation_3

                    if not player_facing_right:
                        self.image = py.transform.flip(player_run_animation_3, True, False)
                    player_walking_state = 0

            if player_walking and player_walking_state == 1 and jump_counter == 12:
                player_footsteps_sound.play()

            if player_walking and player_walking_state < 5 and jump_counter == 12:
                self.image = player_walk_animation_1
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_walk_animation_1, True, False)
                player_walking_state += 1
              
            elif player_walking and player_walking_state >= 5 and player_walking_state < 10 and jump_counter == 12:
                self.image = player_walk_animation_2
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_walk_animation_2, True, False)
                player_walking_state += 1
              
            elif player_walking and player_walking_state >= 10 and player_walking_state < 14 and jump_counter == 12:
                self.image = player_walk_animation_3
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_walk_animation_3, True, False)
                player_walking_state += 1
              
            elif player_walking and player_walking_state == 14 and jump_counter == 12:
                self.image = player_walk_animation_3

                if not player_facing_right:
                    self.image = py.transform.flip(player_walk_animation_3, True, False)
                player_walking_state = 0

        # Method to handle the player idle animation
        def player_idle(self):
            global player_idle_state

            if player_idle_state < 7:
                self.image = player_idle_animation_1
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_idle_animation_1, True, False)
                player_idle_state += 1

            elif player_idle_state < 14:
                self.image = player_idle_animation_2
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_idle_animation_2, True, False)
                player_idle_state += 1

            elif player_idle_state < 21:
                self.image = player_idle_animation_3
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_idle_animation_3, True, False)
                player_idle_state += 1

            elif player_idle_state == 21:
                self.image = player_idle_animation_3
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_idle_animation_3, True, False)
                player_idle_state = 0

        # Method to handle the player jump animation
        def player_jumping(self):
            global player_jumping_state

            if player_jumping_state < 5:
                self.image = player_jump_animation_2
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_jump_animation_2, True, False)
                player_jumping_state += 1

            elif player_jumping_state >= 5 and player_jumping_state < 10:
                self.image = player_jump_animation_2
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_jump_animation_2, True, False)
                player_jumping_state += 1

            elif player_jumping_state >= 10 and player_jumping_state < 14:
                self.image = player_jump_animation_2
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_jump_animation_2, True, False)
                player_jumping_state += 1

            elif player_jumping_state == 14:
                self.image = player_jump_animation_2
              
                if not player_facing_right:
                    self.image = py.transform.flip(player_jump_animation_2, True, False)
                player_jumping_state = 0

        # Method to handle the player falling animation
        def player_falling(self):
            self.image = player_fall_animation_1
          
            if not player_facing_right:
                self.image = py.transform.flip(player_fall_animation_1, True, False)

    # Defines a class that draws the enemy
    class badguy(Player):
        
        #Initialize the badguy class
        def __init__(self):
            py.sprite.Sprite.__init__(self)
            self.images = []
            self.img = py.image.load(
                os.path.join('Images/Player Animations/Walk Animations/Goombario_Walk_3.png')).convert_alpha()
            self.img = py.transform.scale(self.img, (128, 128))
            self.images.append(self.img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.mask = py.mask.from_surface(self.img)
            self.width = self.image.get_width()
            self.height = self.image.get_height()

        #Method to update the enemy's image if they are facing another direction
        def update_image(self, player_facing_right):
            if not player_facing_right:
                self.image = py.transform.flip(self.images[0], True, False)
            else:
                self.image = self.images[0]

        # Method to handle the enemy walking animation
        def enemy_walking(self, player_walking, player_facing_right):
            global enemy_walking_state

            if player_walking and enemy_walking_state < 9:
              
                self.image = enemy_walk_animation_1
                if not player_facing_right:
                    self.image = py.transform.flip(enemy_walk_animation_1, True, False)
                enemy_walking_state += 1
              
            elif enemy_walking_state and enemy_walking_state >= 9 and enemy_walking_state < 18:
                self.image = enemy_walk_animation_2
              
                if not player_facing_right:
                    self.image = py.transform.flip(enemy_walk_animation_2, True, False)
                enemy_walking_state += 1
              
            elif player_walking and enemy_walking_state >= 18 and enemy_walking_state < 27:
                self.image = enemy_walk_animation_3
              
                if not player_facing_right:
                    self.image = py.transform.flip(enemy_walk_animation_3, True, False)
                enemy_walking_state += 1
              
            elif player_walking and enemy_walking_state == 27:
                self.image = enemy_walk_animation_3

                if not player_facing_right:
                    self.image = py.transform.flip(enemy_walk_animation_3, True, False)
                enemy_walking_state = 0

    #Defines a class that draws all the tiles/blocks in the game
    class tile(py.sprite.Sprite):
        
        #Initializes the tile class
        def __init__(self, x, y, img):
            py.sprite.Sprite.__init__(self)
            self.block = py.image.load(os.path.join(img)).convert_alpha()
            self.block = py.transform.scale(self.block, (128, 128))
            self.rect = self.block.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.image = self.block

        #Method to return the tile's x value
        def tilex(self):
            return self.rect.x

        #Method to return the tile's y value
        def tiley(self):
            return self.rect.y

    #Sets up grass tiles and their positions
    grass_locations = []
    grass_list = py.sprite.Group()
    tile_s = 128

    #Inadequate code kept for testing purposes
    for i in range(150):
        grass_locations.append(tile_s * i)
    for i in range(len(grass_locations)):
        grass_holder = tile(grass_locations[i], 560, 'Images/Terrain/Ground/Middle Grass.png')
        for w in range(0, 160, 128):
            dirt_holder = tile(grass_locations[i], 560 + w, 'Images/Terrain/Ground/Middle Grass.png')
            grass_list.add(dirt_holder)
        grass_list.add(grass_holder)

    #Defines active player height
    active_height = [0]

    #Defines a class that draws all the platforms in the game
    class new_plat:
      
        #Define the active class, indicating which platform the player is on
        active_class = None
        height_change = 0

        #Initialize offsets, size, height, moving offset, extra height holding variables, lists to hold collisions
        def __init__(self, offset, offset_y, size, pc, obs, mov, height, ah):
            self.offset = offset
            self.offset_y = offset_y
            self.size = size
            self.pc = pc
            self.obs = obs
            self.mov = mov
            self.height = height
            self.ah = ah

        #Method to create a platform at a given offset
        def platform1(self, file):
          
            #Make sprite group, add a bunch of tiles to desired location, set up rectangles for collisions
            p1l = []
            self.platsg = py.sprite.Group()
            
            for i in range(self.size):
                p1l.append(tile_s * i + 0 + self.offset)

            for i in range(len(p1l)):
                self.platholder = tile(p1l[i], self.offset_y, file)
                self.pc.append(self.platholder.rect)
                self.platsg.add(self.platholder)
            
            #Returns sprite group for current platform
            return self.platsg

        #Method for collision detection of platforms
        def collisons(self):
            ac = abs(camera_offset_x) + 100
            
            for i in self.obs:
                
                #For each tile in the platform, detect collision, and determine collision direction to decide if the player should be stopped or is on top

                if player.rect.colliderect(i):
                    new_plat.active_class = self
                    new_plat.height_change = self.height
                    self.ah[0] = self.height

                    if (player.rect.y < self.height):
                        self.mov[2] = 734
                        break

                    if ac < i.x:
                        self.mov[0] = 634
                        if jump[0]:
                            self.mov[2] = 734
                        break
                      
                    if ac > i.x:
                        if jump[0]:
                            self.mov[2] = 734
                        self.mov[1] = 634
                        break

                else:
                    self.mov[0] = 1
                    self.mov[1] = 1
                    self.mov[2] = 1
                    new_plat.height_change = 0
                    self.ah[0] = 0

        #Method that returns/outputs platform
        def plat_return(self):
            return self.obs

    #Method which detects which platform the player is on and swap the active platform being observed
    def which_platform(plat_list, player, active_height):
        for i in range(len(plat_list)):
            for x in range(len(plat_list[i].plat_return())):
                
              if player.colliderect(plat_list[i].plat_return()[x]):
                    plat_list[i].collisons()
                    break

    #Method for collisions and display for spikes/other dangerous objects
    def spikes(size, offset, offset_y, sc, spritelist):
        p1l = []
        platsg = py.sprite.Group()
        
        for i in range(size):
            p1l.append(tile_s * i + offset)

        for i in range(len(p1l)):
            platholder = tile(p1l[i], offset_y, 'Images/Terrain/Misc/spikes3.png')
            sc.append(platholder.rect)
            platsg.add(platholder)
            if platsg not in spritelist:
                spritelist.add(platsg)
        
        return platsg

    #Method for spike collsions
    def spike_collisons(obs):
        ac = abs(camera_offset_x) + 100
        
        for i in obs:
            if player.rect.colliderect(i):
                return True

    #Creates objects for player, player positon, and sprite group
    player = Player()
    player.rect.x = 500
    player.rect.y = 450
    player_list = py.sprite.Group()
    player_list.add(player)

    #Creates object for enemies, position, and counters for movment
    badguy1 = badguy()
    badguy1.rect.y = 344  # Floor level -28
    badguy1x = 0

    badguy2 = badguy()
    badguy2x = 0
    badguy2.rect.y = 344  # Floor level -28

    badguy3 = badguy()
    badguy3x = 0
    badguy3.rect.y = 344  # Floor level -28

    badguy4 = badguy()
    badguy4x = 0
    badguy4.rect.y = 374  # Floor level -28

    badguy5 = badguy()
    badguy5x = 0
    badguy5.rect.y = 374  # Floor level -28

    bxcounter = 0
    badguy_list = py.sprite.Group()
    badguy_list.add(badguy1, badguy2, badguy3, badguy4, badguy5)

    #Defines active player height
    active_player_height = 0

    #Creates a function for optomized ground drawing function, uses loop to easily output ground in both x and y directions
    def draw_terrain(x_location, y_location, x_size, y_size, file_location, file_size_length, file_size_width):
        image_block = py.image.load(os.path.join(file_location)).convert_alpha()
        image_block = py.transform.scale(image_block, (file_size_length, file_size_width))

        for i in range(x_size + 1):
            current_x_size = i * 128

            for z in range(y_size + 1):
                current_y_size = z * 128
                win.blit(image_block, (x_location + current_x_size, y_location + current_y_size))

    #Creates a function for drawing game over menu and updating player lives
    def game_over_menu(player_dead, given_player_lives):
        global game_over_menu_counter
        global player_lives

        if game_over_menu_counter == 1:
            time.sleep(1.5)
            player_lives += 1
            given_player_lives += 1

            with open("Entry Attempts/Temp_Lives_File", "w") as data_save_table:
                data_save_table.write(str(player_lives))

            if given_player_lives == 2 or given_player_lives == 1:
                play_level_4()
            
            elif given_player_lives == 0:
                with open("Entry Attempts/Temp_Lives_File", "w") as data_save_table:
                    data_save_table.write("3")

                with open("Entry Attempts/Temp_Level_Selection", "r") as data_save_table:
                    data_list_2 = data_save_table.readlines()
                    player_current_levels = [s.strip('\n') for s in data_list_2]

                with open("Entry Attempts/Temp_Level_Selection", "w") as data_save_table:
                    data_save_table.write(str(player_current_levels[0]) + "\n")  # Key
                    data_save_table.write(str(player_current_levels[1]) + "\n")  # Level
                    data_save_table.write(str(0) + "\n")  # XP
                    data_save_table.write(str(player_current_levels[3]) + "\n")  # XP

                game_music.stop()
                main_menu()

            if player_dead == "Won":
                game_music.stop()
                main_menu()

        if player_dead:

            if player_lives == 2 and not player_dead == "Won":
                time.sleep(1.5)
                draw_terrain(0, 0, 0, 0, "Images/User Interface/Game Over Interface/Half Health Screen.png", 1280, 720)
                game_over_menu_counter += 1

            elif player_lives == 1 and not player_dead == "Won":
                time.sleep(1.5)
                draw_terrain(0, 0, 0, 0, "Images/User Interface/Game Over Interface/No Health Screen.png", 1280, 720)
                game_over_menu_counter += 1

            elif player_lives == 0 and not player_dead == "Won":
                time.sleep(1.5)
                game_over_menu_counter += 1

                draw_terrain(0, 0, 0, 0, "Images/User Interface/Game Over Interface/Low Health Screen.png", 1280, 720)

        if player_dead == "Won":
            with open("Entry Attempts/Temp_Level_Selection", "r") as data_save_table:
                data_list_2 = data_save_table.readlines()
                player_current_levels = [s.strip('\n') for s in data_list_2]

            with open("Entry Attempts/Temp_Level_Selection", "w") as data_save_table:
                data_save_table.write(str(player_current_levels[0]) + "\n")  # Key
                data_save_table.write(str(player_current_levels[1]) + "\n")  # Level
                data_save_table.write(str(player_current_levels[2]) + "\n")  # XP
                data_save_table.write(str(player_current_levels[3]) + "\n")  # XP

            time.sleep(0.5)
            draw_terrain(0, 0, 0, 0, "Images/User Interface/Game Over Interface/Level Complete.png", 1280, 720)
            game_over_menu_counter += 1

    #Defines enemy movement amount, and movement list
    bxadd = 5
    move = [1, 1, 1]

    #Runs the main program loop
    while active:

        #Defines spikes list that will be displayed
        spike_list = py.sprite.Group()

        py.time.delay(25)
        for event in py.event.get():
            if event.type == py.QUIT:
                active = False

        # Gets what key the player has pressed
        key = py.key.get_pressed()

        #Defines player positions
        player.rect.x = player_x_position
        player.rect.y = player_y_position

        #Defines enemies positions
        badguy1.rect.x = badguy1x
        badguy2.rect.x = badguy2x
        badguy3.rect.x = badguy3x
        badguy4.rect.x = badguy4x
        badguy5.rect.x = badguy5x

        #Determines if player is dead from spike, and if they have exited
        spike_kill = False
        if key[py.K_ESCAPE]:
            main_menu()

        #Determines if player will key pressing to move right and moves player if that direction
        if not player_x_position >= 630 and key[py.K_d] and player_can_move and key[py.K_LSHIFT] or key[
            py.K_RIGHT] and player_x_position >= 630 and player_can_move and key[py.K_LSHIFT]:
            player_idle_list[2] = 0
            player.player_walking(True, player_facing_right, True)
            player_x_position += velocity

            global_player_x_position += velocity
          
            if player_facing_right == False:
                player_facing_right = True
                player.player_walking(True, player_facing_right, False)
                player.update_image(player_facing_right, player_walk_animation_1, player_walk_animation_2, player_walk_animation_3)

        #Determines if player will key pressing to move right and moves player if that direction
        elif not player_x_position >= 630 and key[py.K_d] and player_can_move or key[py.K_RIGHT] and player_can_move and player_x_position >= 630:
            player_idle_list[2] = 0
            player.player_walking(True, player_facing_right, False)
            player_x_position += velocity

            global_player_x_position += velocity
          
            if player_facing_right == False:
                player_facing_right = True
                player.player_walking(True, player_facing_right, False)
                player.update_image(player_facing_right, player_walk_animation_1, player_walk_animation_2,
                                    player_walk_animation_3)

        
        elif not key[py.K_d] and not key[py.K_RIGHT]:
            player_idle_list[2] = 1

        else:
            player_x_position == 630
        
        #Determines if player will key pressing to move right and moves player if that direction
        if player_x_position == 630 and (key[py.K_d] and player_can_move or key[py.K_RIGHT]) and player_x_position == 630 and move[0] == 1 and player_can_move:
            player_idle_list[2] = 0

            if player_facing_right == False:
                player_facing_right = True

                player.update_image(player_facing_right, player_walk_animation_1, player_walk_animation_2, player_walk_animation_3)

            if key[py.K_d] and key[py.K_LSHIFT] and player_can_move or key[py.K_RIGHT] and key[
                py.K_LSHIFT] and player_can_move:
                camera_offset_x += -(run_velocity)
                global_player_x_position += run_velocity
                player.player_walking(True, player_facing_right, True)

            else:
                camera_offset_x += -(velocity)
                global_player_x_position += velocity
                player.player_walking(True, player_facing_right, False)

        else:
            player_idle_list[2] = 1

        #Determines if player will key pressing to move left and moves player if that direction
        if player_x_position == 630 and (key[py.K_a] and player_can_move or key[py.K_LEFT]) and player_x_position == 630 and move[1] == 1 and player_can_move:

            player_idle_list[1] = 0

            if player_facing_right == True:
                player_facing_right = False
                player.player_walking(True, player_facing_right, False)
                player.update_image(player_facing_right, player_walk_animation_1, player_walk_animation_2,
                                    player_walk_animation_3)

            if key[py.K_a] and key[py.K_LSHIFT] and player_can_move or key[py.K_LEFT] and key[
                py.K_LSHIFT] and player_can_move:
                camera_offset_x += run_velocity
                global_player_x_position -= run_velocity
                player.player_walking(True, player_facing_right, True)

            else:
                camera_offset_x += velocity
                global_player_x_position -= velocity
                player.player_walking(True, player_facing_right, False)

        elif (key[py.K_a] or key[py.K_LEFT]) and move[1] == 1 and player_can_move:

            player_idle_list[0] = 0
            player.player_walking(True, player_facing_right, False)
            if player_facing_right == True:
                player_facing_right = False
                player.player_walking(True, player_facing_right, False)
                player.update_image(player_facing_right, player_walk_animation_1, player_walk_animation_2,
                                    player_walk_animation_3)

            if key[py.K_a] and key[py.K_LSHIFT] and player_can_move or key[py.K_LEFT] and key[
                py.K_LSHIFT] and player_can_move:
                camera_offset_x += run_velocity
                global_player_x_position -= run_velocity

            else:
                camera_offset_x += velocity
                global_player_x_position -= velocity

        else:
            player_idle_list[1] = 1

        if move[2] == 1 and jump[0] == False:
            ground_height = player_ground_position
            if player_y_position < ground_height:
                player_y_position += 10

        #Determines if player is not jumping
        if jump[0] == False:

            if move[2] == 1 and player_can_move and (key[py.K_w] or key[py.K_UP] or key[
                py.K_SPACE]) and player_y_position >= player_ground_position and player_can_move:
                jump[0] = True
                player_idle_list[0] = 0
                player_jump_sound.play()

            else:
                player_idle_list[0] = 1

        else:

            player_idle_list[0] = 0
            if jump_counter >= -12:
                player_y_position -= (jump_counter * abs(jump_counter)) * (1 / 3)
                jump_counter -= 1

            elif player_y_position > player_ground_position - 1:  # This will execute if our jump is finished
                jump_counter = 12
                jump[0] = False
                player_y_position = player_ground_position
              
            elif move[2] == 1 and jump_counter == -13:
                player_y_position = player_ground_position

            if jump_counter <= 0:
                player.player_falling()
            elif jump_counter > 0:
                player.player_jumping()

        #Moves enemies by changing their position each cycle and switch direction back once a counter reaches a certain number
        badguy1x = camera_offset_x + bxcounter + 3098
        badguy2x = camera_offset_x + bxcounter + 4006
        badguy3x = camera_offset_x + bxcounter + 7098
        badguy4x = camera_offset_x + bxcounter + 10226
        badguy5x = camera_offset_x + bxcounter + 9386

        #Determines if enemy has reached their limit
        if bxcounter >= 500:
            bxadd = -5
        elif bxcounter < 0:
            bxadd = 5

        #Handles enemy walking animations
        if bxadd == 5:
            badguy1.enemy_walking(True, False)
            badguy2.enemy_walking(True, False)
            badguy3.enemy_walking(True, False)
            badguy4.enemy_walking(True, False)
            badguy5.enemy_walking(True, False)

        elif bxadd == -5:
            badguy1.enemy_walking(True, True)
            badguy2.enemy_walking(True, True)
            badguy3.enemy_walking(True, True)
            badguy4.enemy_walking(True, True)
            badguy5.enemy_walking(True, True)

        #Adds movement shift to the enemies
        bxcounter += bxadd

        #Fills the screen with orange as the background
        win.fill((251, 144, 98))  
        
        #Draws the sky using the draw_terrain method
        draw_terrain(-2000 + camera_offset_x, 0, 120, 5, "Images/Terrain/Sky/Sky Top.png", 128, 128)
        draw_terrain(-2000 + camera_offset_x, 425, 120, 0, "Images/Terrain/Sky/Sky Middle.png", 128, 128)
        draw_terrain(-2000 + camera_offset_x, 553, 120, 5, "Images/Terrain/Sky/Sky Bottom.png", 128, 128)

        #Draws the clouds using the draw_terrain method
        draw_terrain(250 + (camera_offset_x / 2), 75, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(1000 + (camera_offset_x / 2), 63, 0, 0, "Images/Terrain/Clouds/Cloud 2.png", 222, 72)
        draw_terrain(1500 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 2.png", 222, 72)
        draw_terrain(1650 + (camera_offset_x / 2), 100, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(2432 + (camera_offset_x / 2), 63, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(3354 + (camera_offset_x / 2), 75, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(4654 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(5362 + (camera_offset_x / 2), 100, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(5865 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(6523 + (camera_offset_x / 2), 75, 0, 0, "Images/Terrain/Clouds/Cloud 2.png", 222, 72)
        draw_terrain(6546 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(6954 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(7845 + (camera_offset_x / 2), 63, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(7954 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(8065 + (camera_offset_x / 2), 75, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(8100 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(8150 + (camera_offset_x / 2), 63, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(8354 + (camera_offset_x / 2), 49, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(8485 + (camera_offset_x / 2), 63, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(8676 + (camera_offset_x / 2), 100, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(9654 + (camera_offset_x / 2), 75, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(10432 + (camera_offset_x / 2), 63, 0, 0, "Images/Terrain/Clouds/Cloud 2.png", 222, 72)
        draw_terrain(10876 + (camera_offset_x / 2), 100, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(11543 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 2.png", 222, 72)
        draw_terrain(12453 + (camera_offset_x / 2), 100, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(12876 + (camera_offset_x / 2), 100, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(13325 + (camera_offset_x / 2), 63, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(14453 + (camera_offset_x / 2), 75, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)
        draw_terrain(14876 + (camera_offset_x / 2), 100, 0, 0, "Images/Terrain/Clouds/Cloud 1.png", 222, 72)
        draw_terrain(15453 + (camera_offset_x / 2), 55, 0, 0, "Images/Terrain/Clouds/Cloud 3.png", 222, 72)

        #Draws the level entrance using the draw_terrain method
        draw_terrain(300 + camera_offset_x, 125, 0, 0, "Images/Terrain/Level Entrance/Level 4/Level 4.png", 250, 250)

        #Draws both player and enemy graphics with animations
        player_list.draw(win)
        badguy_list.draw(win)

        #Defines accumlator lists and variables
        pch = []
        pch2 = []
        pch3 = []
        move = [1, 1, 1]
        active_height = [0]

        #Handles drawing the entire map, with tiles and spikes using the draw terrain method
        draw_terrain(1050 + camera_offset_x, 548, 6, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(1050 + camera_offset_x, 676, 6, 2, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(1946 + camera_offset_x, 548, 0, 0, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(1946 + camera_offset_x, 676, 0, 2, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        spikes(1, 1500 + camera_offset_x, 420, pch3, spike_list).draw(win)
        spikes(1, 1750 + camera_offset_x, 420, pch3, spike_list).draw(win)

        draw_terrain(2234 + camera_offset_x, 548, 0, 0, "Images/Terrain/Ground/Single Grass.png", 128, 128)
        draw_terrain(2234 + camera_offset_x, 676, 0, 2, "Images/Terrain/Ground/Single Ground.png", 128, 128)

        draw_terrain(2522 + camera_offset_x, 500, 0, 0, "Images/Terrain/Ground/Single Grass.png", 128, 128)
        draw_terrain(2522 + camera_offset_x, 628, 0, 2, "Images/Terrain/Ground/Single Ground.png", 128, 128)

        draw_terrain(2810 + camera_offset_x, 452, 0, 0, "Images/Terrain/Ground/Single Grass.png", 128, 128)
        draw_terrain(2810 + camera_offset_x, 580, 0, 2, "Images/Terrain/Ground/Single Ground.png", 128, 128)

        draw_terrain(3098 + camera_offset_x, 444, 0, 0, "Images/Terrain/Ground/Left Grass.png", 128, 128)
        draw_terrain(3098 + camera_offset_x, 572, 0, 2, "Images/Terrain/Ground/Left Middle Ground.png", 128, 128)
        draw_terrain(3226 + camera_offset_x, 444, 9, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(3226 + camera_offset_x, 572, 9, 2, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(4506 + camera_offset_x, 444, 0, 0, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(4506 + camera_offset_x, 572, 0, 2, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        draw_terrain(4794 + camera_offset_x, 480, 0, 0, "Images/Terrain/Ground/Left Grass.png", 128, 128)
        draw_terrain(4794 + camera_offset_x, 608, 0, 0, "Images/Terrain/Ground/Left Middle Ground.png", 128, 128)
        draw_terrain(4922 + camera_offset_x, 480, 6, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(4922 + camera_offset_x, 608, 6, 0, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(5818 + camera_offset_x, 480, 0, 0, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(5818 + camera_offset_x, 608, 0, 0, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        spikes(1, 5200 + camera_offset_x, 352, pch3, spike_list).draw(win)
        spikes(1, 5450 + camera_offset_x, 352, pch3, spike_list).draw(win)

        draw_terrain(6106 + camera_offset_x, 480, 0, 0, "Images/Terrain/Ground/Single Grass.png", 128, 128)
        draw_terrain(6106 + camera_offset_x, 608, 0, 2, "Images/Terrain/Ground/Single Ground.png", 128, 128)

        draw_terrain(6394 + camera_offset_x, 550, 0, 0, "Images/Terrain/Ground/Single Grass.png", 128, 128)
        draw_terrain(6394 + camera_offset_x, 678, 0, 2, "Images/Terrain/Ground/Single Ground.png", 128, 128)

        draw_terrain(6682 + camera_offset_x, 480, 0, 0, "Images/Terrain/Ground/Single Grass.png", 128, 128)
        draw_terrain(6682 + camera_offset_x, 608, 0, 2, "Images/Terrain/Ground/Single Ground.png", 128, 128)

        draw_terrain(6970 + camera_offset_x, 444, 0, 0, "Images/Terrain/Ground/Left Grass.png", 128, 128)
        draw_terrain(6970 + camera_offset_x, 572, 0, 0, "Images/Terrain/Ground/Left Middle Ground.png", 128, 128)
        draw_terrain(7098 + camera_offset_x, 444, 4, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(7098 + camera_offset_x, 572, 4, 0, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(7738 + camera_offset_x, 444, 0, 0, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(7738 + camera_offset_x, 572, 0, 0, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        draw_terrain(8140 + camera_offset_x, 480, 0, 0, "Images/Terrain/Ground/Left Grass.png", 128, 128)
        draw_terrain(8140 + camera_offset_x, 572, 0, 0, "Images/Terrain/Ground/Left Middle Ground.png", 128, 128)
        draw_terrain(8268 + camera_offset_x, 480, 4, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(8268 + camera_offset_x, 572, 4, 0, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(8908 + camera_offset_x, 480, 0, 0, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(8908 + camera_offset_x, 572, 0, 0, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        spikes(1, 8228 + camera_offset_x, 352, pch3, spike_list).draw(win)
        spikes(1, 8450 + camera_offset_x, 352, pch3, spike_list).draw(win)

        draw_terrain(9386 + camera_offset_x, 474, 0, 0, "Images/Terrain/Ground/Left Grass.png", 128, 128)
        draw_terrain(9386 + camera_offset_x, 602, 0, 0, "Images/Terrain/Ground/Left Middle Ground.png", 128, 128)
        draw_terrain(9514 + camera_offset_x, 474, 2, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(9514 + camera_offset_x, 602, 2, 0, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(9898 + camera_offset_x, 474, 0, 0, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(9898 + camera_offset_x, 602, 0, 0, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        draw_terrain(10226 + camera_offset_x, 474, 0, 0, "Images/Terrain/Ground/Left Grass.png", 128, 128)
        draw_terrain(10226 + camera_offset_x, 602, 0, 0, "Images/Terrain/Ground/Left Middle Ground.png", 128, 128)
        draw_terrain(10354 + camera_offset_x, 474, 2, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(10354 + camera_offset_x, 602, 2, 0, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(10738 + camera_offset_x, 474, 0, 0, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(10738 + camera_offset_x, 602, 0, 0, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        draw_terrain(11066 + camera_offset_x, 500, 0, 0, "Images/Terrain/Ground/Left Grass.png", 128, 128)
        draw_terrain(11066 + camera_offset_x, 628, 0, 0, "Images/Terrain/Ground/Left Middle Ground.png", 128, 128)
        draw_terrain(11194 + camera_offset_x, 500, 5, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(11194 + camera_offset_x, 628, 5, 0, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(11962 + camera_offset_x, 500, 0, 0, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(11962 + camera_offset_x, 628, 0, 0, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        spikes(1, 11241 + camera_offset_x, 372, pch3, spike_list).draw(win)
        spikes(1, 11550 + camera_offset_x, 372, pch3, spike_list).draw(win)

        draw_terrain(11850 + camera_offset_x, 372, 0, 0, "Images/Terrain/Misc/Finish_Flag.png", 128, 128)

        draw_terrain(-128 + camera_offset_x, 473, 0, 0, "Images/Terrain/Ground/Left Grass.png", 128, 128)
        draw_terrain(-128 + camera_offset_x, 601, 0, 2, "Images/Terrain/Ground/Left Middle Ground.png", 128, 128)
        draw_terrain(0 + camera_offset_x, 473, 8, 0, "Images/Terrain/Ground/Middle Grass.png", 128, 128)
        draw_terrain(0 + camera_offset_x, 601, 8, 5, "Images/Terrain/Ground/Middle Ground.png", 128, 128)
        draw_terrain(1152 + camera_offset_x, 473, 0, 2, "Images/Terrain/Ground/Right Grass.png", 128, 128)
        draw_terrain(1152 + camera_offset_x, 601, 0, 2, "Images/Terrain/Ground/Middle Right Ground.png", 128, 128)

        #Draws the water using the draw_terrain method
        draw_terrain(-2000 + camera_offset_x, 685, 120, 1, "Images/Terrain/Water/Water " + str(3) + ".png", 128, 128)

        #Draws the player lives, based off of determinations, using the draw_terrain method
        if player_lives == 3:
            draw_terrain(50, 0, 0, 0, "Images/User Interface/In-Game Interface/Full Health UI.png", 225, 127)
        elif player_lives == 2:
            draw_terrain(50, 0, 0, 0, "Images/User Interface/In-Game Interface/Half Health UI.png", 225, 127)
        elif player_lives == 1:
            draw_terrain(50, 0, 0, 0, "Images/User Interface/In-Game Interface/Low Health UI.png", 225, 127)

        #Defines a list which contains drawn platforms
        platform_list = []

        #Determines player's current ground level, based on fixed amounts on the map
        if global_player_x_position < -250:
            player_y_position += 1
            player_ground_position = 560

        #Determinations that calculates if a player is standing on a platform, or in mid-air
        if global_player_x_position > 1260:
            player_ground_position = 420

        if global_player_x_position < 1275 and not global_player_x_position < -250:
            player_ground_position = 345

        if global_player_x_position <= 1210 and not global_player_x_position < -250 and move[2] == 1:
            player_ground_position = 345
            if global_player_x_position <= 1210 and player_y_position >= 345:
                player_y_position = 345

        if global_player_x_position > 2000 and global_player_x_position < 2200:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 2200 and global_player_x_position <= 2300:
            player_ground_position = 420

        if global_player_x_position > 2300 and global_player_x_position < 2500:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 2500 and global_player_x_position <= 2600:
            player_ground_position = 372

        if global_player_x_position > 2600 and global_player_x_position < 2800:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 2800 and global_player_x_position <= 2900:
            player_ground_position = 324

        if global_player_x_position > 2900 and global_player_x_position < 3070:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 3070 and global_player_x_position <= 4560:
            player_ground_position = 316

        if global_player_x_position > 4560 and global_player_x_position < 4780:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 4780 and global_player_x_position <= 5880:
            player_ground_position = 352

        if global_player_x_position > 5880 and global_player_x_position < 6090:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 6090 and global_player_x_position <= 6170:
            player_ground_position = 352

        if global_player_x_position > 6170 and global_player_x_position < 6380:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 6380 and global_player_x_position <= 6460:
            player_ground_position = 422

        if global_player_x_position > 6460 and global_player_x_position < 6670:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 6665 and global_player_x_position <= 6750:
            player_ground_position = 352

        if global_player_x_position > 6750 and global_player_x_position < 6960:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 6960 and global_player_x_position <= 7805:
            player_ground_position = 316

        if global_player_x_position > 7805 and global_player_x_position < 8095:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 8095 and global_player_x_position <= 8975:
            player_ground_position = 352

        if global_player_x_position > 8975 and global_player_x_position < 9305:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 9305 and global_player_x_position <= 9960:
            player_ground_position = 346

        if global_player_x_position > 9960 and global_player_x_position < 10210:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 10210 and global_player_x_position <= 10805:
            player_ground_position = 346

        if global_player_x_position > 10805 and global_player_x_position < 11055:
            player_y_position += 1
            player_ground_position = 560

        if global_player_x_position >= 11055 and global_player_x_position <= 12030:
            player_ground_position = 372

        #Determines if player has finished the game, and if true calls game over function
        if global_player_x_position >= 11825:
            game_over_menu("Won", player_lives)

        #Determines if player has touched water or not
        if global_player_x_position > 12030:
            player_y_position += 1
            player_ground_position = 560

        if player_y_position > 550:
            player_can_move = False

        if player_y_position >= 610:
            game_music.stop()
            player_die_sound.play()
            # time.sleep(1.5)

            player_dead = True
            player_lives -= 1

        #Checks if game is over
        game_over_menu(player_dead, player_lives)

        #Draws platforms based on eariler defined values
        which_platform(platform_list, player.rect, active_height)

        #Detects if player is jumping or not
        if move[2] != 1 and player_can_move and (key[py.K_w] or key[py.K_UP] or key[py.K_SPACE]):
            jump[0] = True

        #Calculates player's platform height
        if move[2] != 1:
            player_y_position = active_height[0] - 8
            if jump[0] == True:
                if jump_counter >= -12:
                    player_y_position -= (jump_counter * abs(jump_counter)) * (1 / 3)
                    jump_counter -= 1
                    jump_counter2 = jump_counter

                else:  # This will execute if our jump is finished
                    jump_counter = 12
                    jump[0] = False

        #Determines if player collides with enemy head on, if true player dies
        if py.sprite.spritecollide(player, badguy_list, False, py.sprite.collide_mask) and jump[0] == True:
            collison = py.sprite.spritecollide(player, badguy_list, True, py.sprite.collide_mask)
            enemy_death_sound.play()

        elif py.sprite.spritecollide(player, badguy_list, False, py.sprite.collide_mask):
            game_music.stop()
            player_die_sound.play()

            player_dead = True
            player_lives -= 1

        if py.sprite.spritecollide(player, spike_list, True, py.sprite.collide_mask):
            game_music.stop()
            player_die_sound.play()

            player_dead = True
            player_lives -= 1

        if player_idle_list[0] == 1 and player_idle_list[1] == 1 and player_idle_list[2] == 1:
            player.player_idle()
        
      #Updates game frames
        py.display.update()

    py.quit()