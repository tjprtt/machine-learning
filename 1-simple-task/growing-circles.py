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
  def __init__(self, x, y):
    self.x = x
    self.y = y

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
      d2 = (example.x ** 2 - self.center.x ** 2) ** 2 + (example.y ** 2 - self.center.y)**2
      if (d2 < r2):
        interior_examples.append(example)
    return interior_examples