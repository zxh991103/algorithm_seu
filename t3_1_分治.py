# O(n log n) 分治法



from create_latitude import get_data, get_lat_distance,get_tuple_distance,get_log_distance


data = get_data()
data = sorted(data,key= lambda x:(x[1],x[2]))
N = len(data)


MAX = 0x3fffffff
ans = MAX

planei = 0
planej = 0

def divide(left,right):

    global ans
    global planei
    global planej

    dist = MAX
    if left == right:
        return MAX

    if left + 1 == right :
        t_dis = get_tuple_distance(data[left],data[right])
        if t_dis < dist:
            dist = t_dis
            if dist < ans:
                ans = dist
                planei = left
                planej = right
        return t_dis
    
    mid = int((left+right)/2)

    dist1 = divide(left,mid)
    dist2 = divide(mid+1,right)

    if dist1 < dist2:
        dist = dist1
        if dist1 < ans:
            ans = dist1
            planei = data[left][0]
            planej = data[mid][0]
    else:
        dist = dist2
        if dist2 < ans:
            ans = dist2
            planei = data[mid+1][0]
            planej = data[right][0]

    
    mid_tmp = []

    for i in range(left,right+1):
        if get_log_distance(data[mid],data[i]) <= dist:
            mid_tmp.append(data[i])


    mid_tmp.sort(key = lambda x:x[2])
                
    mid_n = len(mid_tmp)

    for i in range(mid_n-1):
        for j in range(i+1,mid_n):
            if get_lat_distance(mid_tmp[i],mid_tmp[j]) < dist:
                dist3 = get_tuple_distance(mid_tmp[i],mid_tmp[j])
                if dist3 < dist:
                    dist = dist3
                    if dist < ans:
                        ans = dist
                        planei = mid_tmp[i][0]
                        planej = mid_tmp[j][0]
    
    return dist



if __name__ == '__main__':

    from t3_0 import truth

    print("Brute force solution:")

    truth()

    divide(0,N-1)

    print("Divide and conquer algorithm:")

    sod = 'safe'
    if ans < 100:
        sod = 'danger'
    print("plane_ID: {} , {} , Distance: {} , {}".format(planei,planej,ans,sod))

    