from binarytree import *

samples = [(3, 4), (4, 2), (1, 7), (2, 5), (3, 10), (5, 1), (1, 5)]

tree = BuildTree(samples)

print(tree, type(tree), type(tree[0]))

