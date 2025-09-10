a=3
b=5
temp=a
a=b
b=temp
print(a,b)



a=int(input("Enter the value of a"))
if a>=90:
    print("A")

elif a>=80&a<=89:
    print("B")

elif a>=70&a<=79:
    print("C")

elif a>=60&a<=69:
    print("D")

else :
    print("F")



length=int(input("enter length"))
breadth=int(input("enter breadth"))
perimeter=2*(length+breadth)
Area=length*breadth
print(perimeter)
print(Area)




a=complex(input("enter first")) 
b=complex(input("enter second"))
sum=a+b
diff=a-b
multiply=a*b
print(sum,diff,multiply)     


a=int(input("enter the temperature"))
fahrenheit=((9/5)*a)+32
print(fahrenheit)


    
    
