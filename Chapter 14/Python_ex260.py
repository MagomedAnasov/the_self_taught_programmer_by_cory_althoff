class Rectangle():
    recs = []
    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.recs.append((self.width, self.length))

    def print_size(self):
        print("""{} on {}
        """.format(self.width, self.length))
r1 = Rectangle(10,15)
r2 = Rectangle(20,15)
r3 = Rectangle(5,10)

print(Rectangle.recs)
