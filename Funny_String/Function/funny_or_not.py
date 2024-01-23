list_1_question = ['acxz','bcxz']
list_1_ans = ['Funny','Not Funny']

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

def all(list) :
    lst = []
    for i in list :
        x , y = funnyString(i)
        z = list_check(x,y)
        lst.append(z)
    return lst

# user_lst = list_1_question
# my_list = eval(user_lst)
# a = all(my_list)
# print(a)





