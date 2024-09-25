def diff(points=[], radius=0):
    if points == [] or radius == 0:
        print('Missing Arguments Of points Or radius')
        return
    
    corner_pos = (points[0][0] - radius, points[0][1] - radius)

    if points[1][0] < corner_pos[0] or points[1][1] < corner_pos[1]:
        return False
    
    elif points[1][0] - corner_pos[0] < radius * 2 and points[1][1] - corner_pos[1] < radius * 2:
        return True
    
    else:
        return False