import itertools 
n = int(input("Put number here: "))


l = list(itertools.permutations(range(1,n+1)))



out = open("out.txt","a")
out.write(str(len(l))+"\n")
for i in range(len(l)):
	s =""
	for j in l[i]:
		s+=str(j)+" "

	out.write(s+"\n")

