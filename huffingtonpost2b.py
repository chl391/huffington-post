def longestRange(array):
    if len(array) == 0:
        print("The longest consecutive range is 0.")
    arraySet = set([])
    maximum = 1
    leftmost = array[0]
    #Create set based on array
    for i in array:
        arraySet.add(i)
    #Keep track of current leftmost and current longest range
    #Replace if necessary
    for i in array:
        left = i-1
        right = i+1
        currentMax = 1
        currentLeftmost = i
        while left in arraySet:
            currentMax=currentMax+1
            arraySet.remove(left)
            currentLeftmost = left
            left=left-1
        while right in arraySet:
            currentMax=currentMax+1
            arraySet.remove(right)
            right=right+1
        if maximum < currentMax:
            maximum = currentMax
            leftmost = currentLeftmost
    print("The longest conseuctive range is",maximum,"beginning with number",leftmost,end="")
    print(".")
longestRange([5,6,9,8,7,2,1,11])
