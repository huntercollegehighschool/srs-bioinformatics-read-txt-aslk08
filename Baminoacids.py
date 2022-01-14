"""
Define a function weightedstring that takes a string input protein. The function returns the weighted string of that protein based on masstable.txt.

weightedstring should read from masstable.txt. It's helpful to have those masses in a dictionary.
"""

def weightedstring(protein):
  weights = {}
  total = 0
  file = open("masstable.txt", "r")
  for weight in file.readlines():
    weights[weight[0]] = float(weight[2:])
  for p in protein:
    total += weights[p]
  return total
