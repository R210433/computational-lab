def determination(matrix):
  if (len(matrix)!=2 or len(matrix[1])!=2):
     raise valueerror("input matrix must be a 2*2 matrix")
  return matrix[0][0]*matrix[1][1]-matrix[0][1]
matrix_2=[[3,4],[3,4]]
result=determination(matrix_2)
print("Determination of 2*2 matrix",result)
