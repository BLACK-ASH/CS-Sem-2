class Static:
    # Creating Static Method
    @staticmethod
    def call():
        return "I Am Static Method"

# Creating Object
obj = Static()

# Calling
print(obj.call())
print(Static.call())