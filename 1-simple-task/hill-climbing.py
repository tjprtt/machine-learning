# Implementation of Hill-Climbing Algorithm 
# Based on Kubat's 'An Introduction to Machine Learning'

from random import shuffle

def compare_states(state_1, state_2):
  if state_1 is None and state_2 is None:
    return True
  if state_1 is None or state_2 is None:
    return False
  

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
    zero_remainder = zero_index % 3
    for index, tile in enumerate(self.tiles):
      if index % 3 == zero_remainder and tile != 0:
        moveable_tiles.append(tile)
    return moveable_tiles
  
  def matching_tiles(self, other_tileset):
    """Returns number of matching tiles between two tilesets"""
    matches = 0
    for i in range(9):
      if self.tiles[i] == other_tileset.tiles[i]:
        matches += 1
    return matches

# HILL-CLIMBING ALGORITHM
# 1. Create two lists, l and l_seen. l contains the initial state.
initial = SlidingTileSet()
final = SlidingTileSet()

print(initial,'\n',final)
print(initial.matching_tiles(final))