def Collatz(num):
	Ca = []
	i = 0
	Ca.append(num)
	while (int(Ca[i]) != 1):
		if int(Ca[i]) % 2 == 0:
			Ca.append(int(Ca[i])/2)
		else:
			Ca.append(3*int(Ca[i])+1)
		i=i+1
	return Ca

c=int(input("Please enter a number: "))
res1=Collatz(c)
print(res1)

L=[]
for items in range(1,1000):
	L.append(len(Collatz(items)))
print("\nThe number with longest Collatz array is: " + str(L.index(int(max(L)))+1))
