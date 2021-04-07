filename='pi_million_digits.txt'
number=0
with open(filename) as file_object:
	lines=file_object.readlines()
pi_string=''
for line in lines:
	pi_string+=line.strip()
while number != 100000:
	if str(number) not in pi_string:
		print(number)
	number+=1