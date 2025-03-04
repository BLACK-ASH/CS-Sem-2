# Selection Sort
def selectionSort(list):
    for i in range(len(list)):
        min = i
        for j in range (i+1,len(list)):
            if list[min] > list[j]:
                min=j
        list[min],list[i]=list[i],list[min]

    return list
        
# Test Case
list = [1,2,39,5,32,3,3,21,43,5,2]
print("Unsorted List : ",list)
print("Sorted List",selectionSort(list))
