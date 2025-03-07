def Divide(x,y):
    try :
        result = x/y
    except ZeroDivisionError:
        print("Division by Zero")

    else :
        print("result is : ",result)

    finally:
        print("Final clause is executing ")

