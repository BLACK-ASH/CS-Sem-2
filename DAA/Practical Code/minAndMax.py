# By Using Loop
def findMinAndMax1(list):
    min  = list[0]
    max = list[0]

    for num in list:
        if num < min:
            min = num
        if num > max:
            max = num

    return min,max

# By Using Divide And Conquer
import sys
def findMinAndMax(list,first,last,min = sys.maxsize,max = -sys.maxsize):
    # Handling Base Case
    # Case 1 : If The Lenght Of The List Is One
    if first == last:
        if list[first]> max:
            max = list[first]
        if list[first]<min:
            min = list[first]
        return min,max
    
    # Case 1 : If The Lenght Of The List Is One
    if 1 == first - last:
        if list[first] > list[last]:
            if list[first] > max:
                max = list[first]
        if list[last] > list[first]:
            if list[last] > max:
                max = list[last]
        return min,max

    # Dividing The List
    # Calculating The Midpoint Of The List
    mid = (first + last) // 2

    # Handling Left Side
    min,max = findMinAndMax(list,first,mid,min,max)

    # Handling Right Side
    min,max = findMinAndMax(list,mid+1,last,min,max)

    return min,max

list = [1,2,345,2,352,3,235,45,3,432]
print("----- Using For Loop -----")
print(findMinAndMax1(list))
print("----- Using Divide And Conquer -----")
print(findMinAndMax(list,0,len(list)-1))

    
