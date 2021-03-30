class Food:
     def __init__(self,fn,ft,fc,fp,fq):
          self.__foodName=fn
          self.__foodType=ft
          self.__foodCategory=fc
          self.__foodPrice=fp
          self.__foodQuantity=fq

     #getter and setter
     def getFName(self):
          return self.__foodName
     def setFName(self,fn):
          self.__foodName=fn

     def setFType(self,ftype):
          self.__foodType=ftype
     def getFType(self):
          return self.__foodType

     def setFCategory(self,fcat):
          self.__foodCategory=fcat
     def getFCategory(self):
          return self.__foodCategory

     def setFPrice(self,fp):
          self.__foodPrice=fp
     def getFPrice(self):
          return self.__foodPrice

     def setFQuantity(self,Fq):
          self.__foodQuantity=Fq
     def getFQuantity(self):
          return self.__foodQuantity

class Customer:
     pass