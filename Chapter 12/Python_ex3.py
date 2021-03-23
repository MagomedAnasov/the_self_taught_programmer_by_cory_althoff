class Triangle():
    def __init__(self,b,h):
        """S=1?2​⋅a⋅b⋅sin(α), где a, b — стороны треугольника, α — угол между ними."""
        self.base = b
        self.height = h

    def area(self):
        return self.height * self.base / 2
triangle = Triangle(20,15)
print(triangle.area())