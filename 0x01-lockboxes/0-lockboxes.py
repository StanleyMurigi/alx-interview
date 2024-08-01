#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    opened = set()
    queue = [0]
    
    while queue:
        current_box = queue.pop(0)
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < n and key not in opened:
                    queue.append(key)
    
    return len(opened) == n