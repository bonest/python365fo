from typing import List, Set   #, Type
from collections import defaultdict

class ProductDAGTraverseController:
    def __init__(self) -> None:
        self.__todoNodesSet: Set[str] = None # str skal være nodeid aka varenr i 365
        self.__doneNodesSet: Set[str] = None # str skal være nodeid aka varenr i 365
        #self.__parrentNode : ProductDagNode = None

    def _getTodoNodesSet(self) -> Set[str]:
        if self.__todoNodesSet is None:
            self.__todoNodesSet = set()

        return self.__todoNodesSet
    
    def _getDoneNodesSet(self) -> Set[str]:
        if self.__doneNodesSet is None:
            self.__doneNodesSet = set()

        return self.__doneNodesSet
    
    # def setParrentNode(self, parrentNode : ProductDagNode):
    #     self.__parrentNode = parrentNode

    # def getParrentNode(self) -> ProductDagNode:
    #     return self.__parrentNode
    
    def shouldTraverseNode(self, node: ProductDagNode) -> bool:
        if node.getNodeId() in self._getTodoNodesSet():
            return True
        
        return False
    
    def addNodeIdToTodo(self, nodeId : str):
        self._getTodoNodesSet().add(nodeId)
    
    def markNodeAsTraversed(self, node: ProductDagNode):
        if node.getNodeId() in self._getTodoNodesSet():
            self._getTodoNodesSet().remove(node.getNodeId())
            self._getDoneNodesSet().add(node.getNodeId())
        else:
            self._getDoneNodesSet().add(node.getNodeId())
    


#TODO Skal laves om interface i x++
class ProductDAGTraverseNodeAble:
    def __init__(self) -> None:
        self.resultat = []
        self.mindste: int = None

    def handleTraversedNode(self, currentNode: ProductDagNode):
        if self.mindste:            
            self.mindste = min(self.mindste, currentNode.plc)
        else:
            self.mindste = currentNode.plc
        
        # prototyping resultat
        self.resultat.append(currentNode.getNodeId())

    #def 
    


class ProductDAG:

    def __init__(self) -> None:
        self.graph = None
        
    def __getGraph(self) -> defaultdict:
        if self.graph is None:
            
            # En lille python specialitet. List i stedet for set for set er kun til value typer og ikke objekter. 
            self.graph = defaultdict(list)

        return self.graph


    # Hvis der anvendes et set, vil man ikke kunne lægge objekter i, for de vil altid være forskellige.
    # Hvis noden skal indeholde andet data som skal bruges i traverseringen, så bør alle child objekter gemmes i et dictionary 
    def addEdge(self, edge : ProductDagNodesEdge):
        # Find id'en og smid edge objektet i listen. 
        self.__getGraph()[edge.getFromNode().getNodeId()].append(edge)

        """
        Tager en node og markerer den som behandlet, og kalder også resultable, handleNode metoden som kan gøre hvad som helst.
        """
    def __markNodeAsTraversed(self, node: ProductDagNode, controller: ProductDAGTraverseController, traversable : ProductDAGTraverseNodeAble):
        controller.markNodeAsTraversed(node)
        traversable.handleTraversedNode(node)


    # parm skiftes til _ i x++
    def __goDeepFrom(self, parmStartNode: ProductDagNode, traverseController: ProductDAGTraverseController, resultable : ProductDAGTraverseNodeAble):
        
        # Mark the node as handled.
        self.__markNodeAsTraversed(node = parmStartNode, controller = traverseController, traversable = resultable)
                
        # Sæt child liste til at være listen og angiv typen via type hint, så code completion virker. 
        childlist : List[ProductDagNodesEdge] = self.__getGraph()[parmStartNode.getNodeId()]

        # Gennemløb listen som findes i grafen for startnoden        
        for edge in childlist:
            # Lidt debug hvor jeg udskriver fra noden i parameter og fra noden i edge objektet som er i listen. 
            print(f"{parmStartNode.getNodeId()} == {edge.getFromNode().getNodeId()} : ToNodeId = {edge.getToNode().getNodeId()}")

            if traverseController.shouldTraverseNode(edge.getToNode()):
                # Handle new parrent node
                self.__goDeepFrom(edge.getToNode(), traverseController, resultable)
            else:
                #Handle end node
                self.__markNodeAsTraversed(node = edge.getToNode(), controller=traverseController, traversable = resultable)


            # if edge.getToNode().getNodeId() in parmParrentNodesTodoSet:
            #     self.__goDeepFrom(edge.getToNode(), parmParrentNodesTodoSet, parmResultat)


    def traverseDeep(self, startNode: ProductDagNode) -> ProductDAGTraverseNodeAble:
        # Byg et set af parrentNodes der skal løbes igennem
        # parrentNodesTodo = set()
        traversController = ProductDAGTraverseController()

        # Udfylder settet med forældre vare Id'er, når en sådan er løbet igennem så fjernes den fra liste. 
        for parrentId in self.__getGraph().keys():
            traversController.addNodeIdToTodo(parrentId)
            #parrentNodesTodo.add(parrentId)

        

        # Klargør resultat lige nu er det en liste vi sender videre  deepFirst. 
        resultat = ProductDAGTraverseNodeAble()

        self.__goDeepFrom(startNode, traversController, resultat)

        return resultat
        

graf = ProductDAG()

# opret forbindelser
#graf.addEdge(ProductDagNodesEdge(ProductDagNode()))

startNode = ProductDagNode.construct(vareNr="1", plc= 100)

graf.addEdge(ProductDagNodesEdge(startNode, ProductDagNode.construct(vareNr= "2", plc = 20)))
graf.addEdge(ProductDagNodesEdge(startNode, ProductDagNode.construct(vareNr= "3", plc = 30)))
graf.addEdge(ProductDagNodesEdge(ProductDagNode.construct(vareNr="2", plc= 20), ProductDagNode.construct(vareNr= "4", plc = 40)))
graf.addEdge(ProductDagNodesEdge(ProductDagNode.construct(vareNr="2", plc= 20), ProductDagNode.construct(vareNr= "5", plc = 2)))
graf.addEdge(ProductDagNodesEdge(ProductDagNode.construct(vareNr="3", plc= 30), ProductDagNode.construct(vareNr= "6", plc = 3)))

'''
dag.add_edge(1, 2)
dag.add_edge(1, 3)
dag.add_edge(2, 4)
dag.add_edge(2, 5)
dag.add_edge(3, 6)
'''
result = graf.traverseDeep(startNode)

print (f"Traversering liste= {result.resultat} laveste plc = {result.mindste}")
#print("DFS-traversering af DAG fra startnoden {}: {}".format(1, result))
