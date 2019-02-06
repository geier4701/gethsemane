def validate_list_input(choice_count: int, user_input: str):
	parsed_input: int
	valid = True
	
	try:
		parsed_input = int(user_input)
	except ValueError:
		valid = False
	
	if valid:
		if parsed_input > choice_count or parsed_input < 1:
			valid = False
	
	return valid
