def move_tower(height, fromPole, withPole, toPole):
    if height >= 1:
        move_tower(height - 1, fromPole, toPole, withPole)
        move_disk(fromPole, toPole)
        move_tower(height - 1, withPole, fromPole, toPole)
        
def move_disk(fp, tp):
    print('Move disk from', fp, 'to', tp, sep = ' ')

move_tower(4, 'A', 'B', 'C')