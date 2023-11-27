import random
class Hat:

    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)



Hat.sort("Harry Potter")