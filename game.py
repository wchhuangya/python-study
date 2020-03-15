import random

'''
    这是一个经典的数字游戏，小时候在文曲星上玩过。
    为了提高小孩对数字的敏感性，特把这个游戏做到电脑端。
    希望能起到积极的作用。
    @author wchya
    @date-time 2020年03月15日22:57:27
'''

def generate_nums():
    '''生成 4 位互不相同的数字'''
    return ''.join([str(s) for s in random.sample(range(0, 10), 4)])

def game_run(s):
    """
    运行游戏的方法
        :param s: 一个字符串，内容是系统生成的最终答案
    """
    is_win = False
    is_wrong = False
    for item in range(1,9):
        i1 = input('请输入4位数字(以空格分隔数字，当前是第 %d 次，一共 8 次)：\n' % item)
        arr = i1.split(' ')
        if len(arr) != 4:
            print('你不按规矩出牌，游戏结束！o(╥﹏╥)o')
            is_wrong = True
            break
        a_count = 0
        b_count = 0
        for ii in range(0,4):
            if arr[ii] == s[ii]:
                a_count += 1
            else:
                if arr[ii] in s:
                    b_count += 1

        if a_count == 4:
            is_win = True
            break
        else:
            print('%d A %d B' % (a_count, b_count))
    return is_win, is_wrong, item

def main():
    # 游戏提示
    print('''游戏名称：猜数字（文曲星经典游戏），规则：
    1. 系统生成 4 位数字，每一位上的数字不重复；
    2. 用户输入自己猜测的 4 位数字，按回车进行验证
    3. 系统判断：
        3.1 如果在同样的位置上，用户输入一样的数字，则得到 1 个 A
        3.2 如果用户输入的数字猜对了，但是位置不对，则得到 1 个 B
    4. 一共只有 8 次机会猜测
    ''')

    s = generate_nums()
    # 游戏运行，得到运行结果
    is_win, is_wrong, times = game_run(s)

    if not is_wrong:
        if is_win:
            print('恭喜你，猜对了，一共猜了 %d 次' % times)
        else:
            print('很遗憾，你没有猜对，正确的答案是：%s' % s)

if __name__ == '__main__':
    main()