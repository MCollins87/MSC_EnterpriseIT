# Name: Mark Collins
# Student ID: 12696434
# Python code to sort a provided set of data on the file pidata.txt, using the merge sort algorythm 
# Output is a .txt file named MarkCollinsy_yyyy-mm-dd.txt
# Pre-requisites: numpy; datetime
# version 1.1 2024-06-12
###############################################################
# Change log: 
# v.0.1:    - Working algorythm with timers. 
# v.0.2:    - Added inserting name randomly througout the sorted list. 
# v.0.3:    - Added count= to np.fromfile to measure time for different list lengths. 
#           - Added keyboard inputs for name and student number (hashed out for performance testing)
# v1.0:     - Added hash function
# v1.1      - Added Bubble sort and Python list.sort() ready for submission

# Split array into individual elements and then call function to merge back together
def mergesort(data):
    # If the array is less than or equal to 1, then it is already sorted
    if len(data) <= 1:
        return data
    # Find mid-point. Use // to floor round, avoiding floats when len(data) is odd
    mid = len(data) // 2
    # Recursivly call function on each half
    Lt = mergesort(data[:mid])
    Rt = mergesort(data[mid:])
    # Merge the sorted halves
    return merge(Lt, Rt)

# Function to merge back into sorted list
def merge(L, R):
    # Create a holding array for sorted data
    sorted_data = []
    # Set index counters to 0
    i = j = 0
    # Compare each element. Append the lower value to the sorted array
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            sorted_data.append(L[i])
            i += 1
        else:
            sorted_data.append(R[j])
            j += 1
    # Collect any remaining elements and tack onto the end before next itteration
    sorted_data.extend(L[i:])
    sorted_data.extend(R[j:])
    # Return the sorted data
    return sorted_data

#Bubble sort code
def bubblesort(data):
   
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

# Execution code
# Import pre-requisites
import numpy as np
import datetime
# Ask for name and Student ID
Uname = input("Please enter name:")
sid = input("Please enter Student ID:")
# Start Timer
start = np.datetime64(datetime.datetime.now())
# Import data. abs because it kept reading -ve values. 
# dtype to force integer, and sep to read white space as number seperator
data = abs(np.fromfile("pidata.txt", dtype=int, count=-1, sep = " "))#
# Display the number of elements to be sorted
print("number of elements to be sorted: " , len(data))
# Record the time to calculate import time and sort time.
sortstart = np.datetime64(datetime.datetime.now())
# Call the Merge sort function
sorted_data = mergesort(data)
# Uncomment the next to use Bubble sort
# sorted_data = bubblesort(data)
# Uncomment the next lines to use the built-in Python function
#sorted_data = data.sort()
#sorted_data = np.ndarray.tolist(data)
# Insert name and student ID in first two lines. 
sorted_data.insert(0, "Name: " + Uname)
sorted_data.insert(1, "ID: " + sid)
# Insert name 10 times randomly in result
k = 0
for k in range(10):
    sorted_data.insert(np.random.randint(2, len(sorted_data)), Uname + str(k+1))
# Record the time to calculate sort time and export time
sortend = np.datetime64(datetime.datetime.now())
# Save the file. %s to allow string with name.
np.savetxt(Uname+"_"+ str(np.datetime64(datetime.date.today()))+".txt", sorted_data, fmt="%s")
# End timer
end = np.datetime64(datetime.datetime.now())
# Display times for execution:
print("Time to import data: ", np.timedelta64(sortstart - start))
print("Time to sort: ", np.timedelta64(sortend - sortstart))
print("Time to save file: ", np.timedelta64(end - sortend))
print("Total time to execute: ", np.timedelta64(end - start))
print("Hash value for sorted data is: " + str(hash(tuple((sorted_data)))))