"""
Returns a list of the min and max of a list of numbers.
Takes one argument, a list of numbers

sorts the numbers from ascending 
to descedning order then get get min and max number

"""
def find_max_min(list_of_numbers):

	list_of_min_max_numbers = []

	list_of_numbers.sort() # Sort from lowest to highest


	# check if the min number is the same as the max number and return the length of the list
	if list_of_numbers[0] == list_of_numbers[-1]:

		list_of_min_max_numbers.append(len(list_of_numbers))

	# Add to new list
	else:
		list_of_min_max_numbers.append(list_of_numbers[0])
		list_of_min_max_numbers.append(list_of_numbers[-1])

		
	return list_of_min_max_numbers

