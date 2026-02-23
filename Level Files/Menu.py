'''
-------------------------------------------------------------------------------
Name:  Menu.py

Purpose: The main menu allows the player to select different options such as playing the game, logging in, viewing stats, and changing settings. It also includes a level selection menu where the player can choose a specific level to play.

Author: Super Goombario Team (Michael Mondaini, Eric Ardelean, Rikaysh Bidani)

Course Code: ICS4U1

Created:  01/18/2023
------------------------------------------------------------------------------
'''

def main_menu():
    import pygame
    import os
    import time
    from Level_1 import play_level_1
    from Level_2 import play_level_2
    from Level_3 import play_level_3
    from Level_4 import play_level_4

    # Initialize pygame
    pygame.init()
    pygame.display.set_caption('Super Goombario')

    # Set screen resolution
    resolution_width = 1280
    resolution_height = 720
    screen = pygame.display.set_mode((resolution_width, resolution_height))

    # Read current game entry from file
    with open("Entry Attempts/Level 1 Attempts.txt", "r") as data_save_table:
        data_list = data_save_table.readlines()
        current_game_entry = [s.strip('\n') for s in data_list]

    # Initialize global variables
    global level_selection_menu
    global level_menu_current_selection
    global level_menu_prevention
    level_menu_prevention = False
    menu_selection = 1
    menu_quit_selection = 1
    game_entry_counter = 0
    level_menu_current_selection = 1
    level_selection_menu = False
    main_menu_display = True
    key_cooldown = 0

    # Load background image
    background_image = pygame.image.load(os.path.join('Images/Main_Menu_Background.png')).convert_alpha()
    background_image = pygame.transform.scale(background_image, (1280, 720))

    # Load menu images
    menu_play_image = pygame.image.load(os.path.join('Images/Menu_Play.png')).convert_alpha()
    menu_play_image = pygame.transform.scale(menu_play_image, (1280, 720))

    menu_login_image = pygame.image.load(os.path.join('Images/Menu_Login.png')).convert_alpha()
    menu_login_image = pygame.transform.scale(menu_login_image, (1280, 720))

    menu_stats_image = pygame.image.load(os.path.join('Images/Menu_Stats.png')).convert_alpha()
    menu_stats_image = pygame.transform.scale(menu_stats_image, (1280, 720))

    menu_settings_image = pygame.image.load(os.path.join('Images/Menu_Settings.png')).convert_alpha()
    menu_settings_image = pygame.transform.scale(menu_settings_image, (1280, 720))

    menu_quit_yes = pygame.image.load(os.path.join('Images/Menu_Quit (YES).png')).convert_alpha()
    menu_quit_yes = pygame.transform.scale(menu_quit_yes, (1280, 720))

    menu_quit_no = pygame.image.load(os.path.join('Images/Menu_Quit (NO).png')).convert_alpha()
    menu_quit_no = pygame.transform.scale(menu_quit_no, (1280, 720))

    # Load level selection images
    level_1_unlocked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_1_unlocked.png')).convert_alpha()
    level_1_selected = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_1_selected.png')).convert_alpha()

    level_2_locked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_2_locked.png')).convert_alpha()
    level_2_unlocked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_2_unlocked.png')).convert_alpha()
    level_2_selected = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_2_selected.png')).convert_alpha()

    level_3_locked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_3_locked.png')).convert_alpha()
    level_3_unlocked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_3_unlocked.png')).convert_alpha()
    level_3_selected = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_3_selected.png')).convert_alpha()

    level_4_locked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_4_locked.png')).convert_alpha()
    level_4_unlocked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_4_unlocked.png')).convert_alpha()
    level_4_selected = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_4_selected.png')).convert_alpha()

    level_5_locked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_5_locked.png')).convert_alpha()
    level_5_unlocked = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_5_unlocked.png')).convert_alpha()
    level_5_selected = pygame.image.load(os.path.join('Images/User Interface/Level Selection/level_5_selected.png')).convert_alpha()

    level_back_unselected = pygame.image.load(os.path.join('Images/User Interface/Level Selection/back_button_unselected.png')).convert_alpha()
    level_back_selected = pygame.image.load(os.path.join('Images/User Interface/Level Selection/back_button_selected.png')).convert_alpha()

    # Load sounds
    button_select_sound = pygame.mixer.Sound("Sounds/Sound Effects/Mario_Selection_Sound.mp3")
    menu_music = pygame.mixer.Sound(os.path.join("Sounds/Music/Mario_Menu_Music.mp3"))
    menu_music.play(-1)

    transition_done = False
    transition_size = 0
    inverse_transition_size = 1100
    transition_start = False

    #Defines function named transition, used for testing purposes and future switching screens
    def transition():
        global transition_done
        global transition_size
        global inverse_transition_size

        if not transition_done:
            if transition_size == 1100:
                transition_done = True
                transition_size = 0
                inverse_transition_size = 0
            else:
                transition_size += 13.75
                inverse_transition_size -= 13.75

        return transition_done

    #Defines class named Transition which handles all screen switching
    class Transition:
        def __init__(self, transition_start, menu_quit_selection):
            self.transition_start = transition_start
            self.menu_quit_selection = menu_quit_selection
            self.transition_done = False

        def transition_play(self):
            global transition_done
            global transition_size

            if not transition_done:
                if round(transition_size, 2) == 1100:
                    self.transition_done = True
                    transition_size = 0
                else:
                    transition_size += 4.4

        def transition_reverse(self):
            global transition_done
            global inverse_transition_size

            if not transition_done:
                if round(inverse_transition_size, 2) == 0:
                    self.transition_done = True
                    inverse_transition_size = 1100
                else:
                    inverse_transition_size -= 4.4

    #Defines a transition for quitting using the transition class
    quit_menu_transition = Transition(False, 1)

    #Determines if the user has picked a level, and if so to quit main menu
    if int(current_game_entry[0]) == 1:
        menu_music.stop()
        done = True
    else:
        done = False

    #A while loop which acts as the main game processing loop
    while not done:
        for event in pygame.event.get():

            #Determine if player is quitting
            if event.type == pygame.QUIT:
                done = True

            #Allows for a cooldown period before key presses, eliminates key holds
            if key_cooldown != 0:
                key_cooldown -= 1
            else:
                key = pygame.key.get_pressed()

            #Determines if transition has not yet started, and if so to define the main menu background
            if not transition_start or not quit_menu_transition.transition_start:
                screen.fill((173, 216, 230))
                screen.blit(background_image, (0, 0))

            #Handles menu selections
            if not quit_menu_transition.transition_start and not level_selection_menu:
                if (key[pygame.K_w] and menu_selection < 4 or key[pygame.K_UP]) and menu_selection > 1:
                    menu_selection -= 1
                    button_select_sound.play()
                elif (key[pygame.K_s] and menu_selection < 4 or key[pygame.K_DOWN]) and menu_selection < 4:
                    menu_selection += 1
                    button_select_sound.play()

                #Determines if user has selected to play the game, and if so to load corresponding images
                if menu_selection == 1 and not level_selection_menu:
                    screen.blit(menu_play_image, (0, 0))

                    if not quit_menu_transition.transition_start and key[pygame.K_RETURN]:
                        level_selection_menu = True

                        with open("Entry Attempts/Temp_Level_Selection", "r") as data_save_table:
                            data_list_2 = data_save_table.readlines()
                            player_current_levels = [s.strip('\n') for s in data_list_2]

                        main_menu_display = True
                        level_menu_prevention = True

                #Determines if user has selected to login, and if so to load corresponding images (WIP)
                elif menu_selection == 2 and not level_selection_menu:
                    if key[pygame.K_RETURN]:
                        transition_start = True
                    elif transition_start:
                        if not transition_done:
                            transition()
                        else:
                            screen.fill((0,0,0))
                    else:
                        screen.blit(menu_login_image, (0, 0))

                #Determines if user has selected to login, and if so to load corresponding images (WIP)
                elif menu_selection == 3:
                    if key[pygame.K_RETURN]:
                        transition_start = True
                    elif transition_start:
                        if not transition_done:
                            transition()
                        else:
                            screen.fill((0,0,0))
                    else:
                        screen.blit(menu_stats_image, (0, 0))

                #Determines if user has selected to login, and if so to load corresponding images (WIP)
                elif menu_selection == 4:
                    if key[pygame.K_RETURN]:
                        transition_start = True
                    elif transition_start:
                        if not transition_done:
                            transition()
                        else:
                            screen.fill((0,0,0))
                    else:
                        screen.blit(menu_settings_image, (0, 0))

        #Determines if the transition has finished and if so to load the exit menu
        if quit_menu_transition.transition_done and quit_menu_transition.transition_start:
            screen.fill((0, 0, 0))

            if (key[pygame.K_a] or key[pygame.K_LEFT]) and quit_menu_transition.menu_quit_selection > 1:
                quit_menu_transition.menu_quit_selection -= 1
                button_select_sound.play()
            elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and quit_menu_transition.menu_quit_selection < 2:
                quit_menu_transition.menu_quit_selection += 1
                button_select_sound.play()

            if quit_menu_transition.menu_quit_selection == 1:
                screen.blit(menu_quit_yes, (0, 0))

                if key[pygame.K_RETURN]:
                    done = True

            elif quit_menu_transition.menu_quit_selection == 2:
                screen.blit(menu_quit_no, (0, 0))

                if key[pygame.K_RETURN]:
                    quit_menu_transition.transition_start = False
                    quit_menu_transition.transition_done = False
                    quit_menu_transition.menu_quit_selection = 1

        if quit_menu_transition.transition_start:
            if not quit_menu_transition.transition_done:
                quit_menu_transition.transition_play()

        #Determines if user has key pressed to move up or down, and adjusting images accordingly
        if level_selection_menu == True:
            if (key[pygame.K_w] and level_menu_current_selection < 4 or key[pygame.K_UP]) and level_menu_current_selection > 1:
                time.sleep(0.15)
                level_menu_current_selection -= 1
                button_select_sound.play()
            elif (key[pygame.K_s] and level_menu_current_selection < 4 or key[pygame.K_DOWN]) and level_menu_current_selection < 6:
                time.sleep(0.15)
                level_menu_current_selection += 1
                button_select_sound.play()

            screen.blit(background_image, (0, 0))
            main_menu_display = False

            #Determines if player currently has level 1 ready to play
            if level_menu_current_selection == 1 and level_selection_menu == True:
                screen.blit(level_1_selected, (0, 0))

                if key[pygame.K_RETURN] and not level_menu_prevention:
                    file_path = os.path.join("Entry Attempts/Level 1 Attempts.txt")
                    with open(file_path, "w") as data_save_table:
                        game_entry_counter += 1
                        data_save_table.write(str(game_entry_counter))

                    menu_music.stop()
                    play_level_1()
                    pygame.quit()

                else:
                    level_menu_prevention = False
                    time.sleep(0.1)

            else:
                screen.blit(level_1_unlocked, (0, 0))

            # Determines if player currently has level 2 unlocked to play
            if int(player_current_levels[0]) == 1 and level_menu_current_selection == 2:
                screen.blit(level_2_selected, (0, 0))

                if key[pygame.K_RETURN]:
                    file_path = os.path.join("Entry Attempts/Level 1 Attempts.txt")
                    with open(file_path, "w") as data_save_table:
                        game_entry_counter += 1
                        data_save_table.write(str(game_entry_counter))

                    menu_music.stop()
                    play_level_2()

            elif level_menu_current_selection == 2:
                screen.blit(level_2_locked, (0, 0))
                screen.blit(level_2_selected, (0, 0))
            elif int(player_current_levels[0]) == 1:
                screen.blit(level_2_unlocked, (0, 0))
            else:
                screen.blit(level_2_locked, (0, 0))

            # Determines if player currently has level 3 unlocked to play
            if int(player_current_levels[1]) == 1 and level_menu_current_selection == 3:
                screen.blit(level_3_selected, (0, 0))

                if key[pygame.K_RETURN]:
                    file_path = os.path.join("Entry Attempts/Level 1 Attempts.txt")
                    with open(file_path, "w") as data_save_table:
                        game_entry_counter += 1
                        data_save_table.write(str(game_entry_counter))

                    menu_music.stop()
                    play_level_3()

            elif level_menu_current_selection == 3:
                screen.blit(level_3_locked, (0, 0))
                screen.blit(level_3_selected, (0, 0))
            elif int(player_current_levels[1]) == 1:
                screen.blit(level_3_unlocked, (0, 0))
            else:
                screen.blit(level_3_locked, (0, 0))

            # Determines if player currently has level 4 unlocked to play
            if int(player_current_levels[2]) == 1 and level_menu_current_selection == 4:
                screen.blit(level_4_selected, (0, 0))

                if key[pygame.K_RETURN]:
                    file_path = os.path.join("Entry Attempts/Level 1 Attempts.txt")
                    with open(file_path, "w") as data_save_table:
                        game_entry_counter += 1
                        data_save_table.write(str(game_entry_counter))

                    menu_music.stop()
                    play_level_4()

            elif level_menu_current_selection == 4:
                screen.blit(level_4_locked, (0, 0))
                screen.blit(level_4_selected, (0, 0))
            elif int(player_current_levels[2]) == 1:
                screen.blit(level_4_unlocked, (0, 0))
            else:
                screen.blit(level_4_locked, (0, 0))

            # Determines if player currently has level 5 unlocked to play (WIP)
            if int(player_current_levels[3]) == 1 and level_menu_current_selection == 5:
                screen.blit(level_5_selected, (0, 0))
            elif level_menu_current_selection == 5:
                screen.blit(level_5_locked, (0, 0))
                screen.blit(level_5_selected, (0, 0))
            elif int(player_current_levels[3]) == 1:
                screen.blit(level_5_unlocked, (0, 0))
            else:
                screen.blit(level_5_locked, (0, 0))

            # Determines if player currently wants to press the back button
            if level_menu_current_selection == 6:
                screen.blit(level_back_selected, (0, 0))

                if key[pygame.K_RETURN]:
                    level_selection_menu = False
                    level_menu_prevention = True
                    level_menu_current_selection = 1

            else:
                screen.blit(level_back_unselected, (0, 0))

        pygame.display.flip()

    pygame.quit()

main_menu()
