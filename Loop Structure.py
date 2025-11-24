import random

total = 0
for x in range(1, 101):
    total += x
print(total)

total2 = 0
for x in range(1, 101, 2):
    total2 += x
print(total2)

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    guess = int(input("please enter a number between 1 and 100: "))
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
    else:
        print("you got it in " + str(counter) + " tries")
        break
print("the answer is " + str(answer) + ", you got it in " + str(counter) + " tries")


for i in range(1, 10):
    for j in range(1, 10):
        print(str(i) + "*" + str(j) + "=" + str(i * j))
    print("\n")
