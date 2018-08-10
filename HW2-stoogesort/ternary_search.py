def ternary_search(arr, key):
	left = 0
	right = len(arr) - 1
	while left <= right:
		idx1 = left
		idx2 = left + (right - left) // 3
		idx3 = left + 2 * (right - left) // 3
		if key == arr[left]:
			return left
		elif key == arr[right]:
			return right
		elif key < arr[left] or key > arr[right]:
			return -1
		elif key <= arr[idx2]:
			right = idx2
		elif key > arr[idx2] and key <= arr[idx3]:
			left = idx2 + 1
			right = idx3
		else:
			left = idx3 + 1
	return

array = [1,2,3,4,5]
print(ternary_search(array,3))
