# 任意输入 n 个学生的信息，形成字典后存于列表中。学生信息包括：姓名（字符串），年龄（整数），成绩（整数）
#        循环输入学生信息，知道输入学生姓名为空时结束输入
#       [{'name': 'xiaozhang', 'age': 20, 'score': 100}, {'name': 'xiaoli', 'age': 21, 'score': 98}, {'name': 'xiaowang', 'age': 19, 'score': 89}]
#       将以上列表使用漂亮的表格打印出来
# 第一版：

# l = []

# while True:
#     name = input('请输入学生姓名：')
#     if not name:
#         break
#     age = int(input('请输入学生年龄（整数）：'))
#     score = int(input('请输入学生成绩（整数）：'))
#     d = {}
#     d['name'] = name
#     d['age'] = age
#     d['score'] = score
#     l.append(d)

# print(l)

# len_name = max(len(l[0]['name']), len(l[1]['name']), len(l[2]['name']))
# print(len_name)

# 第二版：
# def input_student():
#     l = []
#     while True:
#         name = input('请输入学生姓名：')
#         if not name:
#             break
#         age = int(input('请输入学生年龄（整数）：'))
#         score = int(input('请输入学生成绩（整数）：'))
#         d = {}
#         d['name'] = name
#         d['age'] = age
#         d['score'] = score
#         l.append(d)
#     return l

# def output_student(L):
#     print('+------------+------+-------+')
#     print('|   name     | age  | score |')
#     print('+------------+------+-------+')
#     for d in L:
#         t = (d['name'].center(12), str(d['age']).center(6), str(d['score']).center(7))
#         print('|%s|%s|%s|' % t)
#     print('+------------+------+-------+')


# if __name__ == '__main__':
#     output_student(input_student())

# 第三版：实现添加菜单和选择菜单操作功能
# +------------------------------+
# | 1）添加学生信息                |
# | 2）查看所有学生信息             |
# | 3）修改学生的成绩              |
# | 4）删除学生信息                |
# | q）退出                       |
# +------------------------------+
# 例如：请选择：1         请输入姓名：          请选择：3      请输入修改学生的姓名：

def input_student(l):
    while True:
        name = input('请输入学生姓名（姓名输入为空直接退出添加）：')
        if not name:
            break
        age = int(input('请输入学生年龄（整数）：'))
        score = int(input('请输入学生成绩（整数）：'))
        d = {}
        d['name'] = name
        d['age'] = age
        d['score'] = score
        l.append(d)
    return l

def output_student(l):
    print('+------------+------+-------+')
    print('|   name     | age  | score |')
    print('+------------+------+-------+')
    for d in l:
        t = (d['name'].center(12), str(d['age']).center(6), str(d['score']).center(7))
        print('|%s|%s|%s|' % t)
    print('+------------+------+-------+')

def update_student(l):
    while True:
        s = input('请输入要修改成绩的学生姓名（直接回车退出修改）：')
        if not s:
            break
        for d in l:
            if d['name'] == s:
                score = int(input('请输入新的成绩（整数）：'))
                d['score'] = score
                break
        else:
            print('你输入的学生不存在，请重新输入！')
            continue

def del_student(l):
    while True:
        name = input('请输入要删除的学生姓名（直接回车退出删除）：')
        if not name:
            break
        for d in l:
            if d['name'] == name:
                l.remove(d)
                print('学生 %s 删除成功！' % name)
                break
        else:
            print('你输入的学生不存在，请重新输入！')
            continue

def sort_by_age(l):
    l[:] = sorted(l, key=lambda d: d['age'])

def sort_by_score(l):
    l[:] = sorted(l, key=lambda d: d['score'], reverse=True)

def print_info():
    print('+------------------------------+')
    print('| 1）添加学生信息              |')
    print('| 2）查看所有学生信息          |')
    print('| 3）修改学生的成绩            |')
    print('| 4）删除学生信息              |')
    print('| 5）按学生年龄大小排序        |')
    print('| 6）按学生成绩高低排序        |')
    print('| q）退出                      |')
    print('+------------------------------+')

if __name__ == '__main__':
    l = []
    while True:
        print_info()
        s = input('请选择要进行的操作序号：')
        if s == '1':
            input_student(l)
        elif s == '2':
            output_student(l)
        elif s == '3':
            update_student(l)
        elif s == '4':
            del_student(l)
        elif s == '5':
            sort_by_age(l)
        elif s == '6':
            sort_by_score(l)
        elif s == 'q':
            print('感谢使用本系统，再见！')
            break
        else:
            print('操作选择错误，请重新输入！')
            continue