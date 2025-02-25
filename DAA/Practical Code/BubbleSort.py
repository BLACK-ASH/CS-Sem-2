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
    print(list)

list = [19,2,33,34,45,423,46,2354,64,35,34,567,234,42,5,567,456,45,6]
bubbleSort(list)

