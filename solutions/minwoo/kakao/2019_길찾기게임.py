import sys 
sys.setrecursionlimit(10**8)

def solution(nodeinfo):
    class TreeNode:
        def __init__(self, y, x,val):
            self.val = val
            self.x = x
            self.y = y
            self.left = None
            self.right = None

    def insert(root,cur_node): 
        y,x,val = cur_node
        if root.x > x : # 왼쪽에 삽입
            if root.left == None :
                root.left = TreeNode(y,x,val)
            else:
                insert(root.left,cur_node)
        else : # 오른쪽에 삽입
            if root.right == None:
                root.right = TreeNode(y,x,val)
            else:
                insert(root.right,cur_node)

    def preorder(node,path):
        path.append(node.val)
        if node.left :
            preorder(node.left,path)
        if node.right:
            preorder(node.right,path)
        return path

    def postorder(node,path):
        if node.left :
            postorder(node.left,path)
        if node.right :
            postorder(node.right,path)
        path.append(node.val)
        return path
 
    nodeinfo_t = []
    for i in range(len(nodeinfo)):
        nodeinfo_t.append([nodeinfo[i][1],nodeinfo[i][0],i+1]) # y,x,val 순으로 저장
    nodeinfo_t.sort(key = lambda x : (-x[0],x[1])) # y좌표 내림차순 x좌표 오름차순
    
    root = TreeNode(nodeinfo_t[0][0],nodeinfo_t[0][1],nodeinfo_t[0][2]) 

    for i in range(1,len(nodeinfo_t)):
        insert(root,nodeinfo_t[i])

    return([preorder(root,[]),postorder(root,[])])
