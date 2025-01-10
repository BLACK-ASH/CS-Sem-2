# Declaring Global Variable
num = 23

# Changing Local Variable Inside A Function
def change():
    # Accesing The Global Variable
    global num
    num = num

    # Change
    num = num + 10

    # Printing The Output
    print(num)

# Using Function
change()
