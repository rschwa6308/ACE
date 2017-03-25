import pygame
from time import sleep

from Game_Classes import *
from Colors import *




def display(screen, room, entities):
    player = entities[0]
    #screen.fill(background_color)
    screen.blit(sky_texture, (0,0))

    #adjust all images for camera scroll
    l = player.x
    t = player.y
    cwidth = 832-64*3
    cheight = 640
    cwfenton = "dank mEmes"
##    l, t, _, _ = target_rect
##    print l, t, _, _
##    _, _, w, h = camera
##    l, t, _, _ = -l+int(display_width/2), -t+int(display_height/2), w, h
##    
##    l = min(0, l)               # stop scrolling at the left edge
##    l = max(-(camera.width-832), l)   # stop scrolling at the right edge
##    t = max(-(camera.height-640), t) # stop scrolling at the bottom
##    t = min(0, t)               # stop scrolling at the top
##    print (l,t)

    #static room objects (Platforms, Ladders)
    for y in range(len(room)):
        for x in range(len(room[y])):
            if room[y][x] != 0:
                screen.blit(room[y][x].image, (x*64,y*64))
##            #draw developer grid
##            pygame.draw.rect(screen, black, pygame.Rect(x*64,y*64,64,64), 1)
                
    #entities
    for e in entities:
        screen.blit(e.get_image(), (e.x,e.y))
    
    #flip screen
    pygame.display.update()



#convert 13x9 array of numbers into 13x9 array of room objects and nulls(0s)
def room_builder(level):
    room = [[0 for x in range(len(level[0]))] for y in range(len(level))]
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 0:
                room[y][x] = 0
            elif level[y][x] == 1:
                room[y][x] = Platform(x, y)
            elif level[y][x] == 2:
                room[y][x] = Ladder(x, y)
            elif level[y][x] == 3:
                room[y][x] = Door(x, y)
    return room



