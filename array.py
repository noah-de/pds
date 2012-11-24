#!/usr/bin/env python
# encoding: utf-8
"""
array.py

Created by versorge on 2012-11-22.
"""

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
		if self.curNdx < len( self.arrayRef):
			entry = self.arrayRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration

