#4-3
values=[value for value in range(1,21)]
#print(values)
#4-4
#values=[value for value in range(1,1000001)]
#print(values)
#4-5
values1=[value1 for value1 in range(1,1000001)]
#print(sum(values1))
#print(max(values1))
#print(min(values1))
#4-6
values2=[value2 for value2 in range(1,21,2)]
#print(values2)
#4-7
values3=[value3 for value3 in range(3,31,3)]
#print(values3)
#4-8
cubes=[]
for value4 in range(1,11):
	cube=value4**3
	cubes.append(cube)
#print(cubes)
#4-9
values5=[value5**3 for value5 in range(1,11)]
#print(values5)
#4-10
print(f'The first three itmes in the cube list are {cubes[:3]}')
print(f'Three itmes from the middle of the cube list are {cubes[3:6]}')
print(f'The last three itmes in the cube list are {cubes[-3:]}')
