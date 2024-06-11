class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def organize(prevNode, currentNode):
            if currentNode == None:
                return prevNode
            currentNode.prev = prevNode
            prevNode.next = currentNode

            t = currentNode.next
            tail = organize(currentNode, currentNode.child)
            currentNode.child = None
            return organize(tail, t)

        if head == None:
            return None
        temp = Node(0, None, head, None)
        organize(temp, head)
        temp.next.prev = None
        return temp.next