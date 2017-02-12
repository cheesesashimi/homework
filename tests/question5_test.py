#!/usr/bin/python

import unittest
from homework import question5


class Tests(unittest.TestCase):
  """Tests that the results are correct, given the 3x3 matrix from Rackspace."""
  def test_rackspace_3x3_matrix(self):
    input = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    output = '1 2 3 6 9 8 7 4 5'
    self.assertEquals(question5.spiral_matrix(input), output)

  def test_own_3x3_matrix(self):
    """Tests my own 3x3 matrix."""
    input = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    output = '1 2 3 4 5 6 7 8 9'
    self.assertEquals(question5.spiral_matrix(input), output)

  def test_4x4_matrix(self):
    """Tests with a matrix which has an even number of columns and rows."""
    input = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    output = '1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10'
    self.assertEquals(question5.spiral_matrix(input), output)

  def test_5x5_matrix(self):
    """Tests with a larger odd-rowed/columned matrix."""
    input = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]]
    output = '1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13'
    self.assertEquals(question5.spiral_matrix(input), output)

  def test_5x3_matrix(self):
    """Tests with an asymmetrical odd-columned/rowed matrix."""
    input = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15]]
    output = '1 2 3 4 5 10 15 14 13 12 11 6 7 8 9'
    self.assertEquals(question5.spiral_matrix(input), output)

  def test_3x5_matrix(self):
    """Tests with an asymmetrical odd-columned/rowed matrix in a different
    orientation.
    """
    input = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [10, 11, 12],
             [13, 14, 15]]
    output = '1 2 3 6 9 12 15 14 13 10 7 4 5 8 11'
    self.assertEquals(question5.spiral_matrix(input), output)

  def test_4x5_matrix(self):
    """Tests with an asymmetrical even-columned, odd-rowed matrix."""
    input = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16],
             [17, 18, 19, 20]]
    output = '1 2 3 4 8 12 16 20 19 18 17 13 9 5 6 7 11 15 14 10'
    self.assertEquals(question5.spiral_matrix(input), output)

  def test_5x4_matrix(self):
    """Tests with an asymmetrical odd-columned, even-rowed matrix."""
    input = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20]]
    output = '1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12'
    self.assertEquals(question5.spiral_matrix(input), output)

if __name__ == '__main__':
  unittest.main()
