current_users=['YTY','Marin','Shellin','admin','guest']
new_users=['YTY','admin','Kathin','Ritin','Melanin']
for user1 in current_users:
	for user2 in new_users:
		if user1.title() == user2.title():
			print(f'{user1.title()} already exists, please choose a different name.')
