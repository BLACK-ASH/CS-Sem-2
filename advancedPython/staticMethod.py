class Static:
    @staticmethod
    def call():
        return "I Am Static Method"

obj = Static()
print(obj.call())
