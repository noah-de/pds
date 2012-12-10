# Implementation of the MatricADT using 2-D array
from array import Array2D

class Matrix:
	# Creates a matix of size numRows x numCols initialized to 0
	def __init__(self, numRows, numCols):
		self._theGrid = Array2D(numRows, numCols)
		self._theGrid.clear(0)

	# Return the number of rows in the matrix
	def numRows(self):
		return self._theGrid.numRows()

	# Returns the number of columns in the matrix
	def numCols(self):
		return self._theGrid.numCols()

	# Returns the value of element (i,j)
	def __getitem__(self, ndxTuple):
		return self._theGrid(ndxTuple[0], ndxTuple[1])

	# Sets the value of element (i,j) to the value s
	def __getitem__(self, ndxTuple, s):
		self._theGrid(ndxTuple[0], ndxTuple[1]) = s

	# Scales the matrix by the given scalar
	def scaleBy(self, scalar):
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				self[r,c] *= scalar

	# Creates and returns a new matrix that is the transpose of this matrix
	def transpose(self):
		pass
		
    # Creates and returns a new matrix that results from matrix addition
    def __add__(self, rhsMatrix):
		assert_matrix_compatability(self, rhsMatrix)
		# Create the new matrix
		newMatrix = Matrix(self.numRows(), self.numCols())
		# Add the corresponding elements in the two matrices
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				newMatrix[r,c] = self[r,c] + rhsMatrix[r,c]
		return newMatrix

	# Creates a new matrix that results from matrix subtraction
	def __sub__(self, rhsMatrix):
		assert_matrix_compatability(self, rhsMatrix)
		# Create the new matrix
		newMatrix = Matrix(self.numRows(), self.numCols())
		# Add the corresponding elements in the two matrices
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				newMatrix[r,c] = self[r,c] - rhsMatrix[r,c]
		return newMatrix

	# Creates and returns a new matrix resulting from matrix multiplication
	def __mul__(self, rhsMatrix):
		pass

	def assert_matrix_compatability(thisMatrix, thatMatrix):
		assert thatMatrix.numRows() == thisMatrix.numRows() and thatMatrix.numCols() == thisMatrix.numCols(), "Matrix sizes not compatible for add operation"
