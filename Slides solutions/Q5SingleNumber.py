def single_number(nums):
	seen = []

	for i in nums:
		if i in seen: 
			seen.remove(i)
		else:
			seen.append(i)

	return seen[0]


sol = single_number([2, 3, 5, 6, 3, 2, 6])
print(sol)