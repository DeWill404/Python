# This code required Third party modlue
#	following code for line 1 to 7
# 	Check if required module is present in system or not...
from Dependencies import check_module
check_module({'pyenchant'})
# Module Checking end...
# Remove This part if not required.... :)

import enchant		# for getting meaningfull word

en = enchant.Dict("en_US")	# Setting Language and accent

# Opening crossword file
# Notice You should have file.txt file before runing code
file = open("file.txt", "r+")

# Make 2D list
crossword = file.read().split("\n")
matrix = [ row.split(" ") for row in crossword ]

# Getting row and coloumn
row = len(matrix)
coloum = len(matrix[0])

# Max length
length = row if row>coloum else coloum

# Answer list
combine = []

# This code will iterate around character A at position (x,y)
# 		make all combination of it

for k in range(row):		# x of character A
	for m in range(coloum):		# y of character A
		for i in range(row):		# Move along row of A
			for j in range(coloum):		# Move along coloumn of A

				# Make each combination of length 2 to max
				for n in range(1, length+1):

					word = matrix[k][m]	  # Temporary variable for word
					x,y = i,j			  # Temporary reference of i & j
					
					# left
					if (i==k) and (j+1==m):
						while y>-1 and len(word)<n:
							word+=matrix[x][y]
							y-=1

					# right
					elif (i==k) and (j-1==m):
						while y<coloum and len(word)<n:
							word+=matrix[x][y]
							y+=1
						
					# top-left
					elif (i+1==k) and (j+1==m):
						while x>-1 and y>-1 and len(word)<n:
							word+=matrix[x][y]
							y-=1
							x-=1

					# top-right
					elif (i+1==k) and (j-1==m):
						while y<coloum and x>-1 and len(word)<n:
							word+=matrix[x][y]
							x-=1
							y+=1

					# top
					elif (i+1==k) and (j==m):
						while x>-1 and len(word)<=n:
							word+=matrix[x][y]
							x-=1

					# bottom-left
					elif (i-1==k) and (j+1==m):
						while x<row and y>-1 and len(word)<n:
							word+=matrix[x][y]
							x+=1
							y-=1

					# bottom-right
					elif (i-1==k) and (j-1==m):
						while y<coloum and x<row and len(word)<n:
							word+=matrix[x][y]
							x+=1
							y+=1

					# bottom
					elif (i-1==k) and (j==m):
						while x<row and len(word)<n:
							word += matrix[x][y]
							x+=1
						
					if len(word)>1:
						if en.check(word):
							if word not in combine:
								combine.append(word)


file.write("\n\n")
file.write(f"No. of words : {len(combine)}")
file.write("\n\n")
for word in combine:
	file.write(word+"\t")


print(combine)
print(len(combine))

