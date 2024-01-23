# def lencheck(lst):
#     for_name = '_'.join(str(len(s)) for s in lst)
#     return for_name

# user = input("list: ")
# print(lencheck(eval(user)))

def l(word) :
    return len(word)

user = input("word")
print(l(user))
