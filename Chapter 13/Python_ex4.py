class Horse():
    def __init__(self, name):
        self.name = name
class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse
horse = Horse('Stanley')
rider = Rider('Mick', horse)

print(rider.horse.name)