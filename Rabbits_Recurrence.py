def fib(n,k):
	parent,child = 1,1
	for i in range(n -1):
		child,parent = parent,parent+(child*k)
	return child

print(fib(5,3))