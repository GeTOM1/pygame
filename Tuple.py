stuDetails=('Surabhi', 89)

address=('227', 'Brickfield Shelters', 'Bandalore', 'Karnataka', '562107')

for x in address:
    print(x, end='')

houseno, apartName, city, state, pin = address

print()
print('HNO', houseno)
print('APTNO', apartName)
print(city)
print(state)
print(pin)

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(my_tuple[0][3])
print(my_tuple[1][1])

my_tuple=('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(my_tuple[1:4])

print(my_tuple[:-7])

print(my_tuple[7:])

print(my_tuple[:])

my_tuple=(4, 2, 3, [6, 5])

my_tuple[3][0]=9
print(my_tuple)

print(my_tuple)