def game(screen, level):

    #init entities list and local player
    entities = level.entities
    player = entities[0]

    #build room from level
    room = room_builder(level.room)

    #init display
    display(screen, room, entities)


    #init clocks
    game_clock = pygame.time.Clock()
    animation_clock = pygame.time.Clock()
    animation_tick = 180

    #main game clock
    while True:
        game_clock.tick(60)

        #USER INPUT

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.xvel = -1
                elif event.key == pygame.K_RIGHT:
                    player.xvel = 1
                elif event.key == pygame.K_UP:
                    player.yvel = -1
                elif event.key == pygame.K_DOWN:
                    player.yvel = 1
                elif event.key == pygame.K_RETURN:
                    
                    if player.door and player.key:
                        print "u beat the level!!! XDXD"
                        obj = room[player.get_grid()[1]][player.get_grid()[0]]
                        #transfer key from player to door
                        obj.key = True
                        player.key = False
                        display(screen, room, entities)
                        
                        door_clock = pygame.time.Clock()
                        for step in range(64):
                            door_clock.tick(40)
                            obj.step += 1
                            screen.blit(obj.get_image(),(player.get_grid()[0]*64,player.get_grid()[1]*64))  #only update door chunk (freeze room)
                            screen.blit(player.image,(player.get_grid()[0]*64,player.get_grid()[1]*64))
                            pygame.display.update()
                        sleep(0.5)
                        #fade to black
                        fade_to = (0,50,2)
                        overlay = pygame.Surface((832, 640))
                        overlay.fill(fade_to)
                        fade_clock = pygame.time.Clock()
                        for i in range(100):
                            fade_clock.tick(40)
                            overlay.set_alpha(i)
                            screen.blit(overlay,(0,0))
                            pygame.display.update()
                        print "done"
                        pygame.quit()
                        quit()
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.xvel = 0
                elif event.key == pygame.K_RIGHT:
                    player.xvel = 0
                elif event.key == pygame.K_UP:
                    player.yvel = 0
                elif event.key == pygame.K_DOWN:
                    player.yvel = 0



        #PLAYER MOVEMENT CONTROL iff player is moving (turn is made)

        #orient player
        if player.xvel < 0 and player.flipped == False:
            player.flipped = not player.flipped
            #print "flipping"
        elif player.xvel > 0 and player.flipped:
            player.flipped = not player.flipped
            #print "flipping"

        #player climbing animation
        target = (player.get_grid()[1]+player.yvel,player.get_grid()[0]+player.xvel)
        if isinstance(room[target[0]][target[1]], Ladder):
            #print "ladder found"
            player.climbing = True
        else:
            player.climbing = False

                
        

        #zero horizontal velocity if stand conditions not met - right
        if player.xvel > 0:
            #target cell is occupied
            if isinstance(room[player.get_grid()[1]][player.get_grid()[0]+1],Platform):
                player.xvel = 0
            #floor below target cell is not occupied
            if room[player.get_grid()[1]+1][player.get_grid()[0]+1] == 0:
                player.xvel = 0

        #zero horizontal velocity if target cell is occupied - left
        if player.xvel < 0:
            #target cell is occupied
            if isinstance(room[player.get_grid()[1]][player.get_grid()[0]-1],Platform):
                player.xvel = 0
            #floor below target cell is not occupied
            if room[player.get_grid()[1]+1][player.get_grid()[0]-1] == 0:
                player.xvel = 0

        #zero vertical velocity if not in ladder or target cell is occupied
        if isinstance(room[player.get_grid()[1]][player.get_grid()[0]],Ladder):
            #down
            if player.yvel > 0:
                if isinstance(room[player.get_grid()[1]+1][player.get_grid()[0]],Platform):
                    player.yvel = 0
                #target cell does not have ladder
                if not isinstance(room[player.get_grid()[1]+1][player.get_grid()[0]],Ladder):
                    player.yvel = 0
            #up
            if player.yvel < 0:
                #target cell is occupied
                if isinstance(room[player.get_grid()[1]-1][player.get_grid()[0]],Platform):
                    player.yvel = 0
                #target cell does not have ladder
                if not isinstance(room[player.get_grid()[1]-1][player.get_grid()[0]],Ladder):
                    player.yvel = 0
        else:
            player.yvel = 0


        #move player horizontally with accel curve (TODO: smoothe movement)
        if player.xvel != 0:
            #player.image = player_texture
            for i in range(20):             #accelerate
                animation_clock.tick(animation_tick)
                player.x += player.xvel*1
                #display frame
                display(screen, room, entities)
            for i in range(12):              #plateau
                animation_clock.tick(animation_tick)
                player.x += player.xvel*2
                #display frame
                display(screen, room, entities)
            for i in range(20):             #deccelerate
                animation_clock.tick(animation_tick)
                player.x += player.xvel*1
                #display frame
                display(screen, room, entities)
            #delay between movements (0.05-0.10)
            sleep(0.1)

        #move player vertically with accel curve (TODO: smoothe movement)
        if player.yvel != 0:
            #player.image = climb_texture
            for i in range(20):             #accelerate
                animation_clock.tick(animation_tick)
                player.y += player.yvel*1
                #display frame
                display(screen, room, entities)
            for i in range(12):              #plateau
                animation_clock.tick(animation_tick)
                player.y += player.yvel*2
                #display frame
                display(screen, room, entities)
            for i in range(20):             #deccelerate
                animation_clock.tick(animation_tick)
                player.y += player.yvel*1
                #display frame
                display(screen, room, entities)
            #delay between movements (0.05-0.10)
            #sleep(0.1)
                

        #check for door collision
        player.door = isinstance(room[player.get_grid()[1]][player.get_grid()[0]], Door)

        #check for entity collisions
        for e in entities:
            #Key collision
            if isinstance(e, Key):
                if e.x == player.x and e.y == player.y:
                    player.key = True
                    #destroy key object
                    entities.remove(e)
            #Robot collision
            if isinstance(e, Robot):
                if e.x == player.x and e.y == player.y:
                    if e.threatened:
                        entities.remove(e)
                if e.direction == "L":
                    #print "robot found"
                    if e.x - 64 == player.x and e.y == player.y:
                        print "robot got you, m8"
                    elif e.x + 64 == player.x and e.y == player.y:
                        print "can kill robot"
                        e.threatened = True
                    else:
                        e.threatened = False
                else:
                    if e.x + 64 == player.x and e.y == player.y:
                        print "robot got you, m8"
                    elif e.x - 64 == player.x and e.y == player.y:
                        print "can kill robot"
                        e.threatened = True
                    else:
                        e.threatened = False

                        
        #update entity images based off of movement-caused changes to sprites(pick up key, kill robot, etc.) (only update if change (turn was made))
        if player.xvel != 0 or player.yvel != 0:
            display(screen, room, entities)


        
        #ENTITY MOVEMENT CONTROL
        for e in entities:
            pass
            
            

                







