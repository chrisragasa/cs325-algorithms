def create_array(size = 10000, max = 10000):
	import random
	randoms = []
	for i in range(size):
		randoms.append(random.randrange(0, max))
	return randoms

def stoogesort(arr, l = 0, h = None):
    if h is None:
    	h = len(arr) - 1

    # If first element is smaller
    # than last,swap them
    if arr[h]<arr[l]:
       arr[l], arr[h] = arr[h], arr[l]
  
    # If there are more than 2 elements in
    # the array
    if h - l > 1:
        t = (h - l + 1) // 3
  
        # Recursively sort first 2/3 elements
        stoogesort(arr, l, h-t)
  
        # Recursively sort last 2/3 elements
        stoogesort(arr, l+t, h)
  
        # Recursively sort first 2/3 elements
        # again to confirm
        stoogesort(arr, l, h-t)
    return arr
 
def write_to(arr_in, f_in):
	for i in arr_in:
		f_in.write(str(i) + " ")
	f_in.write("\n")

def print_execution_time(n, arr):
	import timeit
	start = timeit.default_timer()
	stoogesort(arr)
	stop = timeit.default_timer()
	print("Stoogesort, n = " + str(n) + ", time: " + str(stop - start))


def main():
	# create arrays for benchmarking
	array100 = create_array(10, 100)
	array200 = create_array(20, 100)
	array300 = create_array(40, 100)
	array400 = create_array(80, 100)
	array500 = create_array(160, 100)
	array600 = create_array(320, 100)
	array700 = create_array(640, 100)




	# benchmark each mergesort
	print_execution_time(10, array100)
	print_execution_time(20, array200)
	print_execution_time(40, array300)
	print_execution_time(80, array400)
	print_execution_time(160, array500)
	print_execution_time(320, array600)
	print_execution_time(640, array700)

if __name__ == "__main__":
	main()


