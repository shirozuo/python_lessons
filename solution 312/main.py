s = input()
t = input()
count = 0

for i in range(0, len(s)):
    if s.startswith(t):
        count += 1
    s = s.replace(s[0], "", 1)
print(count)
