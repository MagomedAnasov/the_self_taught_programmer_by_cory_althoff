class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class Person():
    def __init__(self, name, id):
        self.name = name
        self.id = id
mick = Person('Mick Jagger',2)
dog = Dog('Stanley', 'bulldog', mick)

print(dog.owner.id)