start=int(input("enter starting limit"))

end=int(input("enter limit"))


if start>end:
   start,end=end,start


i=start
while(i<=end):


 if i%2!=0:
  

  print(i)


  i=i+1