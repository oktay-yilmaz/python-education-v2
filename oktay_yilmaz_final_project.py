Employee_language_list={}
Manager_language_list={}
class Employees():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.language = []
    def addLanguage(self,new_lang):
        self.language.append(new_lang)
        Employee_language_list[self.name] = self.language

class Managers():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.language = []
    def addLanguage(self,new_lang):
        self.language.append(new_lang)
        Manager_language_list[self.name]=self.language

Employee1=Employees("Ali", 28)
Employee1.addLanguage("English")
Employee1.addLanguage("Turkish")

Employee2=Employees("Ahmet", 30)
Employee2.addLanguage("English")
Employee2.addLanguage("French")

Employee3=Employees("Kemal", 25)
Employee3.addLanguage("Turkish")

Manager1=Managers("Mehmet", 40)
Manager1.addLanguage("English")
Manager1.addLanguage("Turkish")

Manager2=Managers("Fatih", 35)
Manager2.addLanguage("Spanish")
Manager2.addLanguage("Turkish")

Manager3=Managers("Emre", 37)
Manager3.addLanguage("Spanish")

for i,j in Employee_language_list.items():
    print("Employee",i,"can speak:",j)

for i,j in Manager_language_list.items():
    print("Manager",i,"can speak:",j)