def alternate(s):
    unique_chars = sorted(set(s))
    max_length = 0

    for i in range(len(unique_chars) - 1):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]

            filtered_string = ''.join([c for c in s if c == char1 or c == char2])

            valid = all(filtered_string[k] != filtered_string[k + 1] for k in range(len(filtered_string) - 1))

            if valid:
                max_length = max(max_length, len(filtered_string))

    return max_length

l = int(input().strip())
s = input()
result = alternate(s)
print(result)
