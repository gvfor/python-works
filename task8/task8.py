def product_except_self(nums):
    n = len(nums)
    
    output = [1] * n

    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]

   
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output

# Example 1
nums1 = [1, 2, 3, 4]
print(product_except_self(nums1))  

# Example 2
nums2 = [-1, 1, 0, -3, 3]
print(product_except_self(nums2))  
