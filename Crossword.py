# import enchant

# en = enchant.Dict("en_US")


# f = open("file.txt", 'r')

# content = f.read().split()

# print(content)

# for word in content:
#   print("Valid" if en.check(word) else "Invalid")

# L = [['A', 'B'],['C', 'D']]
# l = len(L)
# for k in range(l):
# 	for m in range(l):
# 		for i in range(l):
# 			for j in range(l):
# 				if j!=m or i!=k:
# 					print(L[k][m],L[i][j],sep=",",end=" ")
# 		print(end="\n")

L = [['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']]
l = len(L)
for k in range(l):
	for m in range(l):
		for i in range(l):
			for j in range(l):
				if (i+1==k or i-1==k) and (j+1==m or j-1==m):
					print(L[k][m],L[i][j],sep=",",end=" ")
				elif (i+1==k or i-1==k) and (j==m):
					print(L[k][m],L[i][j],sep=",",end=" ")
				elif (i==k) and (j+1==m or j-1==m):
					print(L[k][m],L[i][j],sep=",",end=" ")
		print(end="\n")
