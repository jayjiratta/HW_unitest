def caesarCipher(s, k):
    result = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                result += chr((ord(i) - ord('a') + k) % 26 + ord('a'))
            elif i.isupper():
                result += chr((ord(i) - ord('A') + k) % 26 + ord('A'))
        else:
            result += i
    return result

n = int(input().strip())
s = input()
k = int(input().strip())
result = caesarCipher(s, k)
print(result)