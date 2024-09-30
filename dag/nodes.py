'''
DAG models
'''

# Basisklasse der indeholder varenummer. 
class ProductDagNode:
    def __init__(self):
        self.__nodeId = ''
        self.plc: int = None

    def getNodeId(self) -> str:
        return self.__nodeId
    
    def setNodeId(self, nodeId : str):
        self.__nodeId = nodeId

    @classmethod
    def construct(cls, vareNr : str, plc : int):
        newNode = cls()
        newNode.setNodeId(vareNr)
        newNode.plc = plc
        return newNode

#TODO: lav en subclass af ProductDagNode hvor du har PLC properties på og lav så en måde at få sammenlignet værdierne i traverseringen

class ProductDagNodeMeta:
    
    # Declaring the properties of the ProductDagNodeMeta object
    def __init__(self):
        self.__mainNodeId = '' # private.
        self.parrentNodeId = ''
        self.nodeLevel: int = 1


