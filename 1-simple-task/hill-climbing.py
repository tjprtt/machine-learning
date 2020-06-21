# Implementation of Hill-Climbing Algorithm 
# Based on Kubat's 'An Introduction to Machine Learning'

from random import shuffle
from math import floor

class SlidingTileSet:
  """Represents one state of sliding tiles 0-9 and associated functions"""
  def __init__(self):
    # Generate random order of tiles
    self.tiles = list(range(0, 9))
    shuffle(self.tiles)
  
  def __str__(self):
    """String representation in 3x3 grid"""
    output_string = ""
    output_string += str(self.tiles[0])
    output_string += str(self.tiles[1])
    output_string += str(self.tiles[2])
    output_string += '\n'
    output_string += str(self.tiles[3])
    output_string += str(self.tiles[4])
    output_string += str(self.tiles[5])
    output_string += '\n'
    output_string += str(self.tiles[6])
    output_string += str(self.tiles[7])
    output_string += str(self.tiles[8])
    return output_string

  def moveable_tiles(self):
    """Returns tiles adjacent to 0 and therefore moveable"""
    moveable_tiles = []
    zero_index = self.tiles.index(0)
    zero_col = zero_index % 3
    zero_row = floor( zero_index / 3 )
    for index, tile in enumerate(self.tiles):
      tile_col = index % 3
      tile_row = floor( index / 3 )
      if ((tile_col == zero_col + 1 or tile_col == zero_col - 1) and tile_row == zero_row ) \
      or ((tile_row == zero_row + 1 or tile_row == zero_row - 1) and tile_col == zero_col):
        moveable_tiles.append(tile)
    return moveable_tiles

  def matching_tiles(self, other_tileset):
    """Returns number of matching tiles between two tilesets"""
    matches = 0
    for i in range(9):
      if self.tiles[i] == other_tileset.tiles[i]:
        matches += 1
    return matches
  
  def swap_tiles(self, tile1, tile2):
    """Exchanges two tiles in tileset by value"""
    tile1_index = self.tiles.index(tile1)
    tile2_index = self.tiles.index(tile2)
    self.tiles[tile1_index] = tile2
    self.tiles[tile2_index] = tile1

# HILL-CLIMBING ALGORITHM
initial = SlidingTileSet()
# initial.tiles = [0,1,2,3,4,5,6,7,8,9]
final = SlidingTileSet()
# final.tiles = [1,0,2,3,4,5,6,7,8,9]
print('Initial State:')
print(initial)
print('Final State:')
print(final)
print('#########')

def evaluation_func1(state):
  result = 9-final.matching_tiles(state)
  return result

# Create two lists, l and l_seen. l contains the initial state.
l = [initial]
l_seen = []

counter = 0
while True:
  #Check if l[0] matches final state
  if (final.matching_tiles(l[0]) == 9):
    print('SUCCESS!')
    break

  # Apply search operators to obtain new search states
  search_operators = l[0].moveable_tiles()
  search_states = []
  for i in search_operators:
    new_state = SlidingTileSet()
    new_state.tiles = l[0].tiles.copy()
    new_state.swap_tiles(0, i)

    # Only keep states not already visited
    is_seen = False
    for seen_state in l_seen:
      if (seen_state.matching_tiles(new_state) == 9):
        is_seen = True
    if is_seen == False:
      search_states.append(new_state)
  
  # Sort the new search states by the evaluation function
  search_states.sort(key=evaluation_func1)
  
  # Move l[0] from l to l_seen
  l_seen = [ l[0] ] + l_seen
  l.remove(l[0])

  # Place new search states at front of l
  l = search_states + l

  # If len(l) is 0, then stop and report failure
  if len(l) == 0:
    print('FAILURE')
    break
  
  # print(*search_states)
  print('#######STEP NO. ' + str(counter))
  print('#######STATES GENERATED: ' + str(len(l)))
  print('#######STATES SEEN: ' + str(len(l_seen)))
  print(l[0])
  print('\n')
  counter += 1