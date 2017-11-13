n = int(input())

sum = 0
prev_sum = 0
diff = 0
prev_diff = 0
max_diff = 0
equal_sums = True

for i in range(n):
    current_number1 = int(input())
    current_number2 = int(input())
    prev_sum = sum
    sum = current_number1 + current_number2

    if i >= 1:
        prev_diff = diff
        diff = abs(prev_sum-sum)
        max_diff = max(prev_diff, diff)
        if prev_sum != sum:
            equal_sums = False


if equal_sums:
    print("Yes, value={0}".format(sum))
else:
    print("No, maxdiff={0}".format(max_diff))
