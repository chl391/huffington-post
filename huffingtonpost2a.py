def getMissing(array):
    string = ""
    lowestNum = 0
    highestNum = 99

    #Handle when array has length 0 or 1
    if len(array) == 0:
        string += str(lowestNum)+"-"+str(highestNum)
    elif len(array) == 1:
        if array[0] == lowestNum:
            string += str(lowestNum+1)+'-'+str(highestNum)
        elif array[0] == highestNum:
            string += str(lowestNum)+'-'+str(highestNum-1)
        elif array[0] == highestNum-1:
            string += str(lowestNum)+'-'+str(array[0]-1)+','+str(highestNum)
        else:
            string += str(lowestNum)+'-'+str(array[0]-1)+','+str(array[0]+1)+'-'+str(highestNum)
    else:
        #Construct beginning of string depending on first number in array
        if array[0] != lowestNum:
            if array[0] == lowestNum + 1:
                string += str(lowestNum)+','
            else:
                string += str(lowestNum)+"-"+str(array[0]-1)+','
        #Loop through remainder of array
        for i in range(0,len(array)):
            #Construct end of string depending on last number in array
            if i+1 == len(array):
                if array[i] == highestNum-1:
                    string += str(highestNum)
                elif array[i] != highestNum:
                    string += str(array[i]+1)+'-'+str(highestNum)
                elif array[i] == highestNum:
                    string = string.replace(' ', '')[:-1].upper()
                else:
                    break
            elif array[i+1]-array[i] == 1:
                continue
            elif array[i+1]-array[i] == 2:
                if array[i]+1 == highestNum-1:
                    string += str(array[i]+1)
                else:
                    string += str(array[i]+1)+','
            else:
                string += str(array[i]+1)+'-'+str(array[i+1]-1)+','
    return string

array = [0,1, 2, 50, 52, 75]
print(getMissing(array))
