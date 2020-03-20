'''学生信息操作类

该类中包含了所有用于学生信息的操作方法
'''

def input_student(l):
    '''添加学生信息'''
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
    '''显示学生信息'''
    print('+------------+------+-------+')
    print('|   name     | age  | score |')
    print('+------------+------+-------+')
    for d in l:
        t = (d['name'].center(12), str(d['age']).center(6), str(d['score']).center(7))
        print('|%s|%s|%s|' % t)
    print('+------------+------+-------+')

def update_student(l):
    '''修改学生成绩'''
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
    '''删除学生信息'''
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
    '''按照学生年龄升序排序'''
    l[:] = sorted(l, key=lambda d: d['age'])

def sort_by_score(l):
    '''按照学生成绩倒序排序'''
    l[:] = sorted(l, key=lambda d: d['score'], reverse=True)

def save_info(l):
    '''将用户输入的学生信息保存到文本文件中'''
    if not l:
        print('要保存的信息为空，请添加信息后保存！')
    else:
        try:
            f = open('./stuManage/si.txt', 'w')
            for info in l:
                for key, value in info.items():
                    f.write(str(value))
                    f.write(' ')
                f.write('\n')
            f.close()
        except OSError as o:
            print('文件写入失败，原因：', o)
        finally:
            if f:
                f.close()

def read_info(l):
    '''从文件中读取学生信息，保存到内存中'''
    try:
        f = open('./stuManage/si.txt')
        l.clear()
        for line in f.readlines():
            name, age, score = line.rstrip().split(' ')
            d = {}
            d['name'] = name
            d['age'] = int(age)
            d['score'] = int(score)
            l.append(d)
    except OSError as o:
        print('文件读取失败，原因：', o)
    finally:
        if f:
            f.close()