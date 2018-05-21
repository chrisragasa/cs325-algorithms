#Best case scenario for merge sort is creating an array that is already sorted
def create_array(size = 10000, max = 10000):
    array = []
    for i in range(0, size):
        array.append(i)
    return array


def merge(a, b):
    c = [] # final output array
    a_idx, b_idx = 0,0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx+=1
        else:
            c.append(b[b_idx])
            b_idx+=1
    if a_idx == len(a): c.extend(b[b_idx:])
    else:               c.extend(a[a_idx:])
    return c

def merge_sort(a):
    # a list of 0 or 1 elements is sorted by definition
    if len(a) <= 1: return a

    # split list in half and call merge sort recursively on each half
    left, right = merge_sort(a[:len(a)/2]), merge_sort(a[len(a)/2:])

    # merge the now-sorted sublists
    return merge(left, right)

def write_to(arr_in, f_in):
    for i in arr_in:
        f_in.write(str(i) + " ")
    f_in.write("\n")

def print_execution_time(n, arr):
    import timeit
    start = timeit.default_timer()
    merge_sort(arr)
    stop = timeit.default_timer()
    print("Merge Sort, n = " + str(n) + ", time: " + str(stop - start))

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


