#Different sorting technique using python by montukeshwar vaishnaw

from random import randint


#QUICK SORT USING DIVIDE AND CONQURE TECHNIQUE 
def quick(a):
	if len(a)<=1:
		return a

	smallar = []
	equal = []
	large = []
	pivot = a[randint(0,len(a)-1)]
	print(pivot)
	for x in a:
		if x<pivot:		
			smallar.append(x)
		elif x==pivot:	
			equal.append(x)
		else :	
			large.append(x)

	return quick(smallar)+equal+quick(large)

#MERGE SORT USING DIVIDE AND CONQURE TECHNIQUE 
def merge_array(a,b):
	result = []
	a_idx = 0
	b_idx = 0

	while a_idx < len(a) and b_idx < len(b):
		if a[a_idx] < b[b_idx] : 
			result.append(a[a_idx])
			a_idx +=1
		else : 
			result.append(b[b_idx])
			b_idx +=1

	if a_idx == len(a):
		result.extend(b[b_idx:])
	else : 
		result.extend(a[a_idx:])

	return result

def merge(a):


	if len(a) <= 1 :
		return a
	
	left = merge(a[:int(len(a)/2)])
	right = merge(a[int(len(a)/2):])

	return merge_array(left,right)


#INSERTION SORTING TECHNIQUE
def insertion(a):

	for i in range(1,len(a)):

		curr_item = a[i]
		insert_idx = i-1

		while insert_idx >= 0 and curr_item < a[insert_idx]:
				a[insert_idx+1] = a[insert_idx] 
				insert_idx -= 1

		a[insert_idx+1] = curr_item
	return a


#BUBBLE SORTING TECHNIQUE
def bubble(a):
	for i in range(0,len(a)):
		for j in range(0,len(a)-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]

	return a





a = []
n = int(input("\nEnter the number of element in array : "))
for i in range(n):
	e = input("\nEnter elemet  :")
	a.append(e)

print("\nArray is -> ",a)
n = int(input("\nEnter your choice \n1.quick sort\n2.merge sort\n3.insertion sort\n4.bubble sort\n5.selection sort\n 6.Exit \n-> "))
while n!=6:
		
		if n==1:
			q=quick(a)
			print(q)
			break
		elif n == 2:
			m = merge(a)
			print(m)
			break
		elif n==3:
			m = insertion(a)
			print(m)
			break
		elif n == 4:

			b=bubble(a)
			print(b)
			break
		elif n ==5:
			selection(a)
			break
		elif  n  >= 7:
			print("\nWRONG INPUT \n")
			print("\n TRY AGAIN \n")

print("\n________Thankyou______\n")