#Question 1

class Animals():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.voice = []

    def ShowName(self):
        print("Hello world my name is:", self.name)
    def ShowColor(self):
        print("The color of my skin is:", self.color)
    def addVoice(self, voice):
        self.voice.append(voice)
        print("I can speak with people like:", voice)
    def info(self):
        print("To sum up, my name is {} and the color of myskin is {}".format(self.name, self.color))
        print("I know some words like:")
        for i in self.voice:
            print(i)
Animal1=Animals("Cow", "black")
Animal1.ShowName()
Animal1.ShowColor()
Animal1.addVoice("Mööööö")
Animal1.addVoice("Hhhmmmmöööööö")
Animal1.info()


class Dogs():
    def __init__(self, name, number_of_leg):
        self.name = name
        self.number_of_leg = number_of_leg
        self.voice = []

    def ShowName(self):
        print("Hello world my name is:", self.name)
    def ShowNumberOfLeg(self):
        print("The number of my legs are:", self.number_of_leg)
    def addVoice(self, voice):
        self.voice.append(voice)
        print("I can speak with people like:", voice)
    def info(self):
        print("To sum up, my name is {} and I have {} legs".format(self.name, self.number_of_leg))
        print("I know some words like:")
        for i in self.voice:
            print(i)
Dog1=Dogs("Çomar", 4)
Dog1.ShowName()
Dog1.ShowNumberOfLeg()
Dog1.addVoice("Howww, Hıırrr")
Dog1.info()

class Cats():
    def __init__(self, name, number_of_leg):
        self.name = name
        self.number_of_leg = number_of_leg
        self.voice = []

    def ShowName(self):
        print("Hello world my name is:", self.name)
    def ShowNumberOfLeg(self):
        print("The number of my legs are:", self.number_of_leg)
    def addVoice(self, voice):
        self.voice.append(voice)
        print("I can speak with people like:", voice)
    def info(self):
        print("To sum up, my name is {} and I have {} legs".format(self.name, self.number_of_leg))
        print("I know some words like:")
        for i in self.voice:
            print(i)
Cat1=Cats("Fıstık", 4)
Cat1.ShowName()
Cat1.ShowNumberOfLeg()
Cat1.addVoice("Mııırrrrrrr, Miyavvv")
Cat1.info()
