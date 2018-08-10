#File Object - Read
#Using context manager ... This will automatically close file when done.
with open('act.txt', 'r') as f:
    array = []
    for line in f:
    	line = line.split()
    	if line:
    		line = [int(i) for i in line]
    		array.append(line)

class Job:
	name = 0
	start = 0
	stop = 0
	def __init__(self, name, start, stop):
		self.name = name
		self.start = start
		self.stop = stop

def reformat_list(arr_in):
	newList = []
	#Reformat list of raw data into one that can be formatted
	for i in range(0, len(arr_in)):
		if len(arr_in[i]) == 1:
			tempList = []
			for j in range(i + 1, i + (arr_in[i][0] + 1)):
				tempList.append(arr_in[j])
			newList.append(tempList)

	#Turn list of lists of lists into list of lists of objects
	listOfObjects = []
	for i in range(0, len(newList)):
		tempList = []
		for j in range(0, len(newList[i])):
			job = Job(newList[i][j][0], newList[i][j][1], newList[i][j][2])
			tempList.append(job)
		listOfObjects.append(tempList)
			
	return listOfObjects

def print_listOfListsOfObjects(arr_in):
	for i in range(0, len(arr_in)):
		print("List " + str(i) + ":")
		for j in range(0, len(arr_in[i])):
			print(arr_in[i][j].name, arr_in[i][j].start, arr_in[i][j].stop)

def print_listOfObjects(arr_in):
	print("List")
	for i in range(0, len(arr_in)):
		print(arr_in[i].name, arr_in[i].start, arr_in[i].stop)
		

def last_to_start(arr_in):
	total_schedule = []
	for i in range(0, len(arr_in)):
		list_schedule = []
		for j in range(0, len(arr_in[i])):
			list_schedule.append(arr_in[i][j])
		total_schedule.append(list_schedule)

	#Sort each of the lists of obejcts by decreasing start time	
	for i in range(0, len(arr_in)):
		total_schedule[i] = sorted(total_schedule[i], key=lambda job: job.start, reverse=True)
	
	#print_listOfListsOfObjects(total_schedule)

	#Determine optimal schedules
	for i in range(len(arr_in)):

		list_of_jobs = []

		print("Set " + str(i + 1))

		n = len(total_schedule[i])
		

		#The first activity is always selected
		m = 0
		list_of_jobs.insert(0, total_schedule[i][m].name)

		#Consider the rest of the activities
		for j in range(n):
			#If activity has finish time less than or equal
			#to the start time of previously selected activity, then select it
			if total_schedule[i][j].stop <= total_schedule[i][m].start:
				list_of_jobs.insert(0, total_schedule[i][j].name)
				m = j

		print("Number of activities selected = " + str(len(list_of_jobs)))
		print("Activities:"),
		for x in range(len(list_of_jobs)):
			print(list_of_jobs[x]),

		print("\n")

def write_to(arr_in, f_in):
	for i in arr_in:
		f_in.write(str(i) + " ")
	f_in.write("\n")

def main():
	objects = reformat_list(array)
	last_to_start(objects)



	

	


if __name__ == "__main__":
	main()