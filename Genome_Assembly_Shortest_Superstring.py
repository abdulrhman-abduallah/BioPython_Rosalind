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

seqs= []
for i in dic:
	seqs.append(dic[i])


def find_sim(x,y):
	xhalf1=x[:int(len(x)/2)+1]
	xhalf2=x[int(len(x)/2):]
	yhalf1=y[:int(len(y)/2)+1]
	yhalf2=y[int(len(y)/2):]
	if xhalf2 in y:
		if y.find(xhalf2) > int(len(x)/2):
			pass
		else:
			return x+y
	
main_list=[]
for i in seqs:
	x=seqs.copy()
	x.remove(i)
	for j in x:
		if find_sim(j,i) == None:
			continue
		else:

			main_list.append(find_sim(j,i))

last_list=[]


for i in main_list:
	x=main_list.copy()
	x.remove(i)
	for j in x:
		if find_sim(j,i) == None:
			continue
		else:

			last_list.append(find_sim(j,i))

print(last_list)
