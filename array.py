#array in python by montukeshwar vaishnaw
def sum(a1,a2):
	#addition of two array
	result = []
	for i in range(0,len(a1)):
		sum = a1[i]+ a2[i]
		result.append(sum)

	print(result)


def sub(a1,a2):
	result = []
	for i in range(0,len(a1)):
		sum = a1[i] - a2[i]
		result.append(sum)

	print(result)

def mul(a1,a2):
	result = []
	for i in range(0,len(a1)):
		sum = a1[i] * a2[i]
		result.append(sum)

	print(result)

def div(a1,a2):
	result = []
	for i in range(0,len(a1)):
		sum = a1[i] / a2[i]
		result.append(sum)

	print(result)



a1 = [1,2,3,4,5,6,7,8]
a2 = [8,7,6,5,4,3,2,1]
n = int(input("\nEnter your choice \n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.Exit\n -> "))
while n!=5:
	if n==1:
		sum(a1,a2)
		break
	elif n == 2:
		sub(a1,a2)
		break
	elif n==3:
		mul(a1,a1)
		break
	elif n == 4:
		div(a1,a2)
		break
	elif n >= 6:
		print("Wrong input")
		break

print("\n________Thankyou______\n")
