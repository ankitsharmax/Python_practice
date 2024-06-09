'''
variable: public variable/member::::::: ACCESSIBLE ANYWHERE IN THE CLASS
_variable: protected variable/member:::::: ACCESSIBLE WITHIN THE CLASS AND ITS SUBCLASSES
__variable: private variable/member:::::: ACCESSIBLE WITHIN THE CLASS
'''

class Encapsulation:
    def __init__(self,fname,lname,fullname):
        self.fname = fname
        self._lname = lname
        self.__fullname = fullname

encapsulation = Encapsulation("Ankit", "Sharma", "Ankit Sharma")
print("Public fname: ",encapsulation.fname)
print("Protected lname: ",encapsulation._lname)
print("Private fullname: ",encapsulation._Encapsulation__fullname)

