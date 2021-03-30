from dtabase import *
from Model import Food
class FoodView:
     
     def addfood(self,foodobj):
          try:
               sql="insert into Food(FoodName,FoodType,FoodCategory,FoodPrice,FoodQuantity) values('%s','%s','%s','%f','%d')"
               result=mycursor.execute(sql %(foodobj.getFName(),foodobj.getFType(),foodobj.getFCategory(),foodobj.getFPrice(),foodobj.getFQuantity()))
               db.commit()
               if result!=None:
                    print("Added Sucessfully.......")
                    return True
               else:
                    return False

          except pymysql.DatabaseError as e:
               db.rollback()
               print("Database Error : ",e)

     def showType(self,op):
          try:
               if op.upper()=='A':
                    sql1="select * from food where FoodType='veg'"
                    mycursor.execute(sql1)
                    vFood=mycursor.fetchall()
               elif op.upper()=='B':
                    sql2="select * from food where FoodType='Non veg'"
                    mycursor.execute(sql2)
                    vFood=mycursor.fetchall()
               elif op.upper() == 'C':
                    fname=input("Enter food name : ")
                    sql3 = "select * from food where upper(fname)"
                    mycursor.execute(sql3)
                    vFood = mycursor.fetchall()
               elif op.upper()=='D':
                    sql4="select * from food"
                    mycursor.execute(sql4)
                    vFood=mycursor.fetchall()
          except pymysql.DatabaseError as e:
               print("Exception : ", e)
          return vFood

     def updateFood(self,op1):
          try:
               if op1==1:
                    id=int(input("Enter fooodId to change Food name : "))
                    name=input("Enter updated name : " )
                    sql="update food set FoodName='%s' where FoodId='%d'"
                    up=mycursor.execute(sql %(name,id))
                    db.commit()
                    if up>0:
                         print("Updated Sucessfully......!")
                         return True
                    else :
                         return False
               elif op1==2:
                    id = int(input("Enter fooodId to change Food type : "))
                    name = input("Enter updated Type : ")
                    sql = "update food set FoodType='%s' where FoodId='%d'"
                    up = mycursor.execute(sql % (name, id))
                    db.commit()
                    if up > 0:
                         print("Updated Sucessfully......!")
                         return True
                    else:
                         return False
               elif op1==3:
                    id = int(input("Enter fooodId to change Food Category : "))
                    name = input("Enter updated Category : ")
                    sql = "update food set FoodCategory='%s' where FoodId='%d'"
                    up = mycursor.execute(sql % (name, id))
                    db.commit()
                    if up > 0:
                         print("Updated Sucessfully......!")
                         return True
                    else:
                         return False
               elif op1==4:
                    id = int(input("Enter fooodId to change Food Price : "))
                    name = input("Enter updated Price : ")
                    sql = "update food set FoodPrice='%s' where FoodId='%d'"
                    up = mycursor.execute(sql % (name, id))
                    db.commit()
                    if up > 0:
                         print("Updated Sucessfully......!")
                         return True
                    else:
                         return False
               elif op1 == 5:
                    id = int(input("Enter fooodId to change Food Quantity : "))
                    name = input("Enter updated Quantity : ")
                    sql = "update food set FoodQuantity='%s' where FoodId='%d'"
                    up = mycursor.execute(sql % (name, id))
                    db.commit()
                    if up > 0:
                         print("Updated Sucessfully......!")
                         return True
                    else:
                         return False
          except pymysql.DatabaseError as e:
               print("Exception : ",e)

     def showFoodById(self,fid):
          sql2="select * from food where FoodId='%d'"
          mycursor.execute(sql2 %(fid))
          xfood=mycursor.fetchall()
          return xfood

     def deleteFood(self,fid):
          try:
               sql="delete from food where FoodId='%d'"
               result=mycursor.execute(sql %(fid))
               db.commit()
               if result>0:
                    return True
          except pymysql.DatabaseError as e:
               print("Exception in DeleteFood fun : ",e)




class CustomerView:
     pass