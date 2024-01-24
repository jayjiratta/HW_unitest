def gridChallenge(grid):
    orderedGrid = [sorted(x) for x in grid]
    
    for i, string in enumerate(orderedGrid):
        if i != len(string):
            newString = ''.join([x[i] for x in orderedGrid])

            if newString != ''.join(sorted(newString)):
                return 'NO'
    
    return 'YES'

def all(list_q) :   
    lst = []
    for i in list_q:
        lines = i.split('\n')  
        if lines[0].isdigit():
            t = int(lines[0])

            grid = [line for line in lines[1:] if line]
            result = gridChallenge(grid)
            lst.append(result)
    return lst

    