class Arbol(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def Eliminar_Nodo(root, key):
	if not root: 
		return root
	if root.val > key: 
		root.left = Eliminar_Nodo(root.left, key)
	elif root.val < key: 
		root.right= Eliminar_Nodo(root.right, key)
	else: 
		if not root.right:
			return root.left
		if not root.left:
			return root.right
		temp_val = root.right
		mini_val = temp_val.val
		while temp_val.left:
			temp_val = temp_val.left
			mini_val = temp_val.val
		root.right = Eliminar_Nodo(root.right,root.val)
	return root

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
    
root = Arbol(5)  
root.left = Arbol(3)  
root.right = Arbol(6) 
root.left.left = Arbol(2)  
root.left.right = Arbol(4) 
root.left.right.left = Arbol(7)  
print("Nodo original:")
print(preOrder(root))
result = Eliminar_Nodo(root, 4)
print("Despues de eliminar un nodo especifico:")
print(preOrder(result))
