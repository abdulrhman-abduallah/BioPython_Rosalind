#STEP 1
#Read the file and extract DNA sequence from it

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

DNA = list(dic.values())[0]


#================================================================================
#================================================================================

#STEP 2 
#Converting the DNA int RNA and its reverse complements

codon = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
cDNA=""

DNA_dict = {"A":"T","T":"A","C":"G","G":"C"}

for i in DNA:
	cDNA+=DNA_dict[i]

cDNA = cDNA[::-1]

#================================================================================
#================================================================================

#STEP 3 
#Find all the starting codon position location and then from each starting codon 
#translate it into protein until you hit the stop codon finaly remove the stop codon
#from the protein sequence 


def frame_read(DNA):
	frames_location=[]
	for i in range(len(DNA)):
		x = DNA[i:i+3]
		try:
			if codon[x] == "M":
				frames_location.append(i)
		except:
			break

	proteins=[]
	for i in frames_location:
		segments = ""
		for j in range(i, len(DNA),3):
			try:
				x = DNA[j:j+3]
				if codon[x] =="_":
					segments+=codon[x]
					break
				else:
					segments+=codon[x]
			except:
				break
		if segments.endswith("_"):
			proteins.append(segments.replace("_",""))


	return(proteins)

final = frame_read(DNA) + frame_read(cDNA)


final = set(final)

for i in final:
	print(i)




















































