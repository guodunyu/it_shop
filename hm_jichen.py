class animal(object):
    def run(self):
        print("跑")
    def __eat(self):
        print("吃")

    def love(self):
        print("爱")
class cat(animal):
    def run(self):
        print("用力炮")
        super().run()


tom = cat()
tom.__eat

