file = open("st.txt")

s1=file.readline().strip()
s2=file.readline().strip()

count = 0

for i in range(len(s1)):
	if s1[i] != s2[i]:
		count+=1

print(count)
