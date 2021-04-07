students = [] 
for new_student in range(50):
	new_student = {'age': 18, 'grade': 'A2', 'graduated': False}
	students.append(new_student)
for student in students[:8]:
	if student['age'] == 18:
		student['age']=17
for student in students[-3:]:
	if student['graduated'] == False:
		student['graduated']=True
for student in students[:]:
	if student['graduated'] == True:
		student['grade']='undergraduate'
for student in students:
	print(student)
