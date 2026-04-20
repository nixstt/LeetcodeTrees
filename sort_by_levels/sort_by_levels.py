'''sort_by_levels'''


def tree_by_levels(node):
    if not node:
        return []
    queue = [node]
    res = []
    while queue:
        cur = queue.pop(0)
        res.append(cur.value)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return res
