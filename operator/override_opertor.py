# 运算符重载
## 算数运算符所对应的私有方法：
### __add__(self, rhs)       self + rhs  加法
### __sub__(self, rhs)       self - rhs  减法
### __mul__(self, rhs)       self * rhs  乘法
### __truediv__(self, rhs)   self / rhs  除法
### __floordiv__(self, rhs)  self // rhs 地板除
### __pow__(self, rhs)       self ** rhs 幂

## 反向操作符
### __radd__(self, lhs)       lhs + self  加法
### __rsub__(self, lhs)       lhs - self  减法
### __rmul__(self, lhs)       lhs * self  乘法
### __rtruediv__(self, lhs)   lhs / self  除法
### __rfloordiv__(self, lhs)  lhs // self 地板除
### __rpow__(self, lhs)       lhs ** self 幂

## 复合赋值操作运算符
### __iadd__(self, rhs)       self += rhs  加法
### __isub__(self, rhs)       self -= rhs  减法
### __imul__(self, rhs)       self *= rhs  乘法
### __itruediv__(self, rhs)   self /= rhs  除法
### __ifloordiv__(self, rhs)  self //= rhs 地板除
### __ipow__(self, rhs)       self **= rhs 幂
### 注意：当以上方法不存在时，会把复合赋值运算符拆开，然后在进行计算，比如：self += rhs，会拆成 self = self + rhs

## 比较运算符重载
### __lt__(self, rhs)         self <  rhs  小于
### __le__(self, rhs)         self <= rhs  小于等于
### __gt__(self, rhs)         self >  rhs  大于
### __ge__(self, rhs)         self >= rhs  大于等于
### __eq__(self, rhs)         self == rhs  等于
### __ne__(self, rhs)         self != rhs  不等于
### 注意：比较运算符通常返回 True 或 False

## 位运算符重载
## __invert__(self)           ~self        取反
## __and__(self, rhs)         self &  rhs  位与
## __or__(self, rhs)          self |  rhs  为或
## __xor__(self, rhs)         self ^  rhs  位异或
## __lshift__(self, rhs)      self << rhs  左移
## __rshift__(self, rhs)      self >> rhs  右移

## 反向位运算符重载
## __rand__(self, lhs)         lhs &  self  位与
## __ror__(self, lhs)          lhs |  self  为或
## __rxor__(self, lhs)         lhs ^  self  位异或
## __rlshift__(self, lhs)      lhs << self  左移
## __rrshift__(self, lhs)      lhs >> self  右移
## 注意：当 lhs 是系统内建的，无法改变的类型时，可以使用反向位运算符重载

## 复合赋值位运算符重载
## __iand__(self, lhs)         lhs &=  self  位与
## __ior__(self, lhs)          lhs |=  self  为或
## __ixor__(self, lhs)         lhs ^=  self  位异或
## __ilshift__(self, lhs)      lhs <<= self  左移
## __irshift__(self, lhs)      lhs >>= self  右移
## 注意：当 lhs 是系统内建的，无法改变的类型时，可以使用反向位运算符重载

## 一元运算符的重载
## __neg__(self)               + self 负号
## __pos__(self)               - self 正号
## __invert__(self)            ~ self 取反

## in / not in 运算符重载
## __contains__(self, e)       e in self  成员运算

## 索引和切片运算符的重载
## __getitem__(self, i)        x = self[i]  索引/切片取值
## __setitem__(self, i, v)     self[i] = v  索引/切片赋值
## __delitem__(self, i)        del self[i]  del 语句删除索引

# 总体说明：运算符重载不能改变运算符的优先级

class Employee(object):
    '''雇员类：
    构造函数收集雇员的两类信息：姓名（name），拥有图书的数量（book_nums）
    '''
    def __init__(self, name, book_nums, program_nums):
        self.name = name
        self.book_nums = book_nums
        self.program_nums = program_nums

    def selfAdd(self, another):
        '''自定义类的一个普通的方法，用于演示与 __add__ 方法的区别'''
        return self.book_nums + another.book_nums

    def __add__(self, rhs):
        '''自定义的 + 号方法的实现'''
        return self.book_nums + rhs.book_nums

    def __mul__(self, rhs):
        '''类中自定义乘法的实现'''
        return self.program_nums * rhs.book_nums

    def __rmul__(self, lhs):
        '''反向操作符乘法的实现，即我们自定义的对象在右边，数字在左边
        注意：类的实例将传递给 self 变量，数字将传递给 lhs 变量；如果不定义该方法，直接使用 2 * 类实例 进行计算，会报错
        '''
        return self.program_nums * lhs

    def __itruediv__(self, rhs):
        '''整除复合赋值运算符的自定义实现'''
        self.program_nums /= rhs
        return self

    def __repr__(self):
        '''自定义实现 __repr__ 方法，打印雇员的程序数量'''
        return '%d' % self.program_nums

if __name__ == '__main__':
    e1 = Employee('张三', 23, 12)
    e2 = Employee('李四', 8, 12)
    print('两人共有 %d 本书（普通方法）' % (e1.selfAdd(e2)))
    print('两人共有 %d 本书（__add__方法）' % (e1 + e2))
    print('两人共有 %d 本书（直接调用私有方法）' % (e1.__add__(e2)))
    print('说明：+ 的本质就是调用 __add__ 私有方法')
    print('两个人程序数量的乘积是：%d' % (e1 * e2))
    print('张三通过自己的努力，程序数量翻倍，他现在程序的数量是：%d' % (2 * e1))
    e1 /= 2
    print('张三沉迷于网络爱情，程序数量骤减，他现在程序的数量时：%r' % e1)