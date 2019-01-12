class person(object):
    def __init__(self):
        self.name = "郭敦宇"
        self.age = 26
        self.high = 175
    def __str__(self):
        return "%s的年龄是%d，身高是%d" % (self.name , self.age , self.high)
    def __del__(self):
        print("hello world")
guo = person()

print(guo)
del guo
print("*" * 50)