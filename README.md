# matrixmultiplication
 Import this document to multiply matricies together in python.

 Methods and Attributes:

 variable_name = matrix(numberOfRows, numberOfColumns, Name{must be a string}) - by default all values are set to 0
 variable_name.edit_mat(rowIndex, columnIndex, newValue)

 other_matrix_variable_name = multiply_matrix(any_matrix, another_matrix)

 random_vector_name = vector(Name{must be a string}, i-value, j-value, k-value)
 - if vector is 2d input k as 0

 random_vector_name.printVect(Form, AngleType)
 Forms:
 "Pol" - polar form
 "Col" - column form 
 "Com" - component form

 AngleTypes:
 0 - radians
 1 - degrees

 Angles type will only affect polar form. A value is still required for other forms but the value can be arbituary.



