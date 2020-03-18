

# 条件表达式练习 1
# 输入一个数：1）用 if 语句计算出这个数的绝对值并打印出来；2）用条件表达式计算出这个数的绝对值并打印出来
def ex1():
    n = int(input('请输入一个数字：'))
    if n < 0:
        n = -n
    print(n)

    m = int(input('请输入一个数字：'))
    m = -m if m < 0 else (m ** 2 if m < 100 else m)
    print(m)

# 练习 2
# 北京出租车收费标准：3 公里以内收 13 元，超过 3 公里后基本单价为 2.3 元/公里，超过 15 公里后，每公里加收基本单价的 50% 作为返程的空驶费
# 要求：输入公里数，打印出费用的金额（以元为单位进行四舍五入）
def ex2():
    kir = int(input('请输入出租车行驶的公里数：'))

    fee = 13 + (kir - 3) * 2.3 if kir > 3 else 0 + (kir - 15 ) * (2.3 * 1.5) if kir > 15 else 0

    print('您本次乘车共行驶：%d，费用为；%d' % (kir, int(round(fee))))

# 格式化字符串打印练习 3
# 写一个程序，打印一个高度为 4 的矩形方框
# 要求输入一个整数，此整数代表矩形的宽度，输出次矩形
def ex3():
    '''写一个程序，打印一个高度为 4 的矩形方框'''
    width = int(input('请输入矩形的宽度（正整数）：'))
    for i in range(1, 5):
        if i == 1 or i == 4:
            print('#' * width)
        else:
            print('#' + ' ' * (width-2) + '#')

# 字符串练习 4
# 输入一个字符串，把字符串的第一个字符和最后一个字符去掉，打印出处理后的字符串
def ex4():
    '''输入一个字符串，把字符串的第一个字符和最后一个字符去掉，打印出处理后的字符串'''
    s = input('请输入一个字符串：')
    print('原字符串是：%s\n去掉头尾的字符串是：%s' % (s, s[1:-1]))

# 字符串练习 5
# 输入任意一个字符串，判断这个字符串是否是回文，回文指中心对称的文字，即把字符正序显示和倒序显示是一样的
def ex5():
    '''输入任意一个字符串，判断这个字符串是否是回文，回文指中心对称的文字，即把字符正序显示和倒序显示是一样的'''
    s = input('请输入一个字符串：')
    print('你输入的字符串 %s 回文' % ('是' if s == s[::-1] else '不是'))

# 字符串方法练习 6
# 输入一个字符串：1. 判断输入的字符串有几个空格；2. 将原字符串的左右空格去掉，打印出有效字符的长度；3. 判断输入是否数字
def ex6():
    '''输入一个字符串：1. 判断输入的字符串有几个空格；2. 将原字符串的左右空格去掉，打印出有效字符的长度；3. 判断输入是否数字'''
    s = input('请输入一个字符串：')
    nums = s.count(' ')
    print('你一共输入了 %d 个空格' % nums)
    ss = s.strip()
    print('去掉字符串前后的空格的字符串长度是：%s' % len(ss))
    print('你输入的 %s 数字' % ('是' if ss.isdigit() else '不是'))

# 格式化字符串练习 7
# 输入 3 行文字，1. 让这些文字依次以 20 字符的宽度右对齐输出；2. 以最长字符串的长度进行右对齐显示；
def ex7():
    '''输入 3 行文字，1. 让这些文字依次以 20 字符的宽度右对齐输出；2. 以最长字符串的长度进行右对齐显示；'''
    print('请输入 3 行文字：')
    s1 = input('请输入第 1 行文字：')
    s2 = input('请输入第 2 行文字：')
    s3 = input('请输入第 3 行文字：')
    print('%20s' % s1)
    print('%20s' % s2)
    print('%20s' % s3)
    max_len = max(len(s1), len(s2), len(s3))
    fm = '%%%ds' % max_len
    print(fm % s1)
    print(fm % s2)
    print(fm % s3)

# while 和 print 练习 8
# 打印 1~20 的整数，每行 5 个 打印 4 行，数字之间用空格分隔
def ex8():
    '''打印 1~20 的整数，每行 5 个 打印 4 行，数字之间用空格分隔'''
    i = 1
    while i < 21:
        print('%2d' % i, end=' ')
        if i % 5 == 0:
            print()
        i += 1

