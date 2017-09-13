a = [[1,1,1],
        [2,2,2],
        [3,3,3]]
b = [[0,0,0],
        [0,0,0],
        [0,0,0]]

n = len(a)
for i in range(n):
    for j in range(n):
        b[i][j] = a[i][j]

print(b)

c = [[1,1,1],
        [2,2]]
d = [[0,0,0],
        [0,0]]

for i in range(len(c)):
    for j in range(len(c[i])):
        d[i][j] = c[i][j]
print(d)

d = [[0,0,0],
        [0,0]]
d=[]
for row in c:
    r=[]
    for v in row:
        r+= [v]
    d+=[r]

print(d)
