import re

# Find starting and ending index of a regex instring
# finditer gives many detail like string and its index
####################################################################
string = "We inform you with latest information."

for i in re.finditer( "inform", string ):
	print(i.span())

# or
pattern = re.compile("inform")
for match in pattern.finditer(string):
	print(match, match.span())

####################################################################


# Match a particular partern in string
####################################################################
string = "Bdll, Tcll, Cbll, mall, Bell"
matched = re.findall( "[A-Z][^b]ll", string )

for i in matched:
	print(i)
####################################################################


# Replace a particular pattern in string
####################################################################
string = "aTT gTT bTT qTT cTTdTT nTT"

regexPattern = re.compile( "[a-d]TT" )

string = regexPattern.sub("TTT", string)

print(string)
####################################################################


# Replace tab
####################################################################
string1 = "		a	a	a"
string2 = r'aa\\\\a\\\\a'

reg1 = re.compile("\t")
reg2 = re.compile(r"\b")

new1 = reg1.sub("@", string1)
new2 = reg2.sub("@", string2)

print(new1+"\n"+new2)
####################################################################


# Match digit
####################################################################
string = "1234d12356q13"

print( re.findall("\d", string) )		# MAth all digit
print( re.findall("\D", string) )		# Match all except digit
print( re.findall("\d{2,4}", string) )	# Match all except digit
####################################################################


# Match contect no. with format XXX-XXX-XXXX
####################################################################
contect = [
	"123-345-7657",
	"123-345-757",
	"1232-3454-7657",
	"12&3-34e5-7e657",
	"009-345-7347",
	"990-345-7657",
	"123-345-7657",
	"123-334-7657",
	"123-a45-7a57",
	"a23-345_7657",
]

S = " ".join(contect)
valid_contect = re.findall("\d{3}-\d{3}-\d{4}", S)

print(valid_contect)
####################################################################


# Valid name
####################################################################
names = ["Irshad Ahmed", "Siddique"] 

for name in names:
	if re.findall("[A-z][a-z]*\s[A-z][a-z]*", name):
		print(name+" is valid..")
	else:
		print(name+" is not valid..")
####################################################################

# Vald Email
####################################################################
emails = ["irsha@gm.com", "23%.*@mk.co", "@.co", "asedd@weo2.Co"]

for email in emails:
	if re.findall( "[\w.*%]+@[\w]+.[a-z]{2,3}", email ):
		print( email+" is valid....." )
	else:
		print( email+" is not valid....." )

####################################################################

# Start with^ and end with$
####################################################################
strings = [
	"Apple is greats.",
	"Aeroplane is flying!",
	"Ball is moving.",
	"Bros!!"
]
for string in strings:
	if re.findall( "^A", string ):
		print("Starts with A : "+string)
	if re.findall( "^B", string ):
		print("--Starts with B : "+string)
	if re.findall( "[.]$", string ):
		print("****Ends with . : "+string)
	if re.findall( "!$", string ):
		print("......Ends with ! : "+string)
####################################################################
