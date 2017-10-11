from sys import stdin
for line in stdin:
    if line.strip() == '':
        continue
    print(line, end='')
