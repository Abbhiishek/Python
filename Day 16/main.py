# Object oriented programming
# Classes and objects
# Inheritance
# Polymorphism
# Abstraction
# Encapsulation
# Data hiding
"""
Object-oriented programming is a programming paradigm that uses objects and their interactions to model real world situations.


In OOP what is the name of the blueprint for creating objects?

=> Class

Question 3:
my_toyota = Car()
my_fiat = Car()
What word would you use to describe what's inside my_toyota and my_fiat?

=> objects

"""


class Person:
    def __init__(self, name, age):
        """
        This method initializes the attributes of the class.
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def introduce(self):
        """
        This method prints out the name and age of the person.
        """
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def get_older(self):
        """
        This method increases the age of the person by one.
        :return:
        """
        self.age += 1


class Student(Person):
    """

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old. I am in {self.grade} grade at {self.school}.")

    def get_older(self):
        self.age += 1

    """

    def __init__(self, name, age, grade, school):
        """
        Initializes the student class.
        :param name:
        :param age:
        :param grade:
        :param school:


        """
        super().__init__(name, age)
        self.grade = grade
        self.school = school

    def introduce(self):
        """
        Prints out the name and age of the student.
        :return:

        """
        print(f"Hi, my name is {self.name} and I am {self.age} years old. I am in {self.grade} grade at {self.school}.")

    def get_older(self):
        """
        Increases the age of the student by one.
        :return:
        """
        self.age += 1


# Use the above classes

# Create an instance of the Person class and call the introduce()
# method.

abhishek = Person("Abhishek Kushwaha", 19)
abhishek.introduce()
abhishek.get_older()
print("after the get older attribute")
abhishek.introduce()

# Create an instance of the Student class and call the introduce()

abhishek = Student("Abhishek Kushwaha", abhishek.age, "Btech Cse ", "Jis University")
abhishek.introduce()

abhishek.introduce()


# create a pokemon class

class Pokemon:
    def __init__(self, name, type, level):
        self.name = name
        self.type = type
        self.level = level

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.level} level {self.type} pokemon.")

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}")

    def attack(self, other_pokemon):
        print(f"{self.name} attacked {other_pokemon.name}")
        other_pokemon.level_up()
        print(f"{other_pokemon.name} has leveled up to level {other_pokemon.level}")

    def __str__(self):
        return f"{self.name} is a {self.type} pokemon"


# create a pokemon trainer class

class PokemonTrainer:
    def __init__(self, name, pokemons):
        self.name = name
        self.pokemons = pokemons

    def introduce(self):
        print(f"Hi, my name is {self.name} and I have {len(self.pokemons)} pokemon.")

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def remove_pokemon(self, pokemon):
        self.pokemons.remove(pokemon)

    def __str__(self):
        return f"{self.name} is a trainer"


# create a pokemon battle class

class PokemonBattle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2

    def start(self):
        print(f"{self.trainer1.name} is attacking {self.trainer2.name}")
        self.trainer1.pokemons[0].attack(self.trainer2.pokemons[0])
        print(f"{self.trainer2.name} is attacking {self.trainer1.name}")
        self.trainer2.pokemons[0].attack(self.trainer1.pokemons[0])


# create a pokemon trainer


abhishek = PokemonTrainer("Abhishek", [])
abhishek.add_pokemon(Pokemon("Pikachu", "Electric", 1))
abhishek.add_pokemon(Pokemon("Bulbasaur", "Grass", 1))
abhishek.add_pokemon(Pokemon("Charmander", "Fire", 1))
abhishek.add_pokemon(Pokemon("Squirtle", "Water", 1))

meow = PokemonTrainer("Muskaan Alam", [])
meow.add_pokemon(Pokemon("Pikachu", "Electric", 1))
meow.add_pokemon(Pokemon("Bulbasaur", "Grass", 1))
meow.add_pokemon(Pokemon("Charmander", "Fire", 1))
meow.add_pokemon(Pokemon("Squirtle", "Water", 1))

# create a pokemon battle


battle = PokemonBattle(abhishek, meow)
battle.start()
