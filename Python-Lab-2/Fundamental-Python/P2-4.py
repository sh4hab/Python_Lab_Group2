a = [2**i for i in range(17)]
b = [x*x for x in range(1,5)]
c = [a[x] for x in b if x%2==0]

print('a= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c))