# while 练习 9
# 用 while 语句实现打印三角形，输入一个整数，表示三角形的宽度和高度，打印出相应的直角三角形
def ex9():
    '''用 while 语句实现打印三角形，输入一个整数，表示三角形的宽度和高度，打印出相应的直角三角形'''
    width = int(input('请输入等边三角形的宽度（正整数）：'))
    row = 1
    while row <= width:
        print('*' * row)
        row += 1

# while 练习 10
# 输入一个数字，打印以该数字为宽度的正方形
def ex10():
    '''输入一个数字，打印以该数字为宽度的正方形'''
    width = int(input('请输入正方形的宽度（正整数）：'))
    i = 1
    while i <= width:
        j = 1
        while j <= width:
            print('%d' % j, end=' ')
            j += 1
        print()
        i += 1

# for 练习 11
# 输入任意一个字符串，判断这个字符串中有几个空格，要求使用 for 语句实现
def ex11():
    '''输入任意一个字符串，判断这个字符串中有几个空格，要求使用 for 语句实现'''
    s = input('请输入一个字符串：')
    count = 0
    for c in s:
        if c == ' ':
            count += 1

    print('你输入的字符串中一共有 %d 个空格' % count)

# 练习 12
# 求 100 以内有哪些整数与自身 +1 的乘积再对 11 求余结果等于 8
def ex12():
    '''列表推导式练习'''
    print([x for x in range(101) if x * (x + 1) % 11 == 8])

# 循环练习 13
# 用 while 和 for 两种语句来计算：1 + 3 + 5 + 7 + ... + 99 的和
def ex13():
    '''循环练习'''
    i = 1
    count = 0
    while i < 100:
        count += i
        i += 2
    print('while 循环的结果：%d' % count)

    count = 0
    for j in range(1, 100, 2):
        count += j
    print('for 循环的结果：%d' % count)

# 循环练习 14
# 求多项式的和：1/1 - 1/3 + 1/5 - 1/7 + 1/9 ... + 1/(2*n - 1) 的和，n 最大取 1000000
#           1）打印这个和；2）打印这个和乘以 4 的值
def ex14():
    '''循环练习'''
    sums = 0
    x = 1
    for i in range(1, 10000001):
        sums += x / (2 * i - 1)
        x *= -1

    print(sums)
    print(sums * 4)

# 列表索引、切片练习 15
# 已知列表：L = [3, 5]，用索引和切片操作，把列表改为：L = [1, 2, 3, 4, 5, 6]；将列表反转，然后删除最后一个元素
def ex15():
    '''切片练习'''
    L = [3, 5]
    L[1:1] = [4]
    L[0:0] = [1, 2]
    L[len(L):len(L)] = [6] # L.append(6) # 这是使用方法的做法
    print('插入之后的列表为：%r' % L)
    L = L[::-1]
    print('反转后的列表：%r' % L)
    del L[-1] #L.pop() # 这是使用方法的做法
    print('删除元素后的列表：%r' % L)

# 列表练习 16
# 用户输入一些整数，当输入 -1 时结束输入：
# 1. 打印一共输入了几个数字；2. 打印最大数字；3. 打印最小数字；4. 打印输入数字的平均值；
def ex16():
    '''输入一些整数，输入 -1 结束，计算输入数字的个数、最大值、最小值、平均值'''
    L = []
    while True:
        num = int(input('请输入整数，正负均可：'))
        if num == -1:
            break
        L.append(num)

    print('一共输入了 %d 个数字\n其中最大的数字是 %d\n其中最小的数字是 %d\n输入数字的平均值是 %d' % (len(L), max(L), min(L), sum(L) / len(L)))

# 字典练习 17
# 输入一段字符串，打印出这个字符串中出现过的字符及出现过的次数
def ex17():
    '''统计输入的字符串中出现过的字符及次数'''
    s = input('请随便写点什么吧：')
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1

    for key,val in d.items():
        print('%s : %d' % (key, val))

# 综合练习 18
# 生成前 40 个斐波那锲数：1 1 2 3 5 8 13 ... （自第三个起，之后的所有数为前两个数之和）
def ex18():
    '''斐波那锲数列练习'''
    a = 0
    b = 1
    l = []
    while len(l) < 40:
        a, b = b, a + b
        l.append(a)
    print(l)

