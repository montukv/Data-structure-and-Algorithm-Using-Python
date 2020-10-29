def selectionSort(s):
	for i in range(len(s)):
		cur_index = i
		for j in range(i,len(s)):
			if s[cur_index] > s[j]:
				cur_index = j
		s[i],s[cur_index] = s[cur_index],s[i]
	return s
s = [3,2,1,5,4]
print(selectionSort(s))