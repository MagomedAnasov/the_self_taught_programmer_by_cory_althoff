class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("""{} on {} 
        """.format(self.width, self.length))
class Square(Shape):
    def area(self):
        return self.width * self.length
square = Square(20,20)
print(square.area())