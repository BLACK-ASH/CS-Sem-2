# Insertion Sort    
def insertionSort(list):
    for e in list:
        i = list.index(e)
        while i < len(list)-1:
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1], list[i]
            else:
                break
            i-=1
    return list    

# Test Case
list = [1,2,39,5,32,3,3,21,43,5,2]
print("Unsorted List : ",list)
print("Sorted List",insertionSort(list))
