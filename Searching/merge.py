a1 = [1, 3, 5]
a2 = [2, 4, 6]
a3 = [0] * (len(a1) + len(a2))

def merge(a1, s1, e1, a2, s2, e2, a3, s3):
	i = s1
	j = s2
	k = s3
	while i <= e1 and j <= e2:
		if a1[i] <= a2[j]:
			a3[k] = a1[i]
			i += 1
		else:
			a3[k] = a2[j]
			j += 1
		k += 1
	while i <= e1:
		a3[k] = a1[i]
		i += 1
		k += 1
	while j <= e2:
		a3[k] = a2[j]
		j += 1
		k += 1


merge(a1, 0, len(a1) - 1, a2, 0, len(a2) - 1, a3, 0)
print(a3) # Output: [1, 2, 3, 4, 5, 6]