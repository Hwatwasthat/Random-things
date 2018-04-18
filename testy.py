output = 0
for i in range (100, 1000):
    for x in range (100, 1000):
        a = i
        b = x

        c = a * b
        cc = str(c)
        cr = cc[::-1]

        if cc == cr:
            if c > output:
                output = c
print(output)
                
