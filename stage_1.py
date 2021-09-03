class Main:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "hello world"
    
    def __str__(self):
        retur self.__repr__()

class A:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "hello world"

    def __str__(self):
        return self.__repr__()
main = Main()
a = A()
print(main)
print(a)
