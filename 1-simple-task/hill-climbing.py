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


# HILL-CLIMBING ALGORITHM
# 1. Create two lists, l and l_seen. l contains the initial state.
initial = SlidingTileSet()
final = SlidingTileSet()
print('Initial State:')
print(initial)
print('Final State:')
print(final)
print('#########')

l = [initial]
l_seen = []

print(initial.moveable_tiles())

# 2. Check if l[0] matches final state
while True:
  if (final.matching_tiles(l[0]) == 9):
    print('SUCCESS!')
    break
  # Apply all available search operators to current state
  # to obtain a set of new states
