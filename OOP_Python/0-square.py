class Square:
    def __init__(self,size=0):
        self.size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        
        if(size < 0) :
            raise ValueError("size must be >=0 ")
        
    def getPerimeter(self):
        self.perm=  4 * self.size
        return self.perm
    def getArea(self):
        self.area =  self.size * self.size
        return self.area
square =  Square(12)
perimeter = square.getPerimeter()
area = square.getArea()
print(f"The perimeter of square is: {perimeter}")
print(f"The area of square is: {area}")