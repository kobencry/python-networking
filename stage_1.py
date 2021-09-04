class Main:
    def __init__(self):
        pass

    def __repr__(self):
        return "hello world"
   
    def __str__(self):
        return self.__repr__()

if __name__=='__main__':
    main = Main()
    print(main)
