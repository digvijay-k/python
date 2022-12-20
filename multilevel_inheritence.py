class move_character:

    def move_left(self):
        print("move one step left")
    def move_right(self):
        print("move one step right")

class jump_character(move_character):

    def jump(self):
        print("jump")
    def duck(self):
        print("duck")

class noddy(jump_character):
    # print("noddy" , end = " ")
    def duck(self):
        print("NODDY duck")
    def move_right(self):
        print("NODDY moved right 1 step")
    # pass

noddy1  = noddy()

noddy1.jump()
noddy1.duck()         # method override
noddy1.move_left()
noddy1.move_right()   # method override
print(noddy.mro())



