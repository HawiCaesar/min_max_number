
def find_max_min(list_of_numbers):

	list_of_min_max_numbers = []

	max_number = max(list_of_numbers)
	min_number = min(list_of_numbers)

	if max_number == min_number:
		#list_of_min_max_numbers[max_number]
		list_length = len(list_of_numbers)
		list_of_min_max_numbers.append(list_length)

	else:
		list_of_min_max_numbers.append(min_number)
		list_of_min_max_numbers.append(max_number)

		
	return list_of_min_max_numbers




