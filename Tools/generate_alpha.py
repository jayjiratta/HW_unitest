import random
import string

def generate_random_letters(num_letters):
    if 1 <= num_letters <= 10000:
        letters = ''.join(random.choices(string.ascii_letters, k=num_letters))
        return letters.lower()
    else:
        return "Number of letters must be between 2 and 10000."

count = int(input("line"))
num_letters_input = int(input("long"))
for i in range(count) :
    result = generate_random_letters(num_letters_input)
    print(result)
