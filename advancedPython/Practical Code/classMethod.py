class ClassMethod:
    # Creating Class Method
    @classmethod
    def call(cls):
        return "I Am Class Method Example"

# Creating Object
obj = ClassMethod()

# Calling
print(obj.call())
