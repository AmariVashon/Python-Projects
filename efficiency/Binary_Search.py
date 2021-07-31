import random as rd

nums = [rd.randint(0, 20) for i in range(10)]
print(nums)

def binarySearch(aList, num):
    aList.sort()
    mid = len(aList)//2
    
    if len(aList) == 1:
        return True if aList[mid] == num else False
    elif aList[mid] == num:
        return True
    else:
        if aList[mid] < num:
            return binarySearch(aList[mid+1:], num)
        else:
            return binarySearch(aList[:mid], num)

binarySearch(nums, 5)
