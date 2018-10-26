"""
Author: Yost
Title: Lab 2H
Date: 6 Sep 2018

Lab 2H

Create a program that takes input of a group of students' names and grades... then sorts 
them based on highest to lowest grade. Then calculate and print the sorted list and the 
average for the class. (Hint: Use Dictionaries!)
"""

def grades():
    dict = {}
    sum = 0
#for the loop
	boolX = True
    while boolX == True:
	    choice = raw_input("Would you like to (1)add a student, (2)view the list and class average, or (3)leave?\n")
#add a student
	    if choice == '1': 
	        name = raw_input("Enter the student's name to add.\n")
			grade = raw_input("Enter the student's grade as a number.\n")
#convert the string to an int
			grade = int(grade)
			dict[name] = grade
#add up the grades for taking the average later
			sum+=grade
#view the list and the average
	    elif choice == '2':
#sort the dictionary in reverse order by value (greatest value first)
	        dict_sorted = sorted(dict, key=dict.get, reverse=True)
			for v in dict_sorted:
			    print v, ":", dict[v]
#calculate and print the average using len(dict)
            print "The class average of {} students is {}.".format(len(dict), float(sum/len(dict)))
#leave the program
	    elif choice == '3':
		    boolX = False
#invalid choice
	    else:
	        print "That is not a valid choice.  Please type 1, 2, or 3 and hit <Enter>.\n"