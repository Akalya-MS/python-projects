name=input("enter the name of employee:")
age=int(input("enter the age:"))
gender=input("enter the gender:")
no_of_days=int(input("enter no.of.days:"))

if age>=18 and age<30 and gender=="male":
    wages=700
    amount=no_of_days*wages
    print("the amount to be paid is:",amount)

elif age>=18 and age<30 and gender=="female":
    wages=750
    amount=no_of_days*wages
    print("the amount to be paid is:",amount )

elif age>=30 and age<=40 and gender=="male":
    wages=800
    amount=no_of_days*wages
    print("the amount to be paid is:",amount )

elif age>=30 and age<=40 and gender=="female":
    wages=800
    amount=no_of_days*wages
    print("the amount to be paid is:",amount )

else:
    print("invalid")



