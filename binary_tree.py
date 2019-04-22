# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class BiTree:
    """
    树类，一棵树的初始化以及所有关于树的方法
    """
    def __init__(self, x=None):
        self.root = TreeNode(x)  # 初始化为一棵只有根节点，且值为x的树

    def pre_order_traverse(self, root: TreeNode)-> list:
        """
        树的前序遍历，使用递归方法
        :param root: TreeNode
        :return: list
        """
        res = []
        if self.root is None:
            return res
        res.append(root.val)
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)

    def in_order_traverse(self, root: TreeNode)-> list:
        """
        树的中序遍历，使用递归方法
        :param root: TreeNode
        :return: list
        """
        res = []
        if self.root is None:
            return res
        self.pre_order_traverse(root.left)
        res.append(root.val)
        self.pre_order_traverse(root.right)

    def post_order_traverse(self, root: TreeNode)-> list:
        """
        树的后序遍历，使用递归方法
        :param root: TreeNode
        :return: list
        """
        res = []
        if self.root is None:
            return res
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)
        res.append(root.val)

    def level_order_traverse(self, root: TreeNode)-> list:
        """
        树的层次遍历，使用队列方法
        :param root: TreeNode
        :return: list
        """
        if not root:
            return []
        else:
            q, res = [root], []
            while q:
                cur = []  # cur每次循环开始都应该清空
                q_len = len(q)
                for _ in range(q_len):
                    node = q.pop(0)  # 相当于出队操作
                    cur.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(cur)
            return res

    def max_depth(self, root: TreeNode) -> int:
        """
        返回二叉树的最大深度
        :param root: TreeNode
        :return: int
        """
        # 递归 深度优先搜索
        if not root:  # 递归边界
            return 0
        else:
            left = 1 + self.maxDepth(root.left)
            right = 1 + self.maxDepth(root.right)
            return max(left, right)









