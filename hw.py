class Dog:
    species = "Dog"
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
Golden_Retriever = Dog("Golden_Retriever", 7)
Bulldog = Dog("Bulldog", 5)
print("Golden Retriever is a type of {}".format(Golden_Retriever.species))
print("Bulldog is also a type of {}".format(Bulldog.species))
print("{} is {} years old".format(Golden_Retriever.breed, Golden_Retriever.age))
print("{} is {} years old".format(Bulldog.breed, Bulldog.age))