class emp:

    def __init__(self, fname, profile, email):
        self.fname = fname
        self.profile = profile
        self.email = email

    def greet(self,a):
        print("Hi {} welcome to the {} team".format(self.fname, self.profile))
        print(a)
emp1 = emp("karan","tech","karan@gmail.com")

# print(emp1.fname)
# emp1.greet('c')

class rectangle:

    def __init__(self,lenth,breadth):
        self.l = lenth
        self.b = breadth

    def cal_area(self):
        print("area of rectangle is", self.l * self.b, "unit^3")

    def cal_perimeter(self):
        perimeter = 2 * (self.l + self.b)
        print("perimeter of rectangle is" , perimeter, "unit^2")

rect1 = rectangle(3,4)
# rect1.cal_perimeter()
# rect1.cal_area()

###############################
class interest:

    roi = 0.08  # class variable
    def __init__(self, amount):
        self.amount = amount    # instance/object variable

    def cal_interest(self):
        print(interest.roi)
        print("principle amount", self.amount)
        print("total interest", self.amount * interest.roi)

p1 = interest(30000)
interest.roi = 0.09
p1.cal_interest()



