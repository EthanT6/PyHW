#Classes

class myClass():
    def method1(self):
        print("myClass method1")
    def method2(self, someString):
        print("myClass method2 " + someString)

class my2ndClass():
    def method1(self):
        print("my2ndClass method1")
    def method2(self, someString):
        print("my2ndClass method2 " )

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = my2ndClass()
    c2.method1()
    c2.method2("This is a string")

if __name__ == "__main__":
    main()

#Very Classy~