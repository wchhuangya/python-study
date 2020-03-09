# 运算符重载
## 算数运算符所对应的私有方法：
### __add__(self, rhs)       self + rhs  加法
### __sub__(self, rhs)       self - rhs  减法
### __mul__(self, rhs)       self * rhs  乘法
### __truediv__(self, rhs)   self / rhs  除法
### __floordiv__(self, rhs)  self // rhs 地板除
### __pow__(self, rhs)       self ** rhs 幂

class Employee(object):
    '''雇员类：
    构造函数收集雇员的两类信息：姓名（name），拥有图书的数量（book_nums）
    '''
    def __init__(self, name, book_nums):
        self.name = name
        self.book_nums = book_nums

    def selfAdd(self, another):
        '''自定义类的一个普通的方法，用于演示与 __add__ 方法的区别'''
        return self.book_nums + another.book_nums

    def __add__(self, rhs):
        '''自定义的 + 号方法的实现'''
        return self.book_nums + rhs.book_nums

if __name__ == '__main__':
    e1 = Employee('张三', 23)
    e2 = Employee('李四', 8)
    print('两人共有 %d 本书（普通方法）' % (e1.selfAdd(e2)))
    print('两人共有 %d 本书（__add__方法）' % (e1 + e2))
    print('两人共有 %d 本书（直接调用私有方法）' % (e1.__add__(e2)))
    print('说明：+ 的本质就是调用 __add__ 私有方法')