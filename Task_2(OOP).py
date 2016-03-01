class Observable(object):
    description = {}
    def __init__(self,**kwargs):
        for key in kwargs:
            self.key = key
        self.description = kwargs
    def __repr__(self):
        return "Observable:{0}".format(self.description)
    def __getattr__(self, name):
        for key in self.description:
            if(name == key):
                print(self.description[key])
obj1 = Observable(name="max",exp= "2")
obj1.exp
print(obj1)