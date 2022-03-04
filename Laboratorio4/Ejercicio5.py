class Arbol(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Matriz_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums)//2
    node = Arbol(array_nums[mid_num])
    node.left = Matriz_bst(array_nums[:mid_num])
    node.right = Matriz_bst(array_nums[mid_num+1:])
    return node

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   

array_nums = [1,2,3,4,5,6,7]

print("Matriz original:")
print(array_nums)
result = Matriz_bst(array_nums)
print("\nBusqueda binaria equilibrada en altura:")
print(preOrder(result))
