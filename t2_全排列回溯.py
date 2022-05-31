from copy import deepcopy

N = 4

A = [
    [1,2,3,10],
    [2,1,3,4],
    [3,1,4,2],
    [10,2,1,3]
]
B = [
    [3,1,4,2],
    [4,2,1,3],
    [2,1,3,4],
    [15,2,3,4]
]
MAXN = -9999
RES = []


order = list(range(0,N))

def score(x,y):
    res = 0
    for i,j in zip(x,y):
        res += 1 -abs((i-j)/i)  
    res = res/len(x)
    return res


def cal_score(arr):
    
    sc = 0
    for i in range(N):
        sc += score(A[arr[i]],B[i])
    global MAXN
    global RES
    
    if sc > MAXN:
        MAXN = sc 
        RES = deepcopy(arr)
        
    

def permutations(arr, position, end):
    global MAXN
    global res
    if position == end:  
        cal_score(arr)
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]
    

def best(order):
    permutations(order, 0, N)
    print('-------------------')
    for i in range(N):
        print("{} 号集装箱装有:弹药 {}, 谷物 {}, 肉罐头 {}, 饮用水 {}".format(i,A[i][0],A[i][1],A[i][2],A[i][3]))
    print('-------------------')
    for i in range(N):
        print("{} 号阵地需要:弹药 {}, 谷物 {}, 肉罐头 {}, 饮用水 {}".format(i,B[i][0],B[i][1],B[i][2],B[i][3]))
    print('-------------------')
    print("最大匹配程度: {} %".format(MAXN/N*100))
    print('-------------------')
    for i in range(N):
        print("{} 号集装箱送往 {} 号阵地".format(RES[i],i))

    






if __name__ == "__main__":
    
    best(order)



    

