import math


class vector():
	def __init__(self, vector_name, i, j, k):
		
		self.name = vector_name
		self.i = i 
		self.j = j
		self.k = k

	def printVect(self, form, rad):
		
		print(self.changeForm(form, rad, 3))
		return "Three-Dimensional"

		

	def changeForm(self, form, rad, dimension):
		

		if form == "Com":
			return f'Vector-{self.name} = {self.i}i + {self.j}j + {self.k}k'
		elif form == "Col":
			return f'Vector-{self.name}:\n|{self.i}| \n|{self.j}| \n|{self.k}|'	
		elif form == "Pol":

			if rad == 0:

				self.magnitude = math.sqrt((self.i)*(self.i)+(self.j)*(self.j)+(self.k)*(self.k))
				self.angle_1 = math.atan(self.j/self.i)
				self.angle_2 = math.asin(self.k/self.magnitude)
				return f'Vector-{self.name} = ({round(self.magnitude, 2)} , {round(self.angle_1, 2)} , {round(self.angle_2, 2)})'	

			if rad == 1:
				
				self.magnitude = math.sqrt((self.i)*(self.i)+(self.j)*(self.j)+(self.k)*(self.k))
				self.rad_convert = 180/math.pi
				self.angle_1 = math.atan(self.j/self.i)
				self.angle_1 = self.angle_1 * self.rad_convert
				self.angle_2 = math.asin(self.k/self.magnitude)
				self.angle_2 = self.angle_2 * self.rad_convert
				return f'Vector-{self.name} = ({round(self.magnitude, 2)} , {round(self.angle_1, 2)}\N{DEGREE SIGN} , {round(self.angle_2, 2)}\N{DEGREE SIGN})'	
		
class matrix():
	def __init__(self, rows, columns, name):
		self.rows = rows
		self.columns = columns
		self.mat_array = []
		self.name = name
		
		print(f"A matrix has been created! Rows: {self.rows}, Columns: {self.columns}")
		self.i = 0
		while self.i < self.rows * self.columns:
			self.mat_array.append(0)
			self.i = self.i + 1
	def printMat(self):
		

		print(f"Matrix-{self.name}:")
		
		self.a = 0
		while self.a < self.rows:

			self. b = 0
			self.line = ""
			while self.b < self.columns:
				
				try:

					self.line = self.line + f' {self.mat_array[(self.a*self.columns)+self.b]} '
					self.b = self.b + 1
				except IndexError:
					print("Dimension Error")
					self.b = self.b + 20
					self.a = self.a + 20


			print(f'|{self.line}|')
			self.a = self.a + 1

			

	def edit_mat(self, row, column, value):
		try:
			self.mat_array[(row*self.columns)+column] = value
		except IndexError:
			return False


		
		return True

def multiply_matrix(matA, matB):
	matrixA = matA.mat_array
	matrixB = matB.mat_array

	if matA.columns == matB.rows:
		new_mat_array = []
		number = 0

		a=0
		b=0
		c=0
		while b < matA.rows:
			#b is the current row of multiplication.
			while a < matA.columns:
				#a is current column of multiplication - decides column of matb
				while c < matA.columns:
					#c is number inside the operation. c0 makes number. C1 is number plus new number.
					
					number = number + matrixA[b*(matA.columns)+c]*matrixB[c*(matA.columns)+a]
					

					c=c+1

				
				new_mat_array.append(number)
				
				number = 0
				c = 0
				a=a+1

			a=0
			b = b+1


		b=0
		






		return new_mat_array

	else:
		return "Dimension Error"




		































