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