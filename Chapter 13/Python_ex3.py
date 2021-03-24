class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print('I am a figure')
class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

class Square(Shape):
    def __init__(self,s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4

rectangle = Rectangle(20,15)
square = Square(4)

rectangle.what_am_i()
square.what_am_i()