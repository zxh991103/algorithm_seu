# O(N) 随机算法

from create_latitude import get_data, get_lat_distance,get_tuple_distance,get_log_distance

data = get_data()
N = len(data)

MAX = 0x3fffffff
ans = MAX

planei = 0
planej = 0
count = 0

def randomize(data):
    import random
    for i in range(N-1,0,-1):
        j = random.randint(0,i)
        data[i],data[j] = data[j],data[i]
    return data



def find_grid_box(p,d):
    x = int(p[1]/d)
    y = int(p[2]/d)
    return (x,y)



def build_grid(pl,d):
    grid = {}
    for i in pl:
        box = find_grid_box(i,d)
        if box not in grid:
            grid[box] = []

        grid[box].append(i)

    return grid


def neibors(box):
    x = box[0]
    y = box[1]
    return [(x+1,y),
            (x+1,y-1),
            (x,y-1),
            (x-1,y-1),
            (x-1,y),
            (x-1,y+1),
            (x,y+1),
            (x+1,y+1)
    ]


def find_cp(data=data):
    global ans
    global planei
    global planej
    global count

    data = randomize(data)

    d = get_tuple_distance(data[0],data[1])
    planei = data[0][0]
    planej = data[1][0]

    currentPoints = [data[0],data[1]]

    grid = build_grid(currentPoints,d)

    for i in range(2,N):
        currentPoint = data[i]
        box = find_grid_box(currentPoint,d)
        Report = neibors(box)
        Report.append(box)

        adjacentPoints = []
        for k in Report:
            if k in grid:
                count += 1
                for j in grid[k]:
                    adjacentPoints.append(j)

        distChanged = False

        for k in adjacentPoints:
            currentDist = get_tuple_distance(currentPoint,k)

            if currentDist < d:
                distChanged = True
                d = currentDist
                planei = currentPoint[0]
                planej = k[0]
                ans = d
        
        currentPoints.append(currentPoint)

        if distChanged:
            grid = build_grid(currentPoints,d)
        else:
            if box not in grid:
                grid[box] = [currentPoint]
            else:
                grid[box].append(currentPoint)
    
    print("Iteration counter in Hashing is : ", count )








if __name__ == "__main__":
    from t3_0 import truth
    print("Brute force solution:")
    truth()
    print("O(N) solution:")
    find_cp()
    sod = 'safe'
    if ans < 100:
        sod = 'danger'
    print("plane_ID: {} , {} , Distance: {} , {}".format(planei,planej,ans,sod))