def gridChallenge(grid):
    # Sort each string in the grid lexicographically
    orderedGrid = [sorted(x) for x in grid]
    print(orderedGrid)
    
    # Iterate through each character position in the sorted grid
    for i, string in enumerate(orderedGrid):
        # Check if the current position is not equal to the length of the string
        if (i) != len(string):
            # Create a new string by taking characters at the current position from each string in the grid
            newString = ''.join([x[i] for x in orderedGrid])
            
            # Check if the new string is not equal to its lexicographical sorted version
            if newString != ''.join(sorted(newString)):
                return 'NO'  # If not, return 'NO'
    
    # If all conditions are satisfied, return 'YES'
    return 'YES'

                
t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = gridChallenge(grid)
    print(result)
