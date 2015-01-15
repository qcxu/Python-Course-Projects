__author__ = 'QiongchengXu'

import random

random_number = random.randint(0, 100)
print random_number
if random_number > 50:
    print("Too high")
else:
    print("Too low")