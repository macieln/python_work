my_guest = ['mom', 'dad', 'stephanie', 'luis', 'dulce', 'sam']
invite_message = ' I would like you to come to my dinner party on Wednesday.'
print('\n'+my_guest[0].title() + invite_message)
print(my_guest[1].title() + invite_message)
print(my_guest[2].title() + invite_message)
print(my_guest[3].title() + invite_message)
print(my_guest[4].title() + invite_message)
print(my_guest[5].title() + invite_message)

cancel_message = ' will not be making it to dinner.'
print('\n' + my_guest.pop(1).title() + cancel_message)
print(my_guest.pop(3).title() + cancel_message)

coming_message = ' is still making it for dinner.'
print('\n' + my_guest[0].title() + coming_message)
print(my_guest[1].title() + coming_message)
print(my_guest[2].title() + coming_message)
print(my_guest[3].title() + coming_message)
