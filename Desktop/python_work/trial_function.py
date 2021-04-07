def cambridge_student(a_stars,ethnicity,*age):
	if a_stars >= 4:
		return True
	elif ethnicity == 'Black' and age>18:
		return True
	else:
		return False
