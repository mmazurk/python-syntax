def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    returnValue = False;
    for i in nums:
        if i == 7: 
            returnValue = True;
            return returnValue;
    return returnValue;
   

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

