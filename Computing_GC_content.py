file = open("st.txt")


scores={}

def gc(x):
	return (((x.count("G")+x.count("C")))/len(x))*100



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


for i in dic:
	scores[i] = gc(dic[i])


max_value = max(scores,key=scores.get)

#print(scores)
#print(len(dic[max_value]))
print(max_value.replace(">",""))
print(scores[max_value])

"""==============================================================================="""

