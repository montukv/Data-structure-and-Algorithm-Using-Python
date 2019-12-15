#linked list using Python by montukeshwar Vaishnaw

#class to store data and pointer
class node:
	def __init__ (self,data= None):
		self.data = data
		self.next = None

#class for linked list 
class linked:
	def __init__ (self):
		self.head = node()		#head points the starting of linked list

	def accept(self,data): 			#function to accept nodes
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def length(self):
		count = 0
		cur = self.head
		while cur.next != None:
			count = count + 1
			cur = cur.next

		return count

	def display(self):
		disp = []
		cur = self.head
		while cur.next != None :
			cur = cur.next
			disp.append(cur.data)
		print(disp)

	def search(self,key):
		if key == self.length():
			print("**WRONG INPUT**")
		cur = self.head
		cur_index = 0
		while cur.next != None:
			cur = cur.next
			if key == cur_index :
				print("Search key has value ",cur.data)

			cur_index = cur_index + 1






l_list = linked()		#Object of class

c = int(input("\nEnter your choise \n1.insert \n2.display \n3.search \n4.delete \n5.exit\n-->"))
while c != 5 :
		
		if c == 1  :
			n = input("\nEnter element  : ")
			l_list.accept(n)
		elif c == 2:
			print("Displaying element of linked list")
			l_list.display()
		elif c == 3:
			key = input("\nEnter the key index to search : ")
			l_list.search(key)
		elif c == 4:
			print("\nUNDER PROCESS")
		elif c >= 6 : 
			print("\nWRONG INPUT! please try again")
		
		c = int(input("\nEnter your choise \n1.insert \n2.display \n3.search \n4.delete \n5.exit\n-->"))

print("come again, Motherfucker")	