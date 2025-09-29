class Animal:

    count = 0

    def __init__(self, name='dog'):
        self.name = name
        Animal.count += 1
        print(f"Creating an animal named {self.name}")

    def showingGender(self, gender="man"):
        return f"The {self.name} is {gender}"
    
    @classmethod
    def counting(cls):
        if Animal.count == 1:
           Animal.count += 2
           print(f"There are {Animal.count} Animals created so far")

    def leg(self, leg):
        self.leg = leg

valid_animals = ["dog", "cat", "bird"]
valid_genders = ["man", "woman", "unknown"]


while True:
    animalName = input("Enter the animal name: ".strip().lower())
    if animalName in valid_animals:
        break
    else:
        print(f"Invalid animal name. Please choose from {valid_animals}.")

animal = Animal(animalName);
print(f"Animal created: {animal.name}")

moreAt = Animal.z = 10

while True:
    animalGender = input("Enter the animal gender: ".strip().lower())
    if animalGender in valid_genders:
        break
    else:
        print(f"Invalid gender. Try again. Please choose from {valid_genders}.")

print(animal.showingGender(animalGender) + f" and has {moreAt} legs")

Animal.counting();


class adding:
    def __init__(self):
        self.words = {}

    def add(self, count, word):
        if word in self.words:
            self.words[word] += 1
        else:
            self.words[word] = 1

    def show(self):
        return self.words
    
my_words = adding()

my_words.add("apple")
my_words.add("banana")
my_words.add("apple")

print(my_words.show())  # {'apple': 2, 'banana': 1}