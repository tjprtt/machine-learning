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
  
  def get_moveable_tiles(self):
    """Returns tiles adjacent to 0 and therefore moveable"""
    moveable_tiles = []
    zero_index = self.tiles.index(0)
    zero_remainder = zero_index % 3
    for index, tile in enumerate(self.tiles):
      if index % 3 == zero_remainder and tile != 0:
        moveable_tiles.append(tile)
    return moveable_tiles


l = []
l_seen = []

start = SlidingTileSet()
print(start.tiles)
print(start.get_moveable_tiles())