import os
from Template import FoodTemplate,CustomerTemplate
print("Welcome to FoodPlaza")
while True:
    print("1 : Food \n 2 : Customer \n 3 : Cart \n 4 : Orders \n 5 : Exit")
    try :
        ch=int(input("Namastey  \n Enter your Choice -> \n"))
        if ch==1:
            foodTemplateobj=FoodTemplate()
            foodTemplateobj.foodTask()
        elif ch==2:
            obj=CustomerTemplate()
            obj.customerTask()
        elif ch==3:
            pass
        elif ch==4:
            pass
        elif ch==5:
            os.exit(0)
    except Exception as e:
        print("Enter valid Exception",e)


