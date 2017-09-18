from sys import stdin


maxi = None
mini = None
for line in stdin:
    n = int(line.strip())
    if maxi is None and mini is None:
        maxi = n
        mini = n
    else:
        maxi , mini = max(maxi, n), min(mini, n)
print(mini, maxi)


