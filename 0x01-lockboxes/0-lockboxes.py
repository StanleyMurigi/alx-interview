#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]
    
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)
    
    return all(opened)