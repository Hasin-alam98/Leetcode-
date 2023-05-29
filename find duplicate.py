nums = [1, 2, 4, 5, 2]
prev = {}
for index, num in enumerate(nums):
    if num in prev:
        print("it contains double");
        break
    prev[num] = index
hi = True