class Arbol(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def k_pequeño(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.right
    return root.val

root = Arbol(8)  
root.left = Arbol(5)  
root.right = Arbol(14) 
root.left.left = Arbol(4)  
root.left.right = Arbol(6) 
root.left.right.left = Arbol(8)  
root.left.right.right = Arbol(7)  
root.right.right = Arbol(24) 
root.right.right.left = Arbol(22)  

print(k_pequeño(root, 1))
print(k_pequeño(root, 3))
