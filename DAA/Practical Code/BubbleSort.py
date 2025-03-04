# Bubble Sort

def swap(L,x,y):
    temp=L[x]
    L[x]=L[y]
    L[y]=temp

def bubbleSort(list):
    for i in range(len(list)):
        for k in range (len(list)-1,i,-1):
            if (list[k]<list[k-1]):
                swap(list,k,k-1)
                
    return list

# Test Case
list = [1,2,39,5,32,3,3,21,43,5,2]
print("Unsorted List : ",list)
print("Sorted List",bubbleSort(list))