# 集合练习 19
# 经理有：曹操，刘备，周瑜，技术员有：曹操，周瑜，张飞，赵云，问：
# 1. 既是经理又是技术员的有谁；2. 是经理，但不是技术员的有谁；3. 是技术员，不是经理的有谁；4. 张飞是经理吗；5. 身兼一职的有谁；6. 经理和技术人员共有几个人；
def ex19():
    '''集合操作（交，并，补，...）练习'''
    manager = {'曹操', '刘备', '周瑜'}
    worker = {'曹操', '周瑜', '张飞', '赵云'}
    print('既是经理又是技术员的有：%r' % (manager & worker))
    print('是经理但不是技术员的有：%r' % (manager - worker))
    print('是技术员但不是经理的有：%r' % (worker - manager))
    print('张飞是经理吗？%s' % ('是' if '张飞' in manager else '不是'))
    print('身兼一职的有：%r' % (manager ^ worker))
    print('经理和技术人员共有：%d 人' % (len(manager | worker)))

# 集合练习 20
# 模拟一个点名系统，已知全班学生名单，随机打印学生的姓名进行点名，并得到此学生是否已到信息，输入 y 代表已到，输入其他代表未到场，点名结束后打印未到者名单

def ex20():
    """
    集合练习，模拟一个点名系统，输入 y 代表到，其他代表未到
    """
    names = {'张三', '李四', '王五', '刘六', '赵七', '钱八'}
    final_res = set()
    for name in names:
        res = input(name + '   是否到场(y)?   ')
        if res != 'y':
            final_res.add(name)

    print('未到的人员有：%r' % final_res)

# 函数参数练习
# 写一个函数，功能仿照 range 函数做
def ex21(start, end=None, step=1):
    '''写一个函数，功能仿照 range 函数做（只实现了正向的索引）'''
    L = []
    if not end:
        if step > 0:
            end = start
            start = 0
        else:
            end = start


    while start < end:
        L.append(start)
        start += step

    return L

# map 函数练习 22
def ex22():
    '''练习 map(func, *iterable) 函数的使用'''
    for m in map(pow, {1:2, 3:4}, {5:6, 7:8}):
        print(m)

    for m in map(pow, range(1, 3), range(1, 4)):
        print(m)

    # 生成 1 ** 4， 2 ** 3， 3 ** 2， 4 ** 1
    for m in map(pow, range(1, 5), range(4, 0, -1)):
        print(m)

# 递归函数练习 23
# l = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#   1. 打印出所有元素；2. 返回列表中所有元素的和
def ex23(l):
    '''使用递归函数打印一个列表中的所有元素，并计算这些元素的和'''
    s = 0
    for x in l:
        if type(x) is list:
            s += ex23(x)
        else:
            s += x
            print(x, end=' ')
    return s

# 时间联系 24
# 输入你出生的日期，1）计算你已经出生了几天；2）计算你出生的那天是星期几
def ex24():
    '''输入出生年、月、日，计算你已经活了多少天，计算你出生的日子是星期几'''
    y = int(input('请输入你出生的年份（4位）：'))
    m = int(input('请输入你出生的月份：'))
    d = int(input('请输入你出生的日子：'))
    date_tuplle = (y, m, d, 0, 0, 0, 0, 0, 0)
    import time
    sec = time.mktime(date_tuplle)
    cur = time.mktime(time.localtime())
    days = (cur - sec) / 60 / 60 // 24
    print('自出生你已经生活了：%d 天了' % int(days))
    birthday = time.localtime(time.mktime(date_tuplle))
    d = {
        0 : '星期一',
        1 : '星期二',
        2 : '星期三',
        3 : '星期四',
        4 : '星期五',
        5 : '星期六',
        6 : '星期天'
    }
    print('你出生在 %s' % d[birthday[6]])

# 时间函数练习 25
# 以电子时钟格式打印时间，时间格式为：HH:MM:SS，时间每隔一秒刷新一次
def ex25():
    '''打印当前时分秒，每隔一秒打印一次，直到 ctrl+c 退出'''
    import time
    print('%s\r' % (time.strftime('%H:%M:%S', time.localtime())), end='')
    time.sleep(1)
    ex25()

