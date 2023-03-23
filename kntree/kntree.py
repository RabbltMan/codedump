from binarytree import *

samples = [(7, 2), (5, 4), (9, 6), (2, 3), (4, 7), (8, 1)]

tree = BuildTree(samples)

tree.show()
print(tree[1], type(tree), type(tree[0]))