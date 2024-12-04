arr=[100,200,400,500,600,700,900]

odd_position_elements=[num for index,num in enumerate(arr) if index%2!=0]
odd_position_elements.reverse()

print(odd_position_elements)

for index,num in enumerate(odd_position_elements):

    arr[index+1]=num

print(arr)

