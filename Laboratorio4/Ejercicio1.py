class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Matriz_Ordenada(nums):
    
    if not nums:
        return None
    mid_val = len(nums)//2
    node = TreeNode(nums[mid_val])
    node.left = Matriz_Ordenada(nums[:mid_val])
    node.right = Matriz_Ordenada(nums[mid_val+1:])
    return node

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
    
result = Matriz_Ordenada([1, 2, 3, 4, 5, 6, 7])
preOrder(result)
