
def SayHello(name):
    print("I want to say hello with your, {0}".format(name))
    print("`````````````````````")


if __name__ == "__main__":
    print('***' * 10)
    name = input("Please input your name: ")
    SayHello(name=name)
    print("@@@" * 10)