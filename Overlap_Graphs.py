file = open("st.txt")

s = file.readlines()

dic = {}

l=[]

for i in s:
	l.append(i.replace('\n',''))

for i in l:
	if ">" in i:
		x=i.replace(">","")
		#x=i
		dic[x]="" #dic[i]=""
	else:
		dic[x]+=i


def overlap(dic,n):
	result = ""
	for i in range(len(dic)):
		x = list(dic.values())[i]
		y = list(dic.keys())[i]
		for j in dic:
			if j == y:
				continue
			elif dic[j][-n:] == x[:n]:
				result += j+" "+y+"\n"
	return result



out = open("out.txt","w")
out.write(overlap(dic,3))
out.close()




