#6-7
nurse={'income': 8000,
'work_hour': 10,
}
doctor={'income': 18000,
'work_hour': 12,
}
teacher={'income': 6000,
'work_hour': 6,
}
people=[nurse,doctor,teacher]
print(people)
#6-8
pet1={'kind':'dog', 'owner':'Franklin'}
pet2={'kind':'cat', 'owner':'Sera'}
pet3={'kind':'chicken', 'owner':'Tyler'}
pet4={'kind':'goose', 'owner':'Tyler'}
pets=[pet1,pet2,pet3,pet4]
for pet in pets:
	print(pet['kind'])
#6-9 
favorite_places={
	'Tyler':'Yucca Valley',
	'Sera':'Car rooftop',
	'Franklin':'Dog house',
}
for name, place in favorite_places.items():
	print(f"The favorite place of {name} is {place}")
#6-10 & 6-12
favorite_numbers={
	'Tyler':[12,18],
	'Sera':[13],
	'Franklin':[2,6,9],
}
for name, numbers in favorite_numbers.items():
	if numbers[-1] == numbers[0]:
		print(f"\n{name}'s favorite language is:")
	else:
		print(f"\n{name}'s favorite languages are:")
	for number in numbers:
		print(f'\t{number}')
#6-11
cities = {
	'Nanjing':{
		'country':'China',
		'population':'large',
		'fact':'It is the capital of Republic of China.',
		},
	'Paris':{
		'country':'France',
		'population':'medium',
		'fact':'It is one of the most artisitic cities in the world.',
		},
	'South Pasadena':{
		'country':'United States',
		'population':'small',
		'fact':'Tyler spent two years studying there.',
		},
}
for city, city_info in cities.items():
	print(f'\nCity name: {city}')
	print(f"It is in {city_info['country']} with a {city_info['population']} population.")
	print(city_info['fact'])