def swap(var1,var2):
    vartemp = var1
    var1 = var2
    var2 = vartemp
    return var1,var2

var1 = 2
var2 = 3

print(swap(var1,var2))

N = [i for i in range(0,10)]
print(N)
for i in range(len(N)-1,-1,-1):
    print(N[i])

print('###')

for i in range(0,len(N),2):
    print(N[i])