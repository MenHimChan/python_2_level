f = open("PY301-vacations.csv","r")
ls = []
for line in f:
    line = line.strip()             # 去掉行尾的换行符
    split_line = line.split(',')    # 按逗号分隔，返回一个列表
    ls.append(split_line)
# print(ls)
while True:
    data = input("请输入节假日序号：")
    input_idx = data.split(' ')
    # print(input_idx)

    for i in input_idx:
        if int(i) > 7 or int(i) < 1:
            print("输入节假日编号有误！")
            break
        for j in ls:
            if i == j[0]:
                print("{}({})假期是{}月{}日至{}月{}日之间".format(j[1], j[0], j[2][0:2], j[2][2:4], j[3][0:2], j[3][2:4]))
f.close()

