# Implementation of Growing Circles Algorithm 
# Based on Kubat's 'An Introduction to Machine Learning'

# Define an INITIAL STATE by selecting a random positive example for the center
# and set the radius so it does not contain any other examples

# SEARCH OPERATORS:
# One increases the radius, another shifts the center to another example

# FINAL STATE: A classifier that correctly classifies x% of training examples

# EVALUATION FUNCTION: We try to minimise the error rate

import random

class Example:
  def __init__(self, x, y, is_positive):
    self.x = x
    self.y = y
    self.is_positive = is_positive

class Classifier:
  def __init__(self, examples):
    self.center = random.choice(examples)
    self.radius = 0.1
    while(len(self.get_interior_examples(examples)) > 1):
      self.radius = self.radius / 2
  
  def get_interior_examples(self, examples):
    """Returns a list of examples within the radius of the classifier"""
    interior_examples = []
    for example in examples:
      r2 = self.radius ** 2
      d2 = ( example.x - self.center.x ) ** 2 + ( example.y - self.center.y ) ** 2
      if (d2 < r2):
        interior_examples.append(example)
    return interior_examples

def eval_func(classifier, examples):
  """Determines % of examples correctly classified"""
  total = len(examples)
  total_correct = 0

  interior_examples = classifier.get_interior_examples(examples) 
  for example in interior_examples:
    if (example.is_positive == True): 
      total_correct += 1

  exterior_examples = [x for x in examples if x not in interior_examples]
  for example in exterior_examples:
    if (example.is_positive == False):
      total_correct += 1
  
  return total_correct / total
  


examples = [Example(1, 1, True), Example(1.1, 1, False)]
initial_state = Classifier(examples)

print(eval_func(initial_state, examples))





print(initial_state.center, initial_state.radius)