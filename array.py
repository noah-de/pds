#!/usr/bin/env python
# encoding: utf-8
"""
array.py

Created by elihu on 2012-11-22.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

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
		
	def __getItem__(self, index):
		assert index >= 0 and index < len(self), "Array subscript out of range"
		return self._elements[index]

	def __setItem__(self, index):
		assert index >= 0 and index < len(self), "Array subscript out of range"
		self._elements[index] = value
		
	def __iter__(self):
		return _ArrayIterator(self._elements)

# An iterator for the Array ADT
class _ArrayIterator:
	def __init__(self, the Array):
		self.arrayRef = theArray
		self._curNdx = 0
		
	def __iter__(self)::
		return self
		
	def __next__(self)::
		if self.curNdx < len( self.arrayRef):
			entry = self.arrayRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration

