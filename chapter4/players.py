players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

print(players[:4])
print(players[2:])


print(players[-3:])

print('Here are the first three players in my team: ')
for player in players[:3]:
    print(player.title())


print('\n\nThe first three players of the list are: ')
print(players[:3])
print('\n\nThe middle three players of the list are: ')
print(players[1:4])
print('\n\nThe last three players of the list are: ')
print(players[-3:])
