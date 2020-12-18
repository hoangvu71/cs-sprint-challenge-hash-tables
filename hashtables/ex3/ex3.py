def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    # let s put each list into a dict and those dict into an array
    all_nums = []
    for eachList in arrays:
        list_dict = {}
        for eachNum in eachList:
            if eachNum not in list_dict:
                list_dict[eachNum] = True
        all_nums.append(list_dict)
    
    for num in arrays[0]:
        # check if those nums is also in the other nums
        contains_in_all_count = 0
        for eachDict in all_nums:
            if num in eachDict:
                contains_in_all_count += 1
        if contains_in_all_count == len(all_nums):
            result.append(num)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

