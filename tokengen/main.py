import random
import string
from unittest import result

total = int(input("amount to generate: "))
gen = 0
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy.z.0123456789"

for i in range(total):
    token = "".join(random.choices(char, k=90))
    gen = gen + 1
    print(f'{gen}. {token}')

output = open("output.txt", "a")
output.write(result)