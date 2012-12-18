import ctypes

class Array:
	# Creates an array with size elements
	def __init__(self, size):
		assert size > 0, "Array size must be >0"
		self._size = size
		
		# Create the array structure using the ctypes module
		PyArrayType = ctypes.py_object * size
		self._elements = PyArrayType()
		
		# Initialize each element
		self.clear(None)
	
	def __len__(self):
		return self._size
	
	def __getitem__(self, index):
		#print "getitem is trying to get index: %i" % index
		#print chr(index)
		assert index >= 0 and index < len(self), "Array subscript out of range: "+ord(index)
		return self._elements[index]
	
	def __setitem__(self, index, value):
		assert index >= 0 and index < len(self), "Array subscript out of range: "+ chr(index)
		self._elements[index] = value
	
	def clear(self, value):
		for i in range(len(self)):
			self._elements[i] = value
	
	def __iter__(self):
		return _ArrayIterator(self._elements)

# An iterator for the Array ADT
class _ArrayIterator:
	def __init__(self, theArray):
		self.arrayRef = theArray
		self._curNdx = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.curNdx < len(self.arrayRef):
			entry = self.arrayRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration

# Implementation of the Array2D ADT using an array of arrays

class Array2D: 
	"""
	Creates a 2D array of size numRows x numCols
	@ Array theRows[Array numCols]
	"""
	def __init__(self, numRows, numCols):
		# Create a 1-D array to store an array reference for each row
		self._theRows = Array(numRows)
		
		# Create 2-D arrays for each row of the 2-D array
		for i in range(numRows):
			# print i
			self._theRows[i] = Array(numCols)
	
	# Returns the number of rows
	def numRows(self):
		return len(self._theRows)

	# Returns the number of columns
	def numCols(self):
		return len(self._theRows[0])

	# Clears the array by setting every element to the given value
	def clear(self, value):
		for row in range(self.numRows()):
			self._theRows[row].clear(value)

	# Gets the contents of the element at position [i,j]
	def __getitem__(self, ndxTuple):
		assert len(ndxTuple) == 2, "Invalid array subscript"
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert row >=0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
		the1dArray = self._theRows[row]
		return the1dArray[col]
		
	# Sets the contents of the element at position [i,j] to the value
	def __setitem__(self, ndxTuple, value):
		assert len(ndxTuple) == 2, "Invalid array subscript"
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert row >=0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
		the1dArray = self._theRows[row]
		the1dArray[col] = value 