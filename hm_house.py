class jiaju(object):
    def __init__(self, name, area) :
        self.name = name
        self.area = area
    def __str__(self):

        return "%s占地面积%d" % (self.name,self.area)

a = jiaju("衣柜",2 )
b = jiaju("床",4)
c = jiaju("电视",9)

print(a)
print(b)
print(c)
class house(object):
    def __init__(self):
        self.type = "三室一厅"
        self.titlearea = 80
        self.list = []
        self.ccc = 80
    def tianjia(self,bian):
        if self.titlearea >= bian.area:
            self.list.append(bian.name)
            self.ccc = self.titlearea - bian.area
        else:
            print("剩余面积不够")
    def __str__(self):
        return "房子户型为%s,面积为%d[剩余面积%d],拥有家具%s" % (self.type,self.titlearea,self.ccc,self.list)

tomhouse = house()
tomhouse.tianjia(a)
tomhouse.tianjia(b)
tomhouse.tianjia(c)

print(tomhouse)
