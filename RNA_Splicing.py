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

splist=[]
DNA=list(dic.values())[0]
for i in range(1,len(dic.values())):
	splist.append(list(dic.values())[i])

for i in splist:
	DNA = DNA.replace(i,"")



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
protein = ""

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

print(frame_read(DNA)[0])