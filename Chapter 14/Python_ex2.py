class Square():

    def __init__(self, s1):
        self.s1 = s1

    def __repr__(self):
        return "{} on {} on {} on {}".format(self.s1, self.s1, self.s1, self.s1)

square = Square(29)
print(square)
