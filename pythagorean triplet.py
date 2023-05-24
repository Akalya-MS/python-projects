a=int(input("enter side a:"))
b=int(input("enter side b:"))
c=int(input("enter side c:"))

if(a**2==b**2+c**2)or(b**2==a**2+c**2)or(c**2==a**2+b**2):
    print("it is a pythagorean triplet")
    
else:
    print("it is not a pythagorean triplet")