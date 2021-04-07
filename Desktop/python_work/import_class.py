#from class1 import Admin
#new_admin=Admin('Tianyi','Yang')
#new_admin.show_privileges()
from random import choice
names=['Tyler','Maria','Joe','Josie','Amber','Jesse','Lister','Daisy','Luke','Natalia']
current_number=1
while current_number <=5:
	print(f"{choice(names)}, you're next!")
	current_number+=1
