#Google Question
#Given an array, return the first recurring character
#Example1 : array = [2,1,4,2,6,5,1,4]
#It should return 2

array = [2,1,4,1,5,2,6]

def rcr(array):
    dictionary = {}
    for item in array:
        if item in dictionary:
            return item
        else:
            dictionary[item] = True
    return None

print(rcr(array))