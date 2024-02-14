s = input()
a = input()
b = input()
change_count = 0

while True:
    if change_count > 1000:
        change_count = "Impossible"
        break
    if s.find(a) > -1:
        s = s.replace(str(a), str(b))
        change_count += 1
    if s.find(a) == -1:
        break

print(change_count)
