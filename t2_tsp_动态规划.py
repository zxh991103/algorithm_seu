
class TSP:
    def __init__(self,X,start_node):
        
        self.X = X #距离矩阵
        self.start_node = start_node #开始的节点
        self.N = int(len(X)/2)
        self.array = [[0]*(2**len(self.X)) for i in range(len(self.X))] #记录处于x节点，未经历M个节点时，矩阵储存x的下一步是M中哪一个节点
    def transfer(self,sets):
        su = 0
        for s in sets:
            su = su + 2**s # 二进制转换
        return su
    # tsp总接口

    def show(self):
        M = self.array
        lists = list(range(len(self.X)))
        start = self.start_node
        rel = 0.0
        print('-------------------')
        while len(lists) > 0:
            lists.pop(lists.index(start))
            m = self.transfer(lists)
            next_node = self.array[start][m]
        
            if start <  self.N :
                print("{} 号集装箱送往 {} 号阵地".format(start,next_node-self.N))
                rel += self.X[start][next_node]
            start = next_node
        print('-------------------')
        print("最大匹配程度: {} %".format((self.N-rel)/self.N*100))



    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = list(range(num)) #造成节点的集合
        past_sets = [s] #已遍历节点集合
        cities.pop(cities.index(s)) #构建未经历节点的集合
        node = s #初始节点
        return self.solve(node,cities) #求解函数
    def solve(self,node,future_sets):
        # 迭代终止条件，表示没有了未遍历节点，直接链接当前节点和起点便可
        if len(future_sets) == 0:
            return self.X[node][self.start_node]
        d = 99999
        # node若是通过future_sets中节点，最后回到原点的距离
        distance = []
        # 遍历未经历的节点
        for i in range(len(future_sets)):
            s_i = future_sets[i]
            copy = future_sets[:]
            copy.pop(i) # 删除第i个节点，认为已经完成对其的访问
            distance.append(self.X[node][s_i] + self.solve(s_i,copy))
        # 动态规划递推方程，利用递归
        d = min(distance)
        # node须要链接的下一个节点
        next_one = future_sets[distance.index(d)]
        # 未遍历节点集合
        c = self.transfer(future_sets)
        # 回溯矩阵，（当前节点，未遍历节点集合）——>下一个节点
        self.array[node][c] = next_one
        return d



def score(x,y):
    res = 0
    for i,j in zip(x,y):
        res += 1-abs((i-j)/i)  
    res = res/len(x)
    return res

class dispatch:
    def __init__(self,A,B,N):
        D = []
        MAX_I =9999999
        for i in range(N):
            t = []
            for k in range(N):
                t.append(MAX_I)
            for j in range(N):
                t.append(1-score(A[i],B[j]))
            D.append(t)

        for i in range(N):
            t = []
            for j in range(N):
                t.append(MAX_I)
            for k in range(N):
                t.append(MAX_I)
            D.append(t)
        self.D = D
    def run(self):
        S = TSP(self.D,0)
        S.tsp()
        S.show()





if __name__ == "__main__":
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
    N = 4
    print('-------------------')
    for i in range(N):
        print("{} 号集装箱装有:弹药 {}, 谷物 {}, 肉罐头 {}, 饮用水 {}".format(i,A[i][0],A[i][1],A[i][2],A[i][3]))
    print('-------------------')
    for i in range(N):
        print("{} 号阵地需要:弹药 {}, 谷物 {}, 肉罐头 {}, 饮用水 {}".format(i,B[i][0],B[i][1],B[i][2],B[i][3]))
    print('-------------------')


    Dis = dispatch(A,B,N)
    Dis.run()
