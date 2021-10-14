# - Create a variable named `numbers`
numbers = [4,5,6,7]
#   with the following content: `[4, 5, 6, 7]`
# - Print all the elements of `numbers`
print(numbers)
print(numbers[2])
firstArrayOfNumbers = [1,2,3]
secondArrayOfNumbers = [4,5]
if len(secondArrayOfNumbers) > len(firstArrayOfNumbers):
    print("secondArrayOfNumbers is longer")
else:
    print("firstArrayOfNumbers")

print("\n")

numbers  = [54,23,66,12]
print(numbers[1]+numbers[2])

num = [1,2,3, 8,5,6]
num[3] = 4
print(num[3])

num =[1,2,3,4,5]
print(num[2]+1)
mat = []
for i in range(0,4):
    row = []
    mat.append(row)
    for j in range(0,4):
        if i==j:
            row.append(1)
        else:
            row.append(0)
print(mat)

numlist = [3,4,5,6,7]
for x in numlist:
    print(x*2)

colors = [['lime','forest green','olive','pale green','spring green'],
 ['orange red', 'red','tomato'],
 ['orchid','violet','pink','hot pink']]

animals = ["koal", "pand", "zebr"]
for x in animals:
    x = x+'a'
    print(x)

orders = ["first", "second", "third"]
temp = orders[0]
orders[0] = orders[2]
orders[2] = temp
print(orders)

numbers = [3, 4, 5, 6, 7]
num = 0
for i in numbers:
    num += i
print(num)

numbers = [3, 4, 5, 6, 7]
numbers.reverse()
print(numbers)



