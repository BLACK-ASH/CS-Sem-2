class NotEqualError(Exception):
    pass

n1 = 10
n2 = 9
try :
    if n1!= n2 :
        raise NotEqualError
    else:
        print("Numbers are Equal")

except NotEqualError:
    print("Numbers are not equal")
