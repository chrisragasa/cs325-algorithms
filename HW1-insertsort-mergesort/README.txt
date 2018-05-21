Author: Christopher Ragasa

Project: Oregon State University, CS 325 - Algorithms, HW 1

Description: 
This project shows the implmentation of merge sort and insertion sort in Python, as well as an analysis of their best and worst case scenarios. The implementations take in input from a text file in the form of, 4 19 2 5 11, where the first element is the count of numbers to be sorted and the following elements are the numbers to be sorted. The text file could have multiple lines.
	data.txt example:
	4 19 2 5 11
	8 1 2 3 4 5 6 1 2

When the program is executed, an output file is created with the numbers sorted (excluding the first element).
	insert.out example:
	2 5 11 19
	1 1 2 2 3 4 5 6

File names ending in best_case, part2, and worst_case, display the different possible run times of the respective algorithm.

Date: 4/8/18

Running the program using the command line:
1) Navigate to the directory of the python source code files
2) In terminal, run command: python filename.py
   For example, to run the insertion sort program, type in: "python insertsort.py"
3a) If running best case, part2, or worst case files, see execution time results logged in the console.
3b) If running insertsort.py or mergesort.py, see results in filename.out output file.
   For example, to see the results of "python insertsort.py", open file "insert.out"
