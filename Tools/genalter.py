import random

def generate_random_string(length):
    random_string = ''.join(random.choice('AB') for _ in range(length))
    return random_string

n = int(input(""))
for i in range(n+1) :
    length = int(input(""))
    random_uppercase_string = generate_random_string(length)
    print(random_uppercase_string)