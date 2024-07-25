class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def make_sound(self):
    print("Generic animal sound")

  def eat(self):
    print("Animal is eating")

class Bird(Animal):
  def __init__(self, name, age, wingspan):
    super().__init__(name, age)
    self.wingspan = wingspan

  def make_sound(self):
    print("Tweet tweet!")

class Mammal(Animal):
  def __init__(self, name, age, fur_color):
    super().__init__(name, age)
    self.fur_color = fur_color

  def make_sound(self):
    print("Woof!")

class Reptile(Animal):
  def __init__(self, name, age, scales):
    super().__init__(name, age)
    self.scales = scales

  def make_sound(self):
    print("Hiss!")

def animal_sound(animals):
  for animal in animals:
    animal.make_sound()

class ZooKeeper:
  def __init__(self, name):
    self.name = name

  def feed_animal(self, animal):
    print(f"{self.name} кормит {animal.name}")
    animal.eat()

class Veterinarian:
  def __init__(self, name):
    self.name = name
  def heal_animal(self, animal):
    print(f"{self.name} лечит {animal.name}")

class Zoo:
  def __init__(self, name):
    self.name = name
    self.animals = []
    self.employees = []

  def add_animal(self, animal):
    self.animals.append(animal)
    print(f"{animal.name} добавлен в {self.name}")

  def add_employee(self, employee):
    self.employees.append(employee)
    print(f"{employee.name} добавлен в {self.name}")

my_zoo = Zoo("Central Zoo")

bird = Bird("Tweety", 2, 20)
mammal = Mammal("Sparky", 5, "brown")
reptile = Reptile("Slinky", 1, "green")

my_zoo.add_animal(bird)
my_zoo.add_animal(mammal)
my_zoo.add_animal(reptile)

zookeeper = ZooKeeper("Bob")
veterinarian = Veterinarian("Alice")

my_zoo.add_employee(zookeeper)
my_zoo.add_employee(veterinarian)

animal_sound(my_zoo.animals)

zookeeper.feed_animal(bird)
veterinarian.heal_animal(mammal)
