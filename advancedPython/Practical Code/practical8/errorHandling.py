import sys
while True:
    try:
        n1 = int(input("Enter A Number 1 : "))
        n2 = int(input("Enter A Number 2 : "))
        print("The Divison Is : ",n1/n2)
    except :
        print("There Is An Error",sys.exc_info()[0])
