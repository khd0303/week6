def multiples(a,b):
    arr = []
    for i in range(b):
        arr.append (int(a * (i+1)))
    return arr


r1,r2,r3,r4 = multiples(3,4)


print(r1,r2,r3,r4)



r1,r2,r3,r4,r5 = multiples(2,5)

print(r1,r2,r3,r4,r5)