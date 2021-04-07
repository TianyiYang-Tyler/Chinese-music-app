invite=['Marin','Christin','Shellin']
not_available='Christin'
invite.remove(not_available)
print(f'{not_available} is not able to attend')
new_comer='Kathin'
invite.append(new_comer)
print('Dear all, a XL table is available')
new_comer='Ritin'
invite.insert(0,new_comer)
new_comer='Melanin'
invite.insert(2,new_comer)
new_comer='Charolin'
invite.append(new_comer)
print(f'I invite {invite[0]} to attend')
print(f'I invite {invite[1]} to attend')
print(f'I invite {invite[2]} to attend')
print(f'I invite {invite[3]} to attend')
print(f'I invite {invite[4]} to attend')
print(f'I invite {invite[5]} to attend')
print('The table cannot be delivered on time, so only two guests may come')
guest_popped=invite.pop()
print(f'I am sorry to inform that {guest_popped} is not able to attend')
guest_popped=invite.pop()
print(f'I am sorry to inform that {guest_popped} is not able to attend')
guest_popped=invite.pop()
print(f'I am sorry to inform that {guest_popped} is not able to attend')
guest_popped=invite.pop()
print(f'I am sorry to inform that {guest_popped} is not able to attend')
print(f'I am glad to inform that {invite[0]} is able to attend')
print(f'I am glad to inform that {invite[1]} is able to attend')
del invite[0]
del invite[1]
print(invite)