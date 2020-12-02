data = open("./input.txt", "r")

nums = []

for line in data:
    nums.append(int(line))

for i in range(len(nums)):
    num1 = nums[i]
    for j in range(i+1, len(nums)):
        num2 = nums[j]

        if (num1+num2 == 2020):
            print(f"Found 2-number result: ({num1}, {num2}).\n{num1}x{num2}={num1*num2}")
        
        for k in range(j+1, len(nums)):
            num3 = nums[k]
            if (num1+num2+num3 == 2020):
                print(f"Found 3-number result: ({num1}, {num2}, {num3}).\n{num1}x{num2}x{num3}={num1*num2*num3}")