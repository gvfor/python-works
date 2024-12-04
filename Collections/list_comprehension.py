arr=[2,3,4,5,6,7]

squre=[num **2 for num in arr]

print(squre)

add_ten=[num+10 for num in arr]

print(add_ten)

odd_numbers=[num for num in arr if num%2!=0]

print(odd_numbers)

even_numbers=[num for num in arr if num%2==0]
print(even_numbers)

num_gt_five=[num for num in arr if num>5]
print(num_gt_five)