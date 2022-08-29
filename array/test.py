# from myarray import Array2D

# arr = Array2D(3, 2)
# arr[0, 0] = 0
# arr[0, 1] = 1
# arr[1, 0] = 2
# arr[1, 1] = 3
# arr[2, 0] = 4
# arr[2, 1] = 5

# print(arr.numRows())
# print(arr.numCols())


from matrix import Matrix

m = Matrix(3, 2)

m[0, 0] = 0
m[0, 1] = 1
m[1, 0] = 2
m[1, 1] = 3
m[2, 0] = 4
m[2, 1] = 5

print("Rows : ", m.numRows())
print("Columns : ", m.numCols())
m.plotmatrix()
nm = m.transpose()
print("Rows : ", nm.numRows())
print("Columns : ", nm.numCols())
nm.plotmatrix()
