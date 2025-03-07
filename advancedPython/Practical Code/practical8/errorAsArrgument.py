def Temp_convert(a):
    try :
        return int(a)
    except ValueError as Arg :
        print("The argument does not Contain numbers \n" , Arg)
