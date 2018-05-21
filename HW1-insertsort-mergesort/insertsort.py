#File Object - Read
#Using context manager ... This will automatically close file when done.
with open('data.txt', 'r') as f:
    array = []
    for line in f:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            array.append(line)

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

def main():
    f_out = open('insert.out', 'w')

    for i in range(0, len(array)):
        write_to(insertion_sort(array[i][1:]), f_out)

    f_out.close()

if __name__ == "__main__":
    main()


