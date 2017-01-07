import random

a = []
for x in range(1, random.randint(1, 100)):
    a.append(random.randint(1, 100))

b = []
for x in range(1, random.randint(1, 100)):
    b.append(random.randint(1, 100))

overlap = []

for x in a:
    if x in b:
        if x in overlap:
            continue
        else:
            overlap.append(x)

print("Random list 1: \n", a, "\n")
print("Random list 2: \n", b)

print("\nThe elements in common are:\n", overlap)
        
        
