#!/usr/bin/python

def spiral_matrix(matrix):
  """Navigates a 2D array and traverses the edges in a spiral-pattern.

  Args:
    matrix; list: a 2D list to traverse.

  Returns:
    A string representation of all points traveled in the matrix in the order
    they were traveled to.
  """
  output = list()
  rows = len(matrix[0])
  columns = len(matrix)

  # Our iterators for columns and rows respectively.
  x = 0
  y = 0

  # Our edge coordinates.
  edge_x = 0
  edge_y = 0

  while x < rows and y < columns:
    # Traverses the top edge of the matrix.
    for x in range(0 + edge_x, rows):
      output.append(matrix[y][x])
    rows -= 1

    # Traverses down the right edge of the matrix.
    for y in range(1 + edge_y, columns):
      output.append(matrix[y][x])
    columns -= 1

    if edge_x < x and edge_y < y:
      # Traverses along the bottom edge of the matrix.
      for x in range(rows - 1, -1 + edge_x, -1):
        output.append(matrix[y][x])
      edge_x += 1
    
      # Traverses along the left edge of the matrix.
      for y in range(columns - 1, 0 + edge_y, -1):
        output.append(matrix[y][x])
      edge_y += 1
    else:
      break

  """
  The instructions seemed to indicate that I should return a string, so
  I chose to use the generator notation here to perform that function. I
  chose this vs. a list comprehension since it is a bit more space-efficient.
  """
  output_strings = ' '.join((str(number) for number in output))
  return output_strings
