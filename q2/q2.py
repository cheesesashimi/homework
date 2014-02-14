#!/usr/bin/python

import textwrap


def find_spaces(string_to_check):
  """Returns a list of string indexes for each string this finds.
  
  Args:
    string_to_check; string: The string to scan.

  Returns:
    A list of string indexes.
  """
  spaces = list()
  for index, character in enumerate(string_to_check):
    if character == ' ':
      spaces.append(index)
  return spaces


def pad_line(string_to_pad, width):
  """Pads a string to a specified width.

  Args:
    string_to_pad; string: The string to pad.
    width; integer: The length to pad the string to.

  Returns:
    A string padded to the appropriate length.
  """
  if len(string_to_pad) >= width:
    return string_to_pad

  string_to_pad = list(string_to_pad)
  spaces = find_spaces(string_to_pad)
  space_offset = 0
  while len(string_to_pad) < width:
    for space in spaces:
      if len(string_to_pad) < width:
        string_to_pad.insert(space + space_offset, ' ')
        space_offset += 1
  return ''.join(string_to_pad)


def justify_string(width, string_to_justify):
  """Takes a string and justifies it according to the width provided.

  I admit the use of textwrap might miss the spirit of this exercise, but
  I am prepared to discuss why I chose textwrap and some of the considerations
  I was making. 

  Args:
    width; integer: The column width to justify the string to.
    string_to_justify; string: The string to justify.

  Returns:
    A list of each justified line as a different element in the array.
  """
  if len(string_to_justify) < width:
    return string_to_justify

  output = list()
  lines_to_process = textwrap.wrap(string_to_justify, width)
  for i, line in enumerate(lines_to_process):
    if i < len(lines_to_process) - 1:
      output.append(pad_line(line, width))
    else:
      output.append(line)
  print output
  return output


