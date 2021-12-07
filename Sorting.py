# All of these sorting algorithms run in O(n^2)

def bubble_sort(l):
	for turn in range(len(l)-1):
		for i in range(len(l)-turn-1):
			if l[i]> l[i+1]:
				# Swap the two values
				temp = l[i]
				l[i] = l[i+1]
				l[i+1] = temp

				# Alternatively, since this is python you can also do this to swap values:
				# l[i], l[i+1] = l[i+1], l[i]
				# The above line only works in python
	return


def insertion_sort(l):
	for i in range(1, len(l)):
		key = l[i]
		j = i-1
		# Move elements down by one position every tume it is 
		# less than the new position being compared to
		while j >= 0 and key < l[j]:
			l[j+1] = l[j]
			j -= 1
		l[j+1] = key
	return


def selection_sort(l):
	for i in range(len(l)):
		min_index = i
		# loop to find minimum element in remaining 
		# unsorted portion of the array
		for j in range(i+1, len(l)):
			if l[min_index] > l[j]:
				min_index = j
		# Swap minimum element with the first element from earlier
		l[i], l[min_index] = l[min_index], l[i]
	return


A = [45, 22, 10, 24, 19, 65] 
# bubble_sort(A)
# insertion_sort(A)
selection_sort(A)
print(A)
