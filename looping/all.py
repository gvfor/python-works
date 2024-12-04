start=int(input("enter number"))

end=int(input("enter number"))

if start<end:

    for num in range(start,end+1,1):

         print(num)



else:
     
    for num in range(start,end-1,-1):

        print(num) 