with open("day1data.txt")as f:
    lines = f.readlines()

nums = [ int(line.strip())for line in lines ]

print(nums)
