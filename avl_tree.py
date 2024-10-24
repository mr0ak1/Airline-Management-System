class Node:
    def __init__(self, key, flight_data=None):
        self.key = key
        self.flight_data = flight_data
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, flight):
        self.root = self._insert(self.root, flight)

    def _insert(self, root, flight):
        if not root:
            return Node(flight["flight_number"], flight)
        
        if flight["flight_number"] < root.key:
            root.left = self._insert(root.left, flight)
        else:
            root.right = self._insert(root.right, flight)
        
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        
        balance = self._get_balance(root)
        
        # Perform rotations if tree is unbalanced
        if balance > 1 and flight["flight_number"] < root.left.key:
            return self._right_rotate(root)
        
        if balance < -1 and flight["flight_number"] > root.right.key:
            return self._left_rotate(root)
        
        if balance > 1 and flight["flight_number"] > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        
        if balance < -1 and flight["flight_number"] < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def search_by_route(self, origin, destination):
        results = []
        self._search_by_route(self.root, origin, destination, results)
        return results

    def _search_by_route(self, node, origin, destination, results):
        if node:
            if node.flight_data["origin"] == origin and node.flight_data["destination"] == destination:
                results.append(node.flight_data)
            self._search_by_route(node.left, origin, destination, results)
            self._search_by_route(node.right, origin, destination, results)
