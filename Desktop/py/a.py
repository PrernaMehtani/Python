p=[12,35,43,89]
i=3
#print(p[i])

def rev_list(i):
	if i!=-1:
		print(p[i])
		rev_list(i=i-1)
rev_list(i)
