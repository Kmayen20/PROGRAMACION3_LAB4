class Arbol(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BST(root):
    stack = []
    prev = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.val <= prev.val:
            return False
        prev = root
        root = root.right
    return True

root = Arbol(2)  
root.left = Arbol(1)  
root.right = Arbol(3) 
 
result = BST(root)
print(result)

root = Arbol(1)  
root.left = Arbol(2)  
root.right = Arbol(3) 
 
result = BST(root)
print(result)
