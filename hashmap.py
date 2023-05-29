def two_sum():
    nums = [3, 6, 7, 8, 9, 8]
    target = 15
    prev = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in prev:
            return [prev[diff], index]
        prev[num] = index

    return


print(two_sum())
