#Create an array of size 10000 with random numbers from 0 to 99
def create_array(size = 10000, max = 10000):
    import random
    randoms = []
    for i in range(size):
        randoms.append(random.randrange(0, max))
    return randoms

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
    '''
    array100 = create_array(100, 100)
    array200 = create_array(200, 200)
    array300 = create_array(300, 300)
    array400 = create_array(400, 400)
    array500 = create_array(500, 500)
    array600 = create_array(600, 600)
    array700 = create_array(700, 700)
    array800 = create_array(800, 800)
    array900 = create_array(900, 900)
    '''
    array100 = create_array(10, 100)
    array200 = create_array(20, 200)
    array300 = create_array(40, 300)
    array400 = create_array(80, 400)
    array500 = create_array(160, 500)
    array600 = create_array(320, 600)
    array700 = create_array(640, 700)

    # benchmark each mergesort
    print_execution_time(100, array100)
    print_execution_time(200, array200)
    print_execution_time(300, array300)
    print_execution_time(400, array400)
    print_execution_time(500, array500)
    print_execution_time(600, array600)
    print_execution_time(700, array700)
    #print_execution_time(800, array800)
    #print_execution_time(900, array900)


if __name__ == "__main__":
    main()


