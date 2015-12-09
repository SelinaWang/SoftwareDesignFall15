# -*- coding: utf-8 -*-
"""
Runs interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 12-08-15
"""
import pygame
from pygame.locals import *
from sfcontroller import *
from sfmodel import *
from sfview import *
from random import randint
import time
    
if __name__ == '__main__':
    pygame.init()
    # Define screen size and initialize it
    size = (640,480)
    screen = pygame.display.set_mode(size)
    # Start the background music and make it loop infinitely with a 40% volume
    sound = pygame.mixer.Sound("sounds/POL-coconut-land-short.wav")
    sound.play(loops = -1)
    sound.set_volume(0.4)

    # Variables to keep track of the game state
    running = True
    playing = True
    eaten = False
    playAgain = False
    level = 1
    countdown = 20
    lives = 5

    # Instantiate the model, view, and controller classes
    model = SwimFishModel()
    view = SwimFishView(model, screen, level, countdown, lives)
    controller = SwimFishMouseController(model, view)

    # Display welcome and rules screen
    view.init_screen()
    time.sleep(2)
    view.rules()
    time.sleep(5)
    init = time.time()
    last_monster_spawn = init
    time_since_last_movement = init
    timer = init

    while running:
        while playing and not eaten:
            now = time.time()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                elif event.type == MOUSEMOTION:
                    controller.handle_mouse_event(event)
            #control the monsters' spawning
            #the speed at which they spawn is inversely proportional to the level
            if now - last_monster_spawn >= 50.0/(2*level+10):
                last_monster_spawn = now
                #spawn the monsters at random places
                range_left = randint(75,200)
                range_right = randint(450,550)
                for x in range(range_left,range_right,range_right-range_left-50):
                    #randomly choose one of the monsters to spawn
                    choice = model.choices[randint(0, 4)]
                    monster = Monster(90, 90, choice, x, -100)
                    model.monsters.append(monster)
            #control the monsters' movements
            #the speed at which they move is inversely proportional to the level
            if now - time_since_last_movement >= 10.0/(5*level+60):
                time_since_last_movement = now 
                for monster in model.monsters:
                    monster.move_monster()
            view.draw()
            
            # If collision happened, reset the timer
            if (controller.handle_collision()):
                eaten = True

            #  Update countdown
            if (now-timer >= 1):
                countdown -= 1
                view = SwimFishView(model, screen, level, countdown, lives)
                view.draw()
                timer = now

            # Level up after surviving 20 seconds
            if (now-init >= 20):
                level += 1
                view = SwimFishView(model, screen, level, countdown, lives)
                view.level_up()
                time.sleep(3)
                model.monsters = []
                # counter = 0
                init = time.time()
                countdown = 20
            time.sleep(0.01)

        while eaten:
            # Switch to eaten view
            if (lives >= 2):
                lives -= 1;
                view = SwimFishView(model, screen, level, countdown, lives)
                view.eaten()
                eaten = False
                playing = True
                time.sleep(3)
                model.monsters = []
                init = time.time()
                countdown = 20

            # Switch to lost view and quit
            else:
                view.lost()
                time.sleep(3)
                sound.stop()
                pygame.quit()
