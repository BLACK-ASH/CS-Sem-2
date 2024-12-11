class ClassMethod:
    @classmethod
    def call(cls):
        return "I Am Class Method Example"

obj = ClassMethod()

print(obj.call())
