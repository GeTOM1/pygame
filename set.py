sample_list = [1, 1, 2, 2, 3, 3, 3]

sample_set = set(sample_list)

#print(sample_set[2])

print(sample_set)

if 4 in sample_set:
    print("Yes")
else:
    print("No")

myset = set([])
myset.add(3)
myset.add(3)
myset.add(2)
myset.add(1)

print(myset)

myset.remove(1)
myset.discard(5)

print(myset)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)

print(a.symmetric_difference(b))
print(a ^ b)