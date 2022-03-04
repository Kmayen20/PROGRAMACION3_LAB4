class Arbol(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def ValorMasCercano(root, target):
    a = root.val
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = ValorMasCercano(kid, target)
    return min((a,b), key=lambda x: abs(target-x))

root = Arbol(4)  
root.left = Arbol(2)  
root.right = Arbol(6) 
root.left.left = Arbol(1)  
root.left.right = Arbol(3) 
root.right.left = Arbol(5)
root.right.right = Arbol(7)  
    
result = ValorMasCercano(root,9)
print(result)
