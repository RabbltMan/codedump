from point import *
import typing
import numpy as np


class TreeNode(Point):
    def __init__(self, treeNode: Point) -> None:
        super().__init__(*treeNode)
        self.father = None
        self.childLeft = None
        self.childRight = None


class TreeNodes:
    def __init__(self, treeNodes: typing.List[Point]) -> None:
        self.treeNodes = [TreeNode(node) for node in treeNodes]

    def __len__(self):
        return len(self.treeNodes)

    def __getitem__(self, key):
        return self.treeNodes[key]

    def __repr__(self):
        return str(self.treeNodes)

    def getSplitDimension(self, treeNodeDepth=1) -> int:
        return treeNodeDepth % min(list(x.dimension for x in self.treeNodes))

    def getMidpoint(self, dimension: int) -> TreeNode:
        dim = list(x[dimension] for x in self.treeNodes)
        rank = list(np.argsort(dim))
        if (len(self.treeNodes) % 2 == 0):
            return self.treeNodes[rank[int(len(rank)/2)]]
        else:
            return self.treeNodes[rank[int((len(rank)-1)/2)]]


class BuildTree:
    tree = list()
    LayerNodes = list()

    def __init__(self, Nodes) -> None:
        if isinstance(Nodes, list):
            self.nodes = TreeNodes(Nodes)
        elif isinstance(Nodes, TreeNodes):
            self.nodes = Nodes
        self.buildTree(self.nodes)

    def __call__(self):
        return self.tree
    
    def __getitem__(self, key):
        self.show(0)
        return self.LayerNodes[key]
    
    def show(self, show=1):
        maxdepth = int(np.log2(len(self.tree) + 1))
        self.LayerNodes = list()
        root = []
        for node in self.tree:
            if (node.father == None):
                root.append(node)
                self.LayerNodes.append(root)
                if show == 1:
                    print(root)
        for depth in range(1, maxdepth + 1):
            curDepth = []
            for node in root:
                curDepth.append(node.childLeft)
                curDepth.append(node.childRight)
            root = curDepth
            self.LayerNodes.append(root)
            if show == 1:
                print(root)

    def buildTree(self, treeNodes: TreeNodes, fatherNode=None, childTreeDirection=None, Depth=0):
        if len(treeNodes) == 0:
            return None

        splitDimension = treeNodes.getSplitDimension(Depth)
        rootNode = treeNodes.getMidpoint(splitDimension)
        rootNode.father = fatherNode
        if childTreeDirection == 'left':
            fatherNode.childLeft = rootNode
        if childTreeDirection == "right":
            fatherNode.childRight = rootNode

        LeftChildren, RightChildren = [], []
        Queue = []
        for node in treeNodes:
            if node[splitDimension] < rootNode[splitDimension]:
                LeftChildren.append(node)
            elif node[splitDimension] > rootNode[splitDimension]:
                RightChildren.append(node)
            elif node is rootNode:
                continue
            else:
                Queue.append(node)
        for node in Queue:
            if len(RightChildren) >= len(LeftChildren):
                LeftChildren.append(node)
            else:
                RightChildren.append(node)
        depth = Depth + 1
        leftChildBinaryTreeNodes = TreeNodes(LeftChildren)
        self.buildTree(leftChildBinaryTreeNodes, rootNode, 'left', depth)
        rightChildBinaryTreeNodes = TreeNodes(RightChildren)
        self.buildTree(rightChildBinaryTreeNodes, rootNode, 'right', depth)
        # print(f"第{Depth}层, {rootNode}")
        self.tree.append(rootNode)
        return rootNode
