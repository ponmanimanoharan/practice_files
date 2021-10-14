student = ["Ponmani", "Manoharan", "Tamil"]

#enumerate prints the index and value of elements in the list
for i,j in enumerate(student):
    print(i,j)

# multi-dimentional array
xx = [[1,2,3],[4,5,6]]
print(xx)
print(xx[0])
print(xx[1])

print("The list riddle")
print([] is [])
# the is operator compares whether the two objects are the same,
# thus returns false since they are identical and not the same
print([] == [])
print("This list riddle returns")
list1 = []
list2 = list1
print(list1 is list2)
print(list1 == list2)



