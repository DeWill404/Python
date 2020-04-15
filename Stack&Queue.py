# This program will implement Stack and Queue using Linked list

# Creating a node
class CreateNode:
	def __init__(self, data):
		self.data = data
		self.next = None
# Class LinkedList
class LinkedList:
	def __init__(self):         # Intializing Head node
		self.head = None
	def appendNode(self, data): # Function to append node
		if (self.head == None):
			self.head = CreateNode(data)
		else:
			newNode = self.head
			while(newNode.next != None):
				newNode = newNode.next
			newNode.next = CreateNode(data)
		print(f"{data} added")
	def traverse(self):         # Function to traverse LIFO in list
		if (self.head == None):
			print("Empty -> NO ELEMENT PRESENT")
		else:
			newNode = self.head
			lis = []
			while(newNode != None):
				lis.append(newNode.data)
				newNode = newNode.next
			print(*lis, sep="  ")
			return lis
	def reverse(self):          # Function to traverse FILO in list
		if (self.head == None):
			print("Empty -> NO ELEMENT PRESENT")
		else:
			lis = self.traverse()
			reversed(lis)
			print(*lis, sep="  ")
	def deleteNodeEnd(self):   # Deleting last node
		if(self.head == None):
			print("Empty -> NO ELEMENT PRESENT")
		else:
			node = self.head
			if(node.next == None):
				print(f"{node.data} deleted")
				self.head = None
			else:
				while(node.next.next != None):
					node = node.next
				print(f"{node.next.data} deleted")
				node.next = None
	def deleteNodeFront(self): # Deleting the first node
		if(self.head == None):
			print("Empty -> NO ELEMENT PRESENT")
		else:
			node = self.head
			if(node.next == None):
				print(f"{node.data} deleted")
				self.head = None
			else:
				print(f"{node.data} deleted")
				node = node.next
				self.head = node

# STACK
class Stack:
	def __init__(self):
		self.l = LinkedList()
	def insert(self, data):
		self.l.appendNode(data)
	def delete(self):
		self.l.deleteNodeEnd()
	def display(self):
		self.l.reverse()

# QUEUE
class Queue:
	def __init__(self):
		self.l = LinkedList()
	def insert(self, data):
		self.l.appendNode(data)
	def delete(self):
		self.l.deleteNodeFront()
	def display(self):
		self.l.traverse()

# MENU
menu1 = '''
Enter 
  1 STACK
  2 QUEUE
  3 EXIT
	  Enter :- '''
menu2 = '''
	Enter
	  1 INSERT
	  2 DELETE
	  3 DISPLAY
	  4 EIXT
		  Enter :- '''

# MAIN FUNCTION
while (True):

	select = int(input(menu1))

	if (select == 1):  #STACK

		s = Stack()
		while (True):

			print("STACK", end="")
			select = int(input(menu2))

			if (select == 1):
				select = int(input("    Enter no. to insert : "))
				s.insert(select)
			elif (select == 2):
				s.delete()
			elif (select == 3):
				s.display()
			elif (select == 4):
				break
			else:
				print("\n\t\t Please Enter correct OPTIONS.....\n")

	elif (select == 2):#QUEUE

		q = Queue()
		while (True):

			print("QUEUE", end="")
			select = int(input(menu2))

			if (select == 1):
				select = int(input("   Enter no. to insert : "))
				q.insert(select)
			elif (select == 2):
				q.delete()
			elif (select == 3):
				q.display()
			elif (select == 4):
				break
			else:
				print("\n\t\t Please Enter correct OPTIONS.....\n")

	elif (select == 3):
		break

	else:
		print("\n\t Please Enter correct OPTIONS.....\n")