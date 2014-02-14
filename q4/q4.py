#!/usr/bin/python

def reduce_string(string_to_reduce):
  """Reduces a string by removing spaces and adjacent duplicate characters.

  Note that although I transform the string into a list and transform it back
  into a string before returning it, that the operations are done in-place.

  Args:
    string_to_reduce; string: The string to reduce.

  Returns:
    A reduced string.
  """
  string_to_reduce = list(string_to_reduce.strip(' '))

  for index, character in enumerate(string_to_reduce):
    if index > 0 and index < len(string_to_reduce) - 1:
      if character == string_to_reduce[index - 1]:
        string_to_reduce.pop(index - 1)

      if character == string_to_reduce[index + 1]:
        string_to_reduce.pop(index + 1)

      if string_to_reduce[index] == ' ':
        string_to_reduce.pop(index)
    else:
      if index < len(string_to_reduce) - 1:
        if character == string_to_reduce[index + 1]:
          string_to_reduce.pop(index + 1)

  return ''.join(string_to_reduce)
