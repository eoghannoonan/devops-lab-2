# average.py
# Enter numbers separated by spaces, e.g. "10 20 30"
nums = [float(x) for x in input("Enter numbers: ").split()]
if nums:
    avg = sum(nums) / len(nums)
    print("Average:", avg)
else:
    print("No numbers entered.")
