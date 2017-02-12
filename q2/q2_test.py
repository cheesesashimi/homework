#!/usr/bin/python

import unittest
import q2

LOREM_IPSUM = ('Lorem ipsum dolor sit amet, dicit graeco electram in vis,' 
               ' minimum accusam omnesque has te. Purto equidem an pri, veniam' 
               ' nullam nostrum eos in. His nibh scripta an. Laudem reformidans'
               ' at nec, mundi facete nam at. Agam everti corrumpit qui ei. Mel'
               'ea labitur albucius, ei alii possit qui.')

RACKSPACE_STRING = 'The quick brown fox jumps over the lazy dog.'


class Tests(unittest.TestCase):
  def test_rackspace_provided_case(self):
    """Test for the Rackspace provided case.

    I know the spaces are in different places. I was trying to design it to
    place spaces evenly for padding.
    """
    input = RACKSPACE_STRING
    expected_output = ['The  quick brown fox',
                       'jumps  over the lazy',
                       'dog.']
    output = q2.justify_string(20, input)
    self.assertEquals(output, expected_output)

  def test_string_less_than_width(self):
    """Tests if the string length is less than the width.
    """
    input = RACKSPACE_STRING
    expected_output = RACKSPACE_STRING
    output = q2.justify_string(80, input)
    self.assertEquals(output, expected_output)

  def test_find_spaces(self):
    """Tests the find_spaces function.
    """
    input = RACKSPACE_STRING
    expected_output = [3, 9, 15, 19, 25, 30, 34, 39]
    output = q2.find_spaces(input)
    self.assertEquals(output, expected_output)

  def test_pad_line(self):
    """Tests the pad_line function.
    """
    input = 'The  quick brown fox'
    expected_output = 'The  quick brown fox'
    output = q2.pad_line(input, 20)
    self.assertEquals(output, expected_output)

  def test_longer_string(self):
    """Tests that the functions still work together if given a larger string.
    """
    input = LOREM_IPSUM
    expected_output = ['Lorem   ipsum  dolor',
                       'sit   a met,   dicit',
                       'graeco  electram  in',
                       'vis, minimum accusam',
                       'omnesque   has   te.',
                       'Purto   equidem   an',
                       'pri,  veniam  nullam',
                       'nostrum  eos in. His',
                       'nibh   scripta   an.',
                       'Laudem   reformidans',
                       'at nec, mundi facete',
                       'nam  at. Agam everti',
                       'corrumpit   qui  ei.',
                       'Melea        labitur',
                       'albucius,   ei  alii',
                       'possit qui.']
    output = q2.justify_string(20, input)
    self.assertEquals(output, expected_output)


if __name__ == '__main__':
  unittest.main()
