num1=int(input("enter number"))

num2=int(input("enter number"))

max_number=(num1*num2)

for i in range(max_number,(num1*num2)+1,max_number):


    if i%num1==0 and i%num2==0:


       print(i)    

       break   