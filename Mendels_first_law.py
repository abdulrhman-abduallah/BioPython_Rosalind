"""from itertools import product
k,m,n = 15,22,20

population = (['AA']*k)+(['Aa']*m)+(['aa']*n)

all_children = []

for parent1 in population:
	#remove selected from population
	chosen = population[:]
	chosen.remove(parent1)
	for parent2 in population:
		#get all possible children from 2 parents(punnet square)
		children = product(parent1,parent2)
		all_children.extend([''.join(c) for c in children])


dominants = filter(lambda c: 'A' in c, all_children)
#float for python2
print (float(len(list(dominants)))/len(all_children))"""

k = 23                                                        
m = 22                                                       
n = 27                                                        
pop = k + m + n                                               
prob = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*pop*(pop-1))
print(prob)                        