# 时间函数练习 26
# 编写一个闹钟程序，启动时设定时间，到预定时间后打印一句话，然后退出程序
def ex26(m):
    """
    编写一个闹钟程序，启动时设定时间，到预定时间后打印一句话，然后退出程序
        :param m: 预定时间，单位：秒
    """
    import time
    time.sleep(m)
    print('过了 %d 秒钟后，我才被打印的' % m)

# 综合练习 27
# 模拟斗地主发牌，牌 54 张（黑桃：'\u2660'，红桃：'\u2666'，梅花：'\u2663'，方块：'\u2665'）大小王 A23...10JQK
# 第一次回车，打印第一个人的17张牌；
# 第二次回车：……   二        ……；
# 第三次回车：……   三        ……；
# 输入回车： 打印三张底牌
def ex27():
    '''模拟斗地主发牌'''

    hxse = ['\u2660', '\u2666', '\u2663', '\u2665']
    point = ['A'] + [str(s) for s in range(2, 11)] + list('JQK')
    wh = ['大王', '小王']
    res = wh + [x + y for x in hxse for y in point]

    import random
    random.shuffle(res)
    input('输入回车继续：')
    print('第一个人的 17 张牌是：', res[0:17])
    input('输入回车继续：')
    print('第一个人的 17 张牌是：', res[17:34])
    input('输入回车继续：')
    print('第一个人的 17 张牌是：', res[34:51])
    input('输入回车继续：')
    print('最后的底牌是：', res[51:])

# 异常练习 28
# 写一个函数来获取学生的成绩（0~100），如果输入出现异常，则此函数返回 0，否则返回用户输入的成绩
def ex28():
    '''异常练习'''
    try:
        s = int(input('请输入学生的成绩：'))
        if s < 0 or s > 100:
            return 0
        else:
            return s
    except:
        return 0

# 生成器练习 29
# 写一个生成器函数，该函数可以生成从 0 开始的一系列整数，到 n 结束（不包括 n）
def ex29(n):
    '''生成器练习，生成 0~n 的一系列整数（不包括 n）'''
    i = 0
    while i < n:
        yield i
        i += 1

# 文件读取练习 30
# 将 info.txt 文件中的内容读取出来，打印在屏幕终端上
def ex30():
    '''将 info.txt 文件中的内容读取出来，打印在屏幕终端上'''
    try:
        f = open('info.txt')
        for line in f.readlines():
            print(line)
        f.close()
    except OSError as o:
        print('打开文件失败，原因：\n', o)

# 文件写入练习 31
# 从键盘输入电话和姓名，把输入的信息保存到 phone_book.txt 中
def ex31():
    '''从键盘输入电话和姓名，把输入的信息保存到 phone_book.txt 中'''
    try:
        f = open('phone_book.txt', 'w')
        while True:
            name = input('请输入姓名（直接回车结束）：')
            if not name:
                break
            phone = input('请输入电话：')
            f.write(name + ' ' + phone + '\n')
    except OSError as o:
        print('文件打开失败，原因：' + o)
    except:
        print('文件操作失败，原因不明！')

# 文件读取练习 32
# 读取 phone_book.txt 文件中的内容，并用表格的形式展现出来
def ex32():
    try:
        f = open('phone_book.txt')
        print('+------------+--------------------+')
        print('|   name     |      number        |')
        print('+------------+--------------------+')
        for line in f.readlines():
            name, phone = line.strip().split(' ')
            print('|%s|%s|' % (name.center(12), phone.center(20)))

        print('+----------+----------------------+')
    except OSError as o:
        print('文件打开失败，原因：', o)
    except:
        print('文件打开失败，原因不明！')

if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    # ex13()
    # ex14()
    # ex15()
    # ex16()
    # ex17()
    # ex18()
    # ex19()
    # ex20()
    # print(ex21(10))
    # print(ex21(3, 10))
    # print(ex21(1, 10, 2))
    # ex22()
    # print('列表的总和是：%d' % (ex23([[3, 5, 8], 10, [[13, 14], 15, 18], 20])))
    # print()
    # ex24()
    # ex25()
    # ex26(3)
    # ex27()
    # print(ex28())
    # it = iter(ex29(29))
    # while True:
    #     try:
    #         print(next(it))
    #     except StopIteration:
    #         break
    # ex30()
    # ex31()
    ex32()