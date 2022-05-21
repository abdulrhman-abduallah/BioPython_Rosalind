#This opens the file of fasta format and converts sequences into dictionary

file = open("st.txt")

s = file.readlines()

dic = {}

l=[]

for i in s:
	l.append(i.replace('\n',''))

for i in l:
	if ">" in i:
		x=i
		dic[i]=""
	else:
		dic[x]+=i

#dic is the dictionary containing the sequences and their IDs

f = list(dic.values())[0]

DNA_count = {"A":[],"C":[],"G":[],"T":[]}

for i in range(len(f)):
	G,C,T,A=0,0,0,0

	for j in dic:
		if "A" == dic[j][i]:
			A+=1
		elif "G" == dic[j][i]:
			G+=1
		elif "C" == dic[j][i]:
			C+=1
		elif "T" ==dic[j][i]:
			T+=1 
	DNA_count["A"].append(A)
	DNA_count["T"].append(T)
	DNA_count["G"].append(G)
	DNA_count["C"].append(C)

x = len(list(DNA_count.values())[0])
print(DNA_count)
consensus =""
new_dict={"A":0,"G":0,"C":0,"T":0}
for i in range(x):
	new_dict={"A":0,"G":0,"C":0,"T":0}
	for j in ["A","G","C","T"]:
		new_dict[j] = DNA_count[j][i]
	consensus += max(new_dict,key=new_dict.get)

print(consensus)