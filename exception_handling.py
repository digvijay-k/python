
try:
    x = int(input("enter numerator\n"))
    y = int(input("enter denominator\n"))
    if y == 0:
        raise Exception("denominator can't be zero")
    print(x/y)
except Exception as e:
    print(e)
    print("in except block")
else:
    print("in else block")
finally:
    print("in final block")