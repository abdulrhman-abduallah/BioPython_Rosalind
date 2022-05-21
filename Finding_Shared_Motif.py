"""file = open("st.txt")

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

print(dic)
"""

from Bio import SeqIO                      
sequences = []                             
handle = open('st.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    sequence = []                          
    seq = ''                               
    for nt in record.seq:                  
        seq += nt                          
    sequences.append(seq)                  
handle.close()                             


srt_seq = sorted(sequences, key=len)     
short_seq = srt_seq[0]                   
comp_seq = srt_seq[1:]                   
motif = ''                               
for i in range(len(short_seq)):          
    for j in range(i, len(short_seq)):   
        m = short_seq[i:j + 1]           
        found = False                    
        for sequ in comp_seq:            
            if m in sequ:                
                found = True             
            else:                        
                found = False            
                break                    
        if found and len(m) > len(motif):
            motif = m                    
print(motif)