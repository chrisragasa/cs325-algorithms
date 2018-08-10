
min = 100001
max = -1

def create_array(size = 10000, max = 10000):
	import random
	randoms = []
	for i in range(size):
		randoms.append(random.randrange(0, max))
	return randoms

def getLarger(a, b):
	if a > b:
		return a
	else:
		return b

def getSmaller(a, b):
	if a < b:
		return a
	else:
		return b

def min_and_max(array, start, end):
	global min
	global max
	mid = (start + end) / 2
	if end - start > 2:
		min_and_max(array, start, mid)
		min_and_max(array, mid, end)
	else:
		array = array[start:end]
		if len(array) == 1:
			array.append(array[0])
		max = getLarger(max, getLarger(array[0], array[1]))
		min = getSmaller(min, getSmaller(array[0], array[1]))
	return(min, max)


array = create_array(10, 10000)

print(array)

print(min_and_max(array, 0, len(array)))



