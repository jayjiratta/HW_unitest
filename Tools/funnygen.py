import random

def generate_funny_string(length):
    funny_string = ""
    while True:
        # Generate a random string of the specified length
        test_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
        
        # Check if the reversed string meets the "Funny" criteria
        if is_funny(test_string):
            funny_string = test_string
            break

    return funny_string

def is_funny(test_string):
    for i in range(len(test_string) - 1):
        if abs(ord(test_string[i]) - ord(test_string[i + 1])) != abs(ord(test_string[-(i + 1)]) - ord(test_string[-(i + 2)])):
            return False
    return True

# Generate 5 funny strings of length 4 as an example
# for _ in range(5):
funny_result = generate_funny_string(15)
print(funny_result)
