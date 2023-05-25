v=float(input("enter the speed in kms:"))
t=float(input("enter the temperature in degree celsius:"))
w=13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
print("the wind chill index is:",w)
x=round(w)
print("wind chill index is rounded to the neraest integer:",x)