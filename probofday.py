age=int(input("enter the age"))
if age<18 and  age>=0 :
    print("You are a minor")
elif age>=18 and age<65 :
    print("You are an adult")
elif age>=65 :
    print("You are a senior")
else :
    print("invalid input")            



for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")

    print()




password = input("Enter the password: ")
count1 = 0
count2 = 0
count3 = 0
count4 = 0

if len(password) >= 8:
    for i in range(len(password)):
        ascii_val = ord(password[i])
        
        if ascii_val >= 65 and ascii_val <= 90:  # Uppercase
            count1 += 1
        elif ascii_val >= 97 and ascii_val <= 122:  # Lowercase
            count2 += 1
        elif ascii_val >= 48 and ascii_val <= 57:  # Digits
            count3 += 1
        elif (ascii_val >= 33 and ascii_val <= 47) or \
             (ascii_val >= 58 and ascii_val <= 64) or \
             (ascii_val >= 91 and ascii_val <= 96) or \
             (ascii_val >= 123 and ascii_val <= 126):  # Special characters
            count4 += 1

    if count1 > 0 and count2 > 0 and count3 > 0 and count4 > 0:
        print("Password criteria met.")
    else:
        print("Password criteria not met.")
else:
    print("Password must be at least 8 characters long.")  # Error was here



import matplotlib.pyplot as plt
sales_data=[25,32,29,35,41,40,45,38,50,55,60,70]
months=["jan","feb","mar","apr","may","june","july","aug","sept","oct","nov","dec"]
sales_sum=0
for i in sales_data:
    sales_sum+=i

average_sales=sales_sum/len(sales_data)
max_sales=sales_data[0]
max_month_index=0
for i in range(len(sales_data)):
    if sales_data[i]>max_sales:
        max_sales=sales_data[i]
        max_month_index=i
max_month=months[max_month_index] 
plt.figure(figsize=(10,6))
plt.plot(months,sales_data,marker='o',label="monthly sales")
plt.scatter(months[max_month_index],max_sales,color='red'.s=100,label="Highest sales")
plt.show()
