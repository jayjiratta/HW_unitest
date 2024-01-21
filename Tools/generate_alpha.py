import random
import string

def generate_random_letters(num_letters):
    if 2 <= num_letters <= 10000:
        letters = ''.join(random.choices(string.ascii_letters, k=num_letters))
        return letters.lower()
    else:
        return "Number of letters must be between 2 and 10000."


num_letters_input = int(input("Enter the number of letters (2-10000): "))

result = generate_random_letters(num_letters_input)
print(result)
