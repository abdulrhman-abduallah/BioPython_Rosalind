DNA_string="AAAACCCGGT"

#method1
rDNA = ""
for i in DNA_string:
	if i == "A":
		rDNA+="T"
	if i == "T":
		rDNA+="A"
	if i == "C":
		rDNA+="G"
	if i == "G":
		rDNA +="C"

print(rDNA[::-1])


#method2

cDNA=""

DNA_dict = {"A":"T","T":"A","C":"G","G":"C"}

for i in DNA_string:
	cDNA+=DNA_dict[i]

print(cDNA[::-1])