import nodes

# klasse der indeholder link mellem parrent og child noder    
class ProductDagNodesEdge:    
    def __init__(self, fromNode : nodes.ProductDagNode, toNode: nodes.ProductDagNode):
        # Definerer fromNode og toNode som private
        self.__fromNode = fromNode
        self.__toNode = toNode

    def getFromNode(self) -> nodes.ProductDagNode:
        return self.__fromNode
    
    def getToNode(self) -> nodes.ProductDagNode:
        return self.__toNode