class cat(object):
    def __init__(self,name,high):
        self.name = name
        self.high = high
    #__init__ 是创建对象时候自动会启用的代码

tom = cat("汤姆",185)
print(tom.name)
print(tom.high)