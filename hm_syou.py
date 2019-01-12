class person(object):
    def __init__(self):
        self.name = "guo"
        self.__age = 25
    def __run(self):
        print("我爱你")
    def eat(self):
        self.__run()
        print(self.__age)
guo = person()
print(guo.name
      )
guo.eat()
print(guo._person__age)
