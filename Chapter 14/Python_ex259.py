class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("""{} on {}
        """.format(self.width, self.length))
rectangle = Rectangle(20,25)
rectangle.print_size()