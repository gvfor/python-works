# print all century years from 1800-2024

for year in  range(1800,2024+1,1):
  
    if year%100==0:

        print(year)






# print all non century years from 1800-2024

for year in range(1800,2024+1,1):

    if year%100!=0:

     print(year)