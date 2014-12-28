def longestRange(array):
    if len(array) == 0:
        print("The longest consecutive range is 0.")
    arraySet = set([])
    maximum = 1
    leftmost = array[0]
    for i in array:
        arraySet.add(i)
    for i in array:
        left = i-1
        right = i+1
        count = 1
        currentLeftmost = i
        while left in arraySet:
            count=count+1
            arraySet.remove(left)
            currentLeftmost = left
            left=left-1
        while right in arraySet:
            count=count+1
            arraySet.remove(right)
            right=right+1
        if maximum < count:
            maximum = count
            leftmost = currentLeftmost
    print("The longest conseuctive range is",maximum,"beginning with number",leftmost,end="")
    print(".")
longestRange([5,6,9,8,7,2,1,11])
