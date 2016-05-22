# DerivedClass.py

"""
import BaseClass

class DerivedClass(BaseClass.BaseClass):
    def __init__(self):
       print("DerivedClass")
"""

from BaseClass import BaseClass

class DerivedClass (BaseClass):
    def __init__(self,id,name):
        print("__init from "+__name__)
        BaseClass.__init__(self,id,name)

    def toString(self):
        print("toString: "+str(self.id)+"==>"+self.name)

    def newFunc(self):
        print("newFunc from ",__name__)
        print(str(self.id)+" --> "+self.name)
