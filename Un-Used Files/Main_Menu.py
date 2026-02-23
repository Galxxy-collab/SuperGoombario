
def main_menu():
    import pygame
    import os
    from Level_1a import game



    pygame.init()
    pygame.display.set_caption('Super Goombario')

    resolution_width = 1280
    resolution_height = 720  # Running 720p currently
    screen = pygame.display.set_mode((resolution_width, resolution_height))

    #Starts on the play selection
    menu_selection = 1
    menu_quit_selection = 1
    game_entry_counter = 0
    key_cooldown = 0

    #Background
    background_image = pygame.image.load(os.path.join('Images/Main_Menu_Background.png')).convert_alpha()
    background_image = pygame.transform.scale(background_image, (1280, 720))

    #Menu
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

    button_select_sound = pygame.mixer.Sound("Sounds/Sound Effects/Mario_Selection_Sound.mp3")
    menu_music = pygame.mixer.Sound(os.path.join("Sounds/Music/Mario_Menu_Music.mp3"))
    menu_music.play()

    transition_done = False
    transition_size = 0 # 16
    inverse_transition_size = 1100
    transition_start = False

    done = False

    #key[py.K_w]

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
        transition_circle = pygame.draw.circle(screen, (0, 0, 0), (resolution_width // 2, resolution_height // 2), transition_size)


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

            transition_circle = pygame.draw.circle(screen, (0, 0, 0), (resolution_width // 2, resolution_height // 2), transition_size)

        def transition_reverse(self):
            global transition_done
            global inverse_transition_size

            if not transition_done:
                if round(inverse_transition_size, 2) == 0:
                    self.transition_done = True
                    inverse_transition_size = 1100
                else:
                    inverse_transition_size -= 4.4

            transition_circle = pygame.draw.circle(screen, (0, 0, 0), (resolution_width // 2, resolution_height // 2),
                                                   inverse_transition_size)


    quit_menu_transition = Transition(False, 1)
    play_menu_transition = Transition(False, 1)




    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if key_cooldown != 0:
                key_cooldown -= 1
            else:
                key = pygame.key.get_pressed()




            if not transition_start or not quit_menu_transition.transition_start:
                screen.fill((173, 216, 230))  # Fills the screen with blue
                screen.blit(background_image, (0, 0))





            #Detects if escape
            #------------------

            # ------------------





            if not quit_menu_transition.transition_start:
                if (key[pygame.K_w] or key[pygame.K_UP]) and menu_selection > 1:
                    menu_selection -= 1
                    button_select_sound.play()
                elif (key[pygame.K_s] or key[pygame.K_DOWN]) and menu_selection < 4:
                    menu_selection += 1
                    button_select_sound.play()

                if menu_selection == 1:

                    screen.blit(menu_play_image, (0, 0))

                    if not quit_menu_transition.transition_start and key[pygame.K_RETURN]:
                        play_menu_transition.transition_start = True


                        menu_music.stop()
                        game()
                        pygame.quit()
                        #play_menu_transition.transition_play()










                elif menu_selection == 2:

                    if key[pygame.K_RETURN]:
                        transition_start = True
                    elif transition_start:
                        if not transition_done:
                            transition()
                        else:
                            screen.fill((0,0,0))
                            print("2")
                    else:
                        screen.blit(menu_login_image, (0, 0))

                elif menu_selection == 3:

                    if key[pygame.K_RETURN]:
                        transition_start = True
                    elif transition_start:
                        if not transition_done:
                            transition()
                        else:
                            screen.fill((0,0,0))
                            print("3")
                    else:
                        screen.blit(menu_stats_image, (0, 0))

                elif menu_selection == 4:

                    if key[pygame.K_RETURN]:
                        transition_start = True

                    elif transition_start:
                        if not transition_done:
                            transition()
                        else:
                            screen.fill((0,0,0))
                            print("4")

                    else:
                        screen.blit(menu_settings_image, (0, 0))

        if key[pygame.K_ESCAPE]:
            # if not quit_menu_transition.transition_done:
            quit_menu_transition.transition_start = True

        elif quit_menu_transition.transition_done and quit_menu_transition.transition_start:
            screen.fill((0, 0, 0))

            # CAUSE DRAWN IN HERE
            if (key[pygame.K_a] or key[pygame.K_LEFT]) and quit_menu_transition.menu_quit_selection > 1:
                quit_menu_transition.menu_quit_selection -= 1
                button_select_sound.play()
            elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and quit_menu_transition.menu_quit_selection < 2:
                quit_menu_transition.menu_quit_selection += 1
                button_select_sound.play()

            print(quit_menu_transition.menu_quit_selection)

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
                    #quit_menu_transition.transition_reverse(1100)

        if quit_menu_transition.transition_start:
            if not quit_menu_transition.transition_done:
                quit_menu_transition.transition_play()

        if play_menu_transition.transition_start:
            if not play_menu_transition.transition_done:
                play_menu_transition.transition_play()
            #else:
                #play_menu_transition.transition_start = False

        if play_menu_transition.transition_done and play_menu_transition.transition_start:
            screen.fill((0, 0, 0))




        pygame.display.flip()

    pygame.quit()
main_menu()
