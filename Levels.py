from Game_Classes import *


#0 => empty     1 => platform     2 => ladder    3 => door

#0th element of ents is Player class instance




class Level():
    def __init__(self, room, ents):
        self.room = room
        self.entities = ents


 
test_room = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,3,0,2,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,2,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0],
    [1,0,0,0,2,1,1,1,1,2,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0],
    [1,0,0,0,3,0,0,0,0,2,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

test_ents = [Player(1, 8), Key(6, 4), Robot(7, 8, "R"), Robot(5,4,"R")]

test_level = Level(test_room, test_ents)




Levels = [test_level]
