import re
import requests

file = open("st.txt")

s = file.readlines()

list_ids=[]

for i in s:
	list_ids.append(i.replace('\n',''))

file.close()
#up until here the code reads protein ids in file and puts them in list


#from here the code opens a new txt file and writes to it the fasta format protein sequence and outputs it to out.txt


handle = open("out.txt","w")
ids_uniprot={}
for i in list_ids:
	req = requests.get("http://www.uniprot.org/uniprot/{}.fasta".format(i))
	x = req.text.split('\n')
	ids_uniprot[i] = x[0]#this creates dictionary containing ids and their fasta id
	handle.write(req.text)


handle.close()

#this here read the fasta file protein and turns it into dictionary format

file = open("out.txt")

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



# From here we establish the pattern to look for and put them in a list and out put the list 

r = re.compile("(?=N[^P][ST][^P])+")

#print(ids_uniprot)

for i in dic:
	positions = []
	y=""
	print(list(ids_uniprot.keys())[list(ids_uniprot.values()).index(i)])
	for j in re.finditer(r,dic[i]):
		positions.append(j.start()+1)
	for x in positions:
		y+= str(x) + " "
	print(y)
	print("")
