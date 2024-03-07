from typing import List

def sort_numbers_blocks(array : List[int]):
  """
    Sorts the numbers in blocks and returns the resulting string.

    Args:
        array (List[int]): The input list of integers.

    Returns:
        str: The resulting string after sorting the numbers in blocks.
    """
  if not array:
    return ""

  if array[0] == 0 or array[-1] == 0:
    return "X"

  blocks = find_blocks(array=array)

  blocks_ordered = sort_arrays(arrays=blocks)

  result = get_output(arrays=blocks_ordered)
  
  return result

def find_blocks(array : list) -> List[list]:
    """
    Finds the blocks of numbers in the input list.

    Args:
        array (List[int]): The input list of integers.

    Returns:
        List[List[int]]: A list of lists representing blocks of numbers.
    """
    start = 0 
    blocks = []
    for i, number in enumerate(array):
       if number == 0 and i > start:
          blocks.append(array[start:i])
          start = i + 1
       
       if number == 0 and i == start:
          blocks.append(array[start:i+1])
          start += 1
    
    if start < len(array):
       blocks.append(array[start:])
    return blocks
   
def sort_arrays(arrays : List[list]) -> List[list]:
   """
    Sorts the arrays of numbers in the input list.

    Args:
        arrays (List[List[int]]): The list of arrays to be sorted.

    Returns:
        List[List[int]]: A list of arrays with sorted numbers.
    """
   return [sorted(array) for array in arrays]

def get_output(arrays: List[list]) -> str:
    """
    Generates the output string based on the arrays of numbers.

    Args:
        arrays (List[List[int]]): The list of arrays of numbers.

    Returns:
        str: The resulting output string.
    """
    out = []
    for array in arrays:
        if len(array) == 1 and array[0] == 0:
            out.append("X")
        else:
            out.append("".join(map(str, array)))
    return " ".join(out)