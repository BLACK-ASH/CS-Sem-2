# Linear Search

list = [19,2,33,34,45,423,46,2354,64,35,34,567,234,42,5,567,456,45,6]

def linearSearch(list,key):
    for e in list:
        if e == key:
            return True
    return False

# Test
print(list)
print("33 In List : ",linearSearch(list,33))
print("34 In List : ",linearSearch(list,34))
print("44 In List : ",linearSearch(list,44))


