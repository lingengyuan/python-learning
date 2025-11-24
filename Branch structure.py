##heron's formula
import math

def heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print("please enter the sides of the triangle")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and a + c > b and b + c > a:
    print("the heron's formula return is : " + str(heron(a, b, c)))
else:
    print("the sides you entered cannot form a triangle")
