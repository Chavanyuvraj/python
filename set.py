set={1,2,3,4}
print(type(set))
set.add(5)
print(set)
set.remove(1)

print(set)
set.clear()
print(set)

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))