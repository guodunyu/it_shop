class cat(object):
    def eat(self):
        print("小猫喝水")
    def drink(self):
        print("小猫喝水")
xiaomao = cat()
xiaomao.eat()
xiaomao.drink()
print(xiaomao)
tom = cat()
print(tom)
tom.name = "汤姆"
print(tom.name)