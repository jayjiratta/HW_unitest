import random

def generate_random_string(length,min,max):
    if length < 2 or length > 10000:
        return "Invalid length. Please enter a value between 2 and 10000."
    else:
        random_numbers = [random.randint(min, max) for _ in range(length)]
        random_string = ' '.join(map(str, random_numbers))
        return random_string

user = int(input("num: "))
min = int(input("min: "))
max = int(input("max: "))
random_string_result = generate_random_string(user,min,max)
print(random_string_result)
