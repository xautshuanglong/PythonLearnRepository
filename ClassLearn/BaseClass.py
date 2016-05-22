# BaseClass.py

class BaseClass:
    def __init__(self,id,name):
        print("__init__ from "+__name__)
        self.id = id
        self.name = name

    def toString(self):
        print(self.id,self.name)

    def testFunc(self):
        print(self.name,"__BaseClass")
