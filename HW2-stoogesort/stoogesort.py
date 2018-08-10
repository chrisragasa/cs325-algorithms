#File Object - Read
#Using context manager ... This will automatically close file when done.
with open('data.txt', 'r') as f:
    array = []
    for line in f:
    	line = line.split()
    	if line:
    		line = [int(i) for i in line]
    		array.append(line)

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

def main():
	f_out = open('stooge.out', 'w')
	
	for i in range(0, len(array)):
		my_array = array[i][1:]
		stoogesort(my_array)
		write_to(my_array, f_out)

	f_out.close()
	

if __name__ == "__main__":
	main()


