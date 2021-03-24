class Square():
    def __init__(self,s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
        self.s1 += new_size
square = Square(3)
print(square.s1)

square.change_size(200)
print(square.s1)