class p_class:                     #parent class
    c  = 8
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def p_method(self):
        c = self.age
        return c

class c_class(p_class):   #child class
    pass

o1 = c_class("dig", 39)

print("accessing instance variable of parent class from child class", o1.name)
print("accessing age of parent class method from child class", o1.p_method())
print("class variable", o1.c)
