def merge_intervals(intervals):
    if not intervals:
        return []

    
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]  

    for current in intervals[1:]:
        previous = merged[-1]

        
        if current[0] <= previous[1]:  
        
            merged[-1] = [previous[0], max(previous[1], current[1])]
        else:
            
            merged.append(current)

    return merged


intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals1))  


intervals2 = [[1, 4], [4, 5]]
print(merge_intervals(intervals2))  
