def alternatingCharacters(s):
    return sum(1 for c1, c2 in zip(s, s[1:]) if c1 == c2)

def all(list) :
    lst = []
    for i in list :
        x = alternatingCharacters(i)
        lst.append(x)
    return lst
        