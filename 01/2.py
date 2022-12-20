f = open('input.txt', 'r')
m = [0,0,0]
c = 0
for l in f:
    line = l.strip()
    if line == '':
        if c > min(m):
            m.append(c)
            m.remove(min(m))
        c = 0
    else:
        c+=int(line)
f.close()

print(sum(m))