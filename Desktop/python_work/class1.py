class User:
	def __init__(self, first_name, last_name):
		self.last_name=last_name
		self.first_name=first_name
		self.login_attempts=0
	def describe_user(self):
		print(f"The user's name is {self.first_name} {self.last_name}.")
	def greet_user(self):
		print(f'Hi {self.first_name} {self.last_name}!')
	def reset_login_attempts(self):
		self.login_attempts=0
	def increment_login_attempts(self):
		self.login_attempts+=1
	def show_login_attempts(self):
		print(self.login_attempts)
class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name,last_name)
		self.privileges=['can add post', 'can delete post', 'can ban user']
	def show_privileges(self):
		print('The privileges are:')
		for privilege in self.privileges:
			print(privilege)