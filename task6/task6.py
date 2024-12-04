def longest_common_prefix(strs):
    if not strs:
        return ""

    shortest_str = min(strs, key=len)

    for i in range(len(shortest_str)):
        for string in strs:
            if string[i] != shortest_str[i]:
                return shortest_str[:i]

    return shortest_str

# Example 1
strs1 = ["flower", "flow", "flight"]
print(longest_common_prefix(strs1)) 

# Example 2
strs2 = ["dog", "racecar", "car"]
print(longest_common_prefix(strs2)) 
