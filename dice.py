import random

class Dice:
    def __init__(self):
        self.sides = 6

    def roll(self):
        return random.randint(1, self.sides)

dice = Dice()
print(f"Rolling the dice: {dice.roll()}")


# import random

# class Dice:
#     def roll(self):
#         return random.randint(1, 6)


# dice = Dice()
# print(f"Rolling the dice: {dice.roll()}")


class Dice:
    def __init__(self, sides):
        self.side = sides