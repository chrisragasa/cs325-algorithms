#Best case scenario for insertion sort is creating an array that is already sorted
def create_array(size = 10000, max = 10000):
    array = []
    for i in range(0, size):
        array.append(i)
    return array

def insertion_sort(a):
    # start with the 2nd element in the array
    for i in range(1, len(a)):
        # iterate through the values to the left of i to compare
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
    return a

def write_to(arr_in, f_in):
    for i in arr_in:
        f_in.write(str(i) + " ")
    f_in.write("\n")

def print_execution_time(n, arr):
    import timeit
    start = timeit.default_timer()
    insertion_sort(arr)
    stop = timeit.default_timer()
    print("Insertion Sort, n = " + str(n) + ", time: " + str(stop - start))
		

def main():
    # create arrays for benchmarking
    array1000 = create_array(1000, 10000)
    array2000 = create_array(2000, 10000)
    array5000 = create_array(5000, 10000)
    array7000 = create_array(7000, 10000)
    array10000 = create_array(10000, 10000)
    array12000 = create_array(12000, 10000)
    array15000 = create_array(15000, 10000)

    # benchmark each mergesort
    print_execution_time(1000, array1000)
    print_execution_time(2000, array2000)
    print_execution_time(5000, array5000)
    print_execution_time(7000, array7000)
    print_execution_time(10000, array10000)
    print_execution_time(12000, array12000)
    print_execution_time(15000, array15000)

if __name__ == "__main__":
    main()


