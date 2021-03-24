class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("""{} on {}
        """.format(self.width, self.length))
class Square(Shape):
    pass
square = Square(20,20)
square.print_size()