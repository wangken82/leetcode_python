class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_step = 0
        self.helper(root)
        return self.max_step
    
    def helper(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val-1
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.max_step += abs(left)+abs(right)
        
        return left+right+root.val-1
