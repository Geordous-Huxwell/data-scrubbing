import os
import csv


invalid_names = []
clean_names = []


def name_judger(name_list):			#determines whether an entry can be cleaned or is invalid

	for name in name_list:			#iterate through names in list
		
		if not isinstance(name, str):		#checks for non-string types, sends to invalid list if not string
			invalid_names.append(name) 
			continue
		
		if name.count("-") > 1:
			invalid_names.append("-")
			continue

		char_counter = 0			#counter to compare against length of string which determines when we're at the end of it
		
		for char in name:			#iterate through characters in name
			char_counter += 1
			
			if char.isalpha() == True or char == "-":		#checks that character is one of alpha type or is a hyphen, sends to invalid list if not
				
				if name == None:			#checks for empty string entries, sends name to invalid list if true
					invalid_names.append(name)
					break
				
				if char_counter == len(name)-1:		#determines end of string, move to final check
					
					if name.count("-") > 1:			#check for multiple hyphens
						invalid_names.append(name)
						break
					else:
						name = name.title()			#clean entry to required format
						clean_names.append(name)	#add to list of cleaned names
						break
							
			else:
				invalid_names.append(name)
				break
		

	return invalid_names, clean_names			#return 2 lists as a tuple to the original call

def input_check():
	
	while True:
		try:
			userin = input("Which file would you like to use?\n Press 1 for 10,000 Names\n Press 2 for 100,000 Names\n Press 3 for 10,000,000 Names\n")
			userin = int(userin)			
			break	
		except ValueError:
			print("Invalid input. Please select option 1, 2, or 3.\n")

	if userin == 1:
		file_name = "10000DirtyNames.csv"
	elif userin == 2:
		file_name = "100000DirtyNames.csv"
	elif userin == 3:
		file_name = "10000000DirtyNames.csv"
	else:
		print("Invalid input. Please select option 1, 2, or 3.\n")
		file_name = input_check()
		return file_name

	print("You have selected: " + str(file_name))

	return file_name


with open(input_check(), "r") as file:			#opens file with readable permission

	name_list = file.read()						#establish file reader
	name_list = (name_list.split(","))			#convert to comma-separated list
	name_judger(name_list)						#call judgement function on the list of entries

	
	if len(invalid_names) + len(clean_names) == len(name_list):			#check that qunatity of output matches quantity of input
		print("All names accounted for, sir.")
		
	else:
		print("You are missing names, dumbass!")
		
		print("Invalid length:" + str(len(invalid_names)))
		print("Clean length: " + str(len(clean_names)))
		print("Total of new list: " + str(len((invalid_names))+(len(clean_names))))
		print("Total original list: " + str(len(name_list)))
		print("Number of missing entries: " + str(len(name_list)-len(clean_names)-len(invalid_names)))
		

		a = set(clean_names)&set(invalid_names)			
		print("Entries present in both lists:") 
		print(a)

		b = set(invalid_names)&set(name_list)
		print("Number of mutated invalid_names:")
		print(len(name_list)-len(clean_names)-len(b))
	
	clean_file = open("CleanNames.csv", "w")			#insantiate clean file
	writer = csv.writer(clean_file)						#establish writer
	writer.writerow(clean_names)						#write list to csv
	clean_file.close()

	invalid_file = open("InvalidNames.csv", "w")
	writer = csv.writer(invalid_file)
	writer.writerow(invalid_names)
	invalid_file.close()
	
