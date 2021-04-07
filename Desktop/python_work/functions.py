def class_list(class_name, *student_name):
	print(f'Here is the list of students that belongs to class {class_name}:')
	for student in student_name:
		print(f'\t{student}')
def cars(brand, type, **car_info):
	car_info['brand']=brand
	car_info['type']=type
	return car_info