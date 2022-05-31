# O(N^2) 暴力

def truth():
    import pandas as pd

    data = pd.read_csv("data.csv")
    data = data.values
    from create_latitude import get_data, get_distance

    N = len(data)
    mini = 0
    minj = 0
    mindis = 0xfffffff
    for i in range(N-1):
        for j in range(i+1,N):
            d = get_distance(data[i][1],data[j][1],data[i][2],data[j][2])
            if d < mindis:
                mindis = d
                mini = i
                minj = j
    sod = 'safe'
    if mindis < 100:
        sod = 'danger'
    print("plane_ID: {} , {} , Distance: {} , {}".format(mini,minj,mindis,sod))



# data = get_data()

# data.sort(key=lambda x:x[1])

# data.sort(key=lambda x:x[1][1])

# print(data)