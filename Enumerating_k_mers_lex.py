import itertools 
s=input("put input here: ")
#n = int(input("Put number here: "))
n=int(input("put number here: "))

x=[]
for i in s:
	if i !=" ":
		x.append(i)

x = sorted(x)

l = list(itertools.product(x,x))



out = open("out.txt","w")


for i in range(len(l)):
	s=""
	for j in l[i]:
		s+=str(j)

	out.write(s+"\n")

