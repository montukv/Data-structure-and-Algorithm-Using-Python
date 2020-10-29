def quickSort(a):
	if len(a) <= 1:
		return a
	else:
		pivot = a.pop()

	greater = []
	lower = []

	for i in a:
		if i > pivot:
			greater.append(i)
		else:
			lower.append(i)
	return quickSort(lower) + [pivot] + quickSort(greater)



l = [3,4,6,2,6,8,2,1]
print(quickSort(l))