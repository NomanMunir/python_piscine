from S1E7 import Baratheon, Lannister

# Test Baratheon
robert = Baratheon("Robert")
print(robert.__dict__)
print(robert)
print(repr(robert))

print("---")

# Test Lannister
cersei = Lannister("Cersei")
print(cersei.__dict__)
print(cersei)
print(repr(cersei))

print("---")

# Test class method to create Lannister from Baratheon
jaime = Baratheon.create_lannister("Jaime")
print(jaime.__dict__)
print(jaime)
