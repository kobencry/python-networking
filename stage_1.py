class Main:
    def __init__(self):
        print("hello world")
     
    def __repr__(self):
        return "hello wrold")
    
    def __str__(self):
        return self.__repr__()
main = Main()
