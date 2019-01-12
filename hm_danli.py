class person(object):
    abcd = None
    init_flog = False
    def __new__(cls, *args, **kwargs):
        if cls.abcd is None:
            cls.abcd = super().__new__(cls)
        return cls.abcd
    def __init__(self):
        if person.init_flog:
            return


a = person()
b = person()
print(a)
print(b)
