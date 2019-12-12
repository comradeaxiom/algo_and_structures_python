"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import collections

source = 'destroy all humans!'
print(source)
table = dict()

def haffman_tree(s):
    base = collections.Counter(s)
    order = collections.deque(sorted(base.items(), key=lambda item: item[1]))


    while len(order) > 1:
        node_index = order[0][1] + order[1][1]
        node = ({0: order.popleft()[0], 1: order.popleft()[0]}, node_index)

        for i, _count in enumerate(order):
            if node_index > _count[1]:
                continue
            else:
                order.insert(i, node)
                break
        else:
            order.append(node)

    return order[0][0]

def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')

haffman_code(haffman_tree(source))

for i in source:
    print(i, table[i], end=' ')
print()