from matmult import *
#imports the matrix multiplication file. It needs to be in same folder as this file.

print("")
matrix_a = matrix(2, 2, "A")
#This creates a 2x2 matrix.

print("")
matrix_a.printMat()
#This prints the matrix. It currently has 0 in all positions.


matrix_a.edit_mat(0, 1, 5)
#This changes the value in the 0th row in the 1st column to a 5.

matrix_a.edit_mat(0, 1, 3)
matrix_a.edit_mat(1, 0, 2)
matrix_a.edit_mat(1, 1, 1)
#Other values were imputed into the matrix.

print("")
matrix_a.printMat()
#This prints the new matrix.


matrix_b = matrix(2, 2, "B")
#This creates a new matrix.

matrix_b.mat_array = multiply_matrix(matrix_a, matrix_a)
#This sets matrix_b to matrix_a multiplied by itself

print("")
matrix_b.printMat()
#This prints matrix_b, aka matrix_a^2



vector_a = vector("A", 6, 4, 2)
#This creates a vector with the name of A

print("")
vector_a.printVect("Pol", 0)
#This prints the vector in polar form and the angles are in radians

print("")
vector_a.printVect("Pol", 1)
#This prints the vector in polar form and the angles are in degrees

print("")
vector_a.printVect("Col", 0)
#This prints the vector in column form

print("")
vector_a.printVect("Com", 0)
#This prints the vector in component form












