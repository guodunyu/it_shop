class person(object):
    def __init__(self):
        self.name = "小明"
        self.high = 175
    def run(self):
        self.high += 4
        # eturn
        # self.highr
        print(self.high)
    def eat(self):
        print("小明爱跑步")

xiaoming = person()
print(person)
print(xiaoming.name)
xiaoming.eat()

print(xiaoming.run())