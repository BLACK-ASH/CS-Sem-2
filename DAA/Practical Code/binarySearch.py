# Binary Search

list = [2, 5, 6, 19, 33, 34, 34, 35, 42, 45, 45, 46, 64, 234, 423, 456, 567, 567, 2354]

def binarySearch(list,key):
    start = 0
    end = len(list)-1

    while end >= start:
        mid = int((start + end)/2)

        if list[mid] == key:
            return True
        elif list[mid] > key:
            end = mid - 1
        else :
            start = mid + 1

    return False

# Test
print(list)
print("33 In List : ",binarySearch(list,33))
print("34 In List : ",binarySearch(list,34))
print("44 In List : ",binarySearch(list,44))       
