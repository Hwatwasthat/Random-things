def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def fiveTimes(a):
    a = a * 5
    return a

testList = [1, -4, 8, -9]

applyToEach(testList, fiveTimes)

print(testList)
