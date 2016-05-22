class MyClass:
    def __init__(self,id,name):
        print("inside ",__name__)
        self.id = id
        self.name = name

    def toString(self):
        print(self.id,"-->",self.name)
