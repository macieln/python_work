pizzas = ['hawaiian', 'pepperoni', 'cheese']
for pizza in pizzas:
    print('I like ' + pizza.title() + ' pizza.')

print('My favorite Pizza is cooked in wood oven, has thin and chrunchy crust.')

my_pizzas = pizzas[:]
my_pizzas.append('truffle shuffle')
friend_pizzas = pizzas[:]
friend_pizzas.append('jersy jerk')

print('\n\nMy favorite pizzas are:')
for pizza in my_pizzas:
    print('\t' + pizza.title())

print("\n\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print('\t' + pizza.title())
