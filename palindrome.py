#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

file = open("words.txt", "r")
count = 0
for line in file:
    word = line.strip()
    if word == word[::-1]:
        count += 1

file.close()
print("Number of palindromes:", count)