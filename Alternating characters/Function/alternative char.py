def alternatingCharacters(s):
    return sum(1 for c1, c2 in zip(s, s[1:]) if c1 == c2)


q = int(input().strip())
for q_itr in range(q):
    s = input()
    result = alternatingCharacters(s)
