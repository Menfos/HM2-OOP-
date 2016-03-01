class Lonely(object):
    counter = 0
    def __new__(cls, name):
        cls.counter+=1
        if (cls.counter==1):
            return super(Lonely,cls).__new__(cls)
        else:
            return None
    def __init__(self,name):
        self.name = name
    def __del__(self):
        Lonely.counter-=1
        print("Obj {0} deleated".format(self.name))

    def useful_method(self):
        print ("Ive been called with name {0}".format(self.name))

obj1 = Lonely("Jack")
obj2 = Lonely("Sparrow")
obj1.useful_method()
obj2.useful_method()