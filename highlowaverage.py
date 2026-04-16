#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

file = open("numbers.txt", "r")
numbers = []
for line in file: 
    numbers.append(int(line.strip()))
file.close()

count = len(numbers)
total = sum(numbers)
average = total / count
highest = max(numbers)
lowest = min(numbers)

print("Count:", count)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)