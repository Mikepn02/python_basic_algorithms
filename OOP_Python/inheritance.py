import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def getPerimeter(self):
        perm =  2 * math.pi * self.radius
        return perm
    def getArea(self):
        area = math.pi * self.radius ** 2
        return area

radius = float(input("Input the radius of the circle: "))
circle = Circle(radius)
area = circle.getArea()
perimeter = circle.getPerimeter()

print(f"The perimeter of circle is: {perimeter}")
print(f"The area of circle is: {area}")