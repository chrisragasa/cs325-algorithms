#File Object - Read
#Using context manager ... This will automatically close file when done.
with open('data.txt', 'r') as f:
    array = []
    for line in f:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            array.append(line)

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

def main():
    f_out = open('merge.out', 'w')

    for i in range(0, len(array)):
        write_to(merge_sort(array[i][1:]), f_out)

    f_out.close()

if __name__ == "__main__":
    main()


