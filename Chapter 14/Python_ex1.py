class Square():
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)
square1 = Square(20)
square2 = Square(5)

print(Square.square_list)