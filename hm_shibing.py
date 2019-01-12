class gun(object):
    def __init__(self,model):
        self.model = model
        self.count = 0
    def fashe(self):
        if self.count > 0 :

            self.count -= 1
        else:
            print("没子弹了"
                  "")
    def add(self,count):
        self.count = count

AK47 = gun("ak47")
AK47.fashe()
AK47.add(55)


class solder(object):
    def __init__(self,name):
        self.name = name
        self.gun = None
    def fire(self):
        self.gun.fashe()
        print(self.gun.count)
sanduo = solder("sanduo")
sanduo.gun = AK47
print(sanduo.gun.model)
sanduo.fire()