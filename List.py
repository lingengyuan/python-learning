import random
items = [1, 2, 3, 4, 5]
print(items[0])
print(items[1])
items2 = ["hello", "world"]
print(items2[0])
print(items2[1])
items3 = items + items2
print(items3)
items4 = items3 * 2
print(items4)
items5 = [1, 2, 3, 4, 5]
size = len(items5)
print(size)
items5.append(6)
print(items5)
items5.insert(0, 0)
print(items5)
items5.remove(3)
print(items5)
items5.pop()
print(items5)
print(items5.index(4))
items5.sort()
print(items5)
items5.reverse()
print(items5)
for item in items5:
    print(item)
for index, item in enumerate(items5):
    print(index, item)

counter = [0] * 6
for _ in range(600):
    face = random.randint(1, 6)
    counter[face - 1] += 1
for face in range(1, 7):
    print(f'{face} Points appeared {counter[face - 1]} counter times')
