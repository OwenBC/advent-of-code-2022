f = open('input.txt', 'r')
m = 0
c = 0
for l in f:
    line = l.strip()
    if line == '':
        m = max(m, c)
        c = 0
    else:
        c+=int(line)
f.close()

print(m)