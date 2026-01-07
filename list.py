matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(len(matrix))
print(matrix[0])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()

row=int(input("Please enter a value: "))
col=int(input("please enter a value: "))
matrix=[]
for i in range(row):
    temp=[]
    for j in range(col):
        value=int(input("Please enter a value: "))
        temp.append(value)
    matrix.append(temp) 
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()
       