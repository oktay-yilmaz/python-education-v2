#Using Inheritance
class Animals():
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Dogs(Animals):
    def __init__(self, name, color, voice):
        super().__init__(name, color)
        self.voice =voice
    def doginfo(self):
            print("Hello world! my name is:", self.name, ", the color of my skin is:", self.color, "and i know some words like:", self.voice)
Dog1=Dogs("Çomar", "White", "HowwwwwHoowww")
Dog1.doginfo()

class Cats(Animals):
    def __init__(self, name, color, voice):
        super().__init__(name, color)
        self.voice =voice
    def catinfo(self):
            print("Hello world! my name is:", self.name, ", the color of my skin is:", self.color, "and i know some words like:", self.voice)
Cat1=Cats("Fıstık", "black and white", "Miyavvvv")
Cat1.catinfo()
