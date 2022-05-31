words = ['0','6','8','9']

M = 5 # 生成 4-M 位的所有可能密码
res = []


def find_password(pwd,i):
    pwd = pwd + i
    use_num = len(set(pwd))
    if len(pwd) >= len(words) and use_num == len(words):
        res.append(pwd)
    if M - len(pwd) + use_num < len(words) or len(pwd) == M:
        return
    for j in words:
        find_password(pwd,j)




if __name__ == "__main__":
    find_password('','')
    print("可能的密码个数：",len(res))
    print("可能的密码为：",res)

