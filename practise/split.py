def split_list(input_list):

    mid = len(input_list)//2

    first_half = input_list[:mid]
    second_half = input_list[mid:]

    return first_half , second_half

my_list=[1,2,3,4,5,6,7,8,9]

first_half, second_half=split_list(my_list)

print("first half:",first_half)
print("second half:",second_half)
