

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
    width = int(input('请输入矩形的宽度（正整数）：'))
    for i in range(1, 5):
        if i == 1 or i == 4:
            print('#' * width)
        else:
            print('#' + ' ' * (width-2) + '#')

# 字符串练习 4
# 输入一个字符串，把字符串的第一个字符和最后一个字符去掉，打印出处理后的字符串
def ex4():
    s = input('请输入一个字符串：')
    print('原字符串是：%s\n去掉头尾的字符串是：%s' % (s, s[1:-1]))

# 字符串练习 5
# 输入任意一个字符串，判断这个字符串是否是回文，回文指中心对称的文字，即把字符正序显示和倒序显示是一样的
def ex5():
    s = input('请输入一个字符串：')
    print('你输入的字符串 %s 回文' % ('是' if s == s[::-1] else '不是'))

# 字符串方法练习 6
# 输入一个字符串：1. 判断输入的字符串有几个空格；2. 将原字符串的左右空格去掉，打印出有效字符的长度；3. 判断输入是否数字
def ex6():
    s = input('请输入一个字符串：')
    nums = s.count(' ')
    print('你一共输入了 %d 个空格' % nums)
    ss = s.strip()
    print('去掉字符串前后的空格的字符串长度是：%s' % len(ss))
    print('你输入的 %s 数字' % ('是' if ss.isdigit() else '不是'))

# 格式化字符串练习 7
# 输入 3 行文字，1. 让这些文字依次以 20 字符的宽度右对齐输出；2. 以最长字符串的长度进行右对齐显示；
def ex7():
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
    i = 1
    while i < 21:
        print('%2d' % i, end=' ')
        if i % 5 == 0:
            print()
        i += 1

# while 练习 9
# 用 while 语句实现打印三角形，输入一个整数，表示三角形的宽度和高度，打印出相应的直角三角形
def ex9():
    width = int(input('请输入等边三角形的宽度（正整数）：'))
    row = 1
    while row <= width:
        print('*' * row)
        row += 1

# while 练习 10
# 输入一个数字，打印以该数字为宽度的正方形
def ex10():
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
    s = input('请输入一个字符串：')
    count = 0
    for c in s:
        if c == ' ':
            count += 1

    print('你输入的字符串中一共有 %d 个空格' % count)

# 练习 12
# 求 100 以内有哪些整数与自身 +1 的乘积再对 11 求余结果等于 8
def ex12():
    print([x for x in range(101) if x * (x + 1) % 11 == 8])

# 循环练习 13
# 用 while 和 for 两种语句来计算：1 + 3 + 5 + 7 + ... + 99 的和
def ex13():
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

    L = []
    while True:
        num = int(input('请输入整数，正负均可：'))
        if num == -1:
            break
        L.append(num)

    print('一共输入了 %d 个数字\n其中最大的数字是 %d\n其中最小的数字是 %d\n输入数字的平均值是 %d' % (len(L), max(L), min(L), sum(L) / len(L)))

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
    ex16()