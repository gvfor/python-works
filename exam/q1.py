num1=int(input("enter number"))

num2=int(input("enter number"))

num3=int(input("enter number"))

if num1>num2 and num1>num3:
    print("num1 is largest")

    if num2>num3:
        print("num2 is second largest")

        print(num1,num2,num3)


    else:
        print("num3 is second largest")
        print(num1,num3,num2)


elif num2>num1 and num2>num3:
    print("num2 is largest")

    if num1>num3:
        print("num1 is second largest")
        print(num2,num1,num3)


    else:
        print("num3 is second largest")
        print(num2,num3,num1)

elif num3>num1 and num3>num2:
    print("num3 is largest")

    if num1>num2:
        print("num1 is second largest") 
        print(num3,num1,num2)


    else:

        print("num2 is second largest") 
        print(num3,num2,num1) 


elif num1==num2 and num1==num3:

    print("all numbers are equal")         