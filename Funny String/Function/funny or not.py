def funnyString(s):
    list_1 = []
    list_2 = []
    for i in s :
        ascii = ord(i)
        list_1.append(ascii)
    list_2 = list(reversed(list_1))
    return list_1 ,list_2

def list_check(list_1, list_2):
    for i in range(len(list_1) - 1):
        if abs(list_1[i] - list_1[i + 1]) != abs(list_2[i] - list_2[i + 1]):
            return "Not Funny"
    
    return "Funny"


q = int(input().strip())
for q_itr in range(q):
    s = input() 
    list_1, list_2 = funnyString(s)
    result = list_check(list_1, list_2)
    print(result)
