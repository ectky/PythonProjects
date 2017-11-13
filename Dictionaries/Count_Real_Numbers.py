def print_number(num):
    if len(str(num)) in range(8,12):
        return num
    else:
        return'%g' %num

nums = [float(item) for item in input().split()]

counter = {}

for i in nums:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

for key in sorted(counter):
    print('{0} -> {1} times'.format(print_number(key), counter[key]))
