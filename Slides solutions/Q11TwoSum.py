def two_sum_inefficient(nums, target):

	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]
	return None


def two_sum_efficient(nums, target):

	pair = {}

	for i in range(len(nums)):
		if target - nums[i] in pair:
			return [pair[target - nums[i]], i]
		else:
			pair[nums[i]] = i

	return None


sol = two_sum_inefficient([3, 2, 4], 6)
print(sol)