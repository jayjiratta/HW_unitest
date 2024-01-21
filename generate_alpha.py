import random
import string

def generate_random_letters(num_letters,min,max):
    if min <= num_letters <= max:
        letters = ''.join(random.choices(string.ascii_letters, k=num_letters))
        return letters
    else:
        return "Number of letters must be between 2 and 10000."

num_letters_input = int(input("Enter the number of letters (2-10000): "))

min = int(input("min: "))
max = int(input("max: "))

result = generate_random_letters(num_letters_input)
print(result)
