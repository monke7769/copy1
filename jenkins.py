import random

count = 0
for i in range(50):
    n = random.randint(1,10)
    if n > 8:
        count += 1
print(count)