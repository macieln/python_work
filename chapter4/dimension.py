dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# this causes an error because tuples are immutable
# dimensions[0] = 250
for dimesion in dimensions:
    print(dimesion)

print('\n\nOriginal dimensions: ')
for dimesion in dimensions:
    print('\t' + str(dimesion))

dimensions = (400, 100)
print('\nModified dimensions: ')
for dimesion in dimensions:
    print('\t' + str(dimesion))
