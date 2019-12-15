#stack and queue in python by Montukeshwar Vaishnaw
#In python ue can use list as stack and queue both :
def push(a):
		a.append(a)
		return a

def stack(a): 
	print("\npoping all element of stack one b one \n")
	for i in range(0,len(a)):
			print("\n->")
			a.pop()
	return a
	
def queue(a):
	print("\ndequeue all element one b one \n")
	for i in range(0,len(a)):
			print("\n->")
			a.leftpop()
	return a

count = 0
a = []
c = int(input( "\n\n1.stack \n2.queue\n->"))
if c == 1 :
	n = input("\n1.push\n2.pop\n->")	
	while n == 2:
		e = input("\nEnter the element -> ")
		a.append(e)
		count = count + 1
		n = input("\n1.push\n2.pop\n->")
	
	for i in range(count):
			print("\n->")
			a.pop()




