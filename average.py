from sys import stdin

total = 0.0
count = 0
for line in stdin:
    n = line.strip()
    if len(n) == 0 and count > 0:
        break
    total += float(n)
    count += 1
print ("avergage" , total/count)


