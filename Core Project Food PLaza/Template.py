from Model import Food,Customer
from View import FoodView,CustomerView
class FoodTemplate:
     fViewobj=FoodView()
     def foodTask(self):
          print("1- Add Food \n 2 - Show Menu \n 3 - Update Food \n 4 - Delete Food")
          op=int(input("What You Want to do ? "))
          if op==1:
               name=input("Enter your name : ")
               type1=input("Enter type : ")
               category=input("Enter caegory : ")
               price=float(input("Enter Price : "))
               quantity=int(input("Enter Available quantity : "))
               foodobj=Food(name,type1,category,price,quantity)
               FoodTemplate.fViewobj.addfood(foodobj)
          elif op==2:
               print("A. Veg \n B. Non-Veg \n C. Search by Name \n D. Show All \n")
               choice=input("Enter your Choice : ")
               flist=FoodTemplate.fViewobj.showType(choice)
               if flist !=None:
                    for food in flist:
                         print(food)

          elif op==3:
               print("1. Food name \n 2. Food Type \n 3. Food Catagory \n 4. Food Price \n 5. Food Quantity")
               op1=int(input("What you want to update ?"))
               FoodTemplate.fViewobj.updateFood(op1)
          elif op==4:
               print("Enter food Id to delete the Food ")
               fid=int(input("Enter the FoodID to be deleted : "))
               fobj=FoodTemplate.fViewobj.showFoodById(fid)
               if fobj is not None:
                    delete=input("Do you want to delete this Food press y/n")
                    if delete=='y':
                         flag=FoodTemplate.fViewobj.deleteFood(fid)
                         if flag==True:
                              print("Food is deleted...*_*")
                         else :
                              print("Food is not deleted....^-^")
                    else :
                         print("Okay...")
               else:
                    print("Food not found ")
          
class CustomerTemplate:
     def customerTask(self):
          pass
