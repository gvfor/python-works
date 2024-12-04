def summary_ranges(nums):
    if not nums:
        return []

    ranges = []
    start = nums[0]  

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}->{nums[i - 1]}")
      
            start = nums[i]

    if start == nums[-1]:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}->{nums[-1]}")

    return ranges


nums = [0, 2, 3, 4, 6, 8, 9]
print(summary_ranges(nums))  
