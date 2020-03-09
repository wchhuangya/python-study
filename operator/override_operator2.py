# 运算符重载

class MyList:
    '''让自己定义的类也拥有类似 list + 的操作'''
    def __init__(self, iterable):
        self.data = list(iterable)

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __repr__(self):
        '''使用自定义的 __repr__ 方法，友好的显示 MyList 的值'''
        return '%r' % self.data

if __name__ == '__main__':
    l1 = MyList([1, 2, 3])
    l2 = MyList([7, 8, 9])
    l3 = l1 + l2
    print(l3)