class Shape():
    def __init__(self,w,l):
        self.width = w
        self.length = l
    def print_size(self):
        print("""{} on {}
        """.format(self.width, self.length))
shape = Shape(20,25)
shape.print_size()