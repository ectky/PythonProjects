text = input().lower()
sub = input().lower()

count = 0
found_index = text.find(sub)

while found_index != -1:
    count += 1
    found_index = text.find(sub, found_index + len(sub))

print(count)
