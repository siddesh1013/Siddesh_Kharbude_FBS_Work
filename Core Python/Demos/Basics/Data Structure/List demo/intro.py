#1. structure: []
li = [10, 20, 30, 40, 3.14, 'abc', 10]
print(type(li))

#2. types of data: Heterogenous
print(li)

#3. sequence: ordered

#4. changable: mutable
li = [10, 20, 50, 40, 3.14, 'abc', 10]
print(li)

#5. duplication: allowed
print(id(li))
li[2] = 50
print(id(li))