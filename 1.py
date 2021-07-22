def helloWorld(i):
    if((i % 3 == 0) and (i % 5 == 0)):
        print("Hello World")
    elif(i % 5 == 0):
        print("World")
    elif(i % 3 == 0):
        print("Hello")


def test_HelloWorld():
    helloWorld(15)
    helloWorld(10)
    helloWorld(9)


test_HelloWorld()
