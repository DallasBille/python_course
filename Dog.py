import moduleexample as m
class Dog():

    # The two underscores indicate special class methods
    # initaialization
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

        # string representation of object
    def __str__(self):
        return "Breed: {}, Name: {}, Age: {}".format(self.breed, self.name, self.age)


newDog = Dog("collie", "Rusty", 14)

print(newDog)
print(m.module_function())
# Rusty
