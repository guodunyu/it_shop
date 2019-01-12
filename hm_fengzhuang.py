class person(object):
    def __init__(self,name,weight):
        self.name   = name
        self.weight = weight
    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1

    def __str__(self):
        return "%s的跑步之后体重为%.2f,吃饭以后体重为%.2f" % (self.name,self.weight,self.weight)

xiaoming = person("小明",75)
print(xiaoming)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)