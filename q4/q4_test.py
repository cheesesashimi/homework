#!/usr/bin/python

import unittest
import q4


class Tests(unittest.TestCase):
  def test_rackspace_provided_string(self):
    """Tests that the function acts upon the Rackspace data and
    provides the appropriate output.
    """
    output = q4.reduce_string('abb cddpddef gh')
    self.assertEquals(output, 'abcdpdefgh')

  def test_no_spaces(self):
    """Tests that the function properly removes spaces even when no adjacent
    duplicates are found.
    """
    output = q4.reduce_string('za ch a r y')
    self.assertEquals(-1, output.find(' '))

  def test_no_duplicates(self):
    """Tests that the function removes adjacent duplicates even if no spaces
    are found.
    """
    output = q4.reduce_string('zzaacchhaarryy')
    self.assertEquals(output, 'zachary')

  def test_no_leading_spaces(self):
    """Tests that leading spaces are removed."""
    output = q4.reduce_string(' asdfqwer')
    # The -1 is the exit condition of the .find() method if that substring
    # is not found.
    self.assertEquals(-1, output.find(' '))

  def test_no_trailing_spaces(self):
    """Tests that trailing spaces are removed."""
    output = q4.reduce_string('asdfe ')
    self.assertEquals(-1, output.find(' '))

  def test_no_leading_nor_trailing_spaces(self):
    """Tests that both leading and trailing spaces are removed."""
    output = q4.reduce_string(' asdfe ')
    self.assertEquals(-1, output.find(' '))

  def test_no_beginning_duplicates(self):
    """Tests that duplicates at the beginning will be found and removed."""
    output = q4.reduce_string('zzachary')
    self.assertEquals(output, 'zachary')

  def test_no_ending_duplicates(self):
    """Tests that duplicates at the end will be found and removed."""
    output = q4.reduce_string('zacharyy')
    self.assertEquals(output, 'zachary')

if __name__ == '__main__':
  unittest.main()
