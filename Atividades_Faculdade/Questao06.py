s = 0
i = 0
n = 10
while i < n:
    if i > n // 3:
        s += i
    i += 1
else:
    print(i, s)