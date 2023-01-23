import numpy as np


def determinantOfMatrix(mat):
    determine = mat[0][0]*(mat[1][1]* mat[2][2] - mat[2][1] * mat[1][2]) - mat[0][1]*(mat[1][0]*mat[2][2]-mat[2][0]*mat[1][2]) + mat[0][2]*(mat[1][0]*mat[2][1] - mat[2][0]*mat[1][1])

    return determine



def findSolution(coeff):
   Dx = [
     [coeff[0][3],coeff[0][1], coeff[0][2]],
     [coeff[1][3],coeff[1][1], coeff[1][2]],
     [coeff[2][3],coeff[2][1], coeff[2][2]],
   ]

   Dy = [
    [coeff[0][0], coeff[0][3], coeff[0][2]],
    [coeff[1][0], coeff[1][3], coeff[1][2]],
    [coeff[2][0], coeff[2][3], coeff[2][2]]
   ]

   Dz = [
    [coeff[0][0], coeff[0][1], coeff[0][3]],
    [coeff[1][0], coeff[1][1], coeff[1][3]],
    [coeff[2][0], coeff[2][1], coeff[2][3]]
   ]

   D = determinantOfMatrix(coeff)
   DX = determinantOfMatrix(Dx)
   DY = determinantOfMatrix(Dy)
   DZ = determinantOfMatrix(Dz)

   x = DX/D
   y = DY/ D
   z = DZ/ D

   print("Determine of main matrix : ", D)
   print("Determine of DX matrix : ", DX)
   print("Determine of DY matrix : ", DY)
   print("Determine of DZ matrix : ", DZ)

   return [x, y ,z]



coeff = np.random.randint(-5, high=10, size=(3, 4))


print("Main Matrix: ")
print(coeff)
results = findSolution(coeff)

print("Value of coefficient x , y & z : ",results)


