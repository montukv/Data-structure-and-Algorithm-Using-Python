#Binary tree using python by Montukeshwar vaishnaw

class node:
	def __init__ (self,data = None):
		self.data=data
		self.left = None
		self.right = None

class tree:
	def __init__ (self):
		self.root = None

	def insert(self , value) :
		if self.root == None:
			self.root = node(value)
		else : 
			self._insert(value , self.root)

	def _insert(self, value ,cur_node):
		if value < cur_node.data :
			if cur_node.left == None:
				cur_node.left = node(value)
			else : 
				self._insert(value , cur_node.left)

		elif value > cur_node.data:
			if cur_node.right == None:
				cur_node.right = node(value)
			else : 
				self._insert(value,cur_node.right)

		else :
			print("Value is already in the tree ")

	def display(self):
		if self.root ==None:
			print("\nTree is empty") 
		else : 
			self._display(self.root)

	def _display(self,cur_node):
		if cur_node != None :
			self._display(cur_node.left)
			print(str(cur_node.data))
			self._display(cur_node.right)
			

	def search(self , key):
		if self.root == key :
			print ("searched key is found at root",cur_node.data)
		else : 
			self._search(key  , self.root)

	def _search(self , key , cur_node):
		if key == cur_node.data :
			print("key if found : ",cur_node.data)
		elif key < cur_node.left : 
			self._search(key,cur_node.left)
		else :
			self._search(key , cur_node.right)

	def height(self):
		if self.root != None: 
			return self._height(self.root , 0)
		else : 
			return 0

	def _height(self , cur_node , cur_height): 
		if cur_node == None : 
			return cur_height
		else  :
			left_height = self._height(cur_node.left , cur_height + 1 )
			right_height = self._height(cur_node.right , cur_height + 1)
			return max(left_height , right_height)

	def leaf(self):
		if self.root == None :
			print ("TREE IS EMPTY")
		else  :
			self._leaf(self.root)

	def _leaf(self , cur_node) :
		leaf = []
		if cur_node.data == None : 
			leaf.append(cur_node.data)
		else :
			left_leaf = _leaf(cur_node.left)
			right_leaf = _leaf(cur_node.right)

		print(leaf)

t = tree()
c = int(input("\nEnter your choise \n1.insert \n2.display \n3.search \n4.height of tree n5.leaf nodes \n6.delete node\n7.exit\n-->"))
while c != 7 :
		
		if c == 1  :
			n = input("\nEnter element  : ")
			t.insert(n)
		elif c == 2:
			print("Displaying element of linked list")
			t.display()
		elif c == 3:
			key = input("\nEnter the key index to search : ")
			t.search(key)
		elif c == 4:
			
			h = t.height()
			print ("\nHeight of tree is ",h)
		elif c == 5 : 
			print("leaf nodes are  :")
			t.leaf()
		elif c == 6 :
			print("\nTHIS PART IS NOT BUILD YET PLEASE TRY OTHER OPTIONS\n")
		elif c >= 8 : 
			print("\nWRONG INPUT! please try again")
		
		c = int(input("\nEnter your choise \n1.insert \n2.display \n3.search \n4.height of tree \n5.leaf nodes \n6.delete node\n7.exit\n-->"))

print("come again, Motherfucker")
