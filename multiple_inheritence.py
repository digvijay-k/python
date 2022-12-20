class move_character:

    def move_left(self):
        print("move one step left")
    def move_right(self):
        print("move one step right")

class jump_character:

    def jump(self):
        print("jump")
    def duck(self):
        print("duck")

class noddy(move_character, jump_character):
    # print("noddy" , end = " ")
    def duck(self):
        print("noddy duck")
    def move_right(self):
        print("noddy moved right 1 step")
    # pass

noddy1  = noddy()

noddy1.jump()
noddy1.duck()         # method override
noddy1.move_left()
noddy1.move_right()   # method override

print(noddy.mro())

