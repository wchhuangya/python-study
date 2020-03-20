# 初衷
只是为了好好的学习一下 Python，顺便再做一个记录。一是便于查找与复习；二是致敬曾经学过的习。

[Toc]

# 总述
## 适合的领域
1. Web 网站和各种网络服务

2. 系统工具和脚本

3. 作为胶水语言把其他语言开发的模块包装起来，方便使用

## 不适合的领域
1. 贴近硬件的代码（首选 `C` 开发），比如驱动程序

2. 移动开发，因为它们有各自的开发语言

3. 游戏开发（`C/C++`），因为速度要求高

## 与其他语言的对比
![](index_files/0d9a50db-aa3d-454e-980f-5e95db94565b.jpg)

## 劣势
1. 速度慢

2. 源码不能加密

# 基础知识
## 交互模式
1. 进入方法：在命令行中输入 `python3`

## 字符常识
1. 计算机只能处理数字，如果计算机要处理文本，就需要把文本转换为数字才能处理

2. 最早的计算机在设计时采用 `8` 比特（`bit`）表示一个字节（`byte`），所以一个字节能表示的最大的数字就是 `255`（`0b11111111`）

3. `0~255` 被用来表示大小写英文字母、数字和一些字符，这个编码表被称为 `ASCII` 编码,比如：`A` 的编码是 `65`，`z` 的编码是 `122`

## 运行 Python 的方式
1. 在当前目录打开命令行，在命令行中输入：`python3 xx.py`

2. 先修改 `.py` 文件的权限：`chmod +x .py；`；然后在 `.py` 文件的第一行输入 `python` 的环境变量地址（如下所示），最后在任意目录下打开命令行，输入：`./xx.py`

    ```python
    #! /usr/bin/python3
    ```

## 变量
1. 用来绑定数据对象的标识符

2. 大小写英文、数字、下划线的组合

3. 不能以数字开头

4. 不能使用 `Python` 的关键字

## 换行
1. 显示换行使用换行符：`\`

2. 隐式换行：所有括号内的换行

## 运算符
### 算术运算符

| 运算符 | 描述 | 实例
| --- | --- | ---
| + | 加 - 两个对象相加 | a + b 输出结果 30
| - | 减 - 得到负数或是一个数减去另一个数 | a - b 输出结果 -10
| * | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 200
| / | 除 - x除以y | b / a 输出结果 2
| % | 取模 - 返回除法的余数 | b % a 输出结果 0
| ** | 幂 - 返回x的y次幂 | a**b 为10的20次方， 输出结果 100000000000000000000
| // | 取整除 - 返回商的整数部分（向下取整） | 9//2 = 4,-9//2 = -5

### 比较运算符

| 运算符 | 描述 | 实例
| --- | --- | ---
| == | 等于 - 比较对象是否相等 | (a == b) 返回 False。
| != | 不等于 - 比较两个对象是否不相等 | (a != b) 返回 true.
| > | 大于 - 返回x是否大于y | (a > b) 返回 False。
| < | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。 | (a < b) 返回 true。
| \>= | 大于等于 - 返回x是否大于等于y。 | (a \>= b) 返回 False。
| <= | 小于等于 -	返回x是否小于等于y。 | (a <= b) 返回 true。

### 赋值运算符

| 运算符 | 描述 | 实例
| --- | --- | ---
| = | 简单的赋值运算符 | c = a + b 将 a + b 的运算结果赋值为 c
| += | 加法赋值运算符 | c += a 等效于 c = c + a
| -= | 减法赋值运算符 | c -= a 等效于 c = c - a
| *= | 乘法赋值运算符 | c *= a 等效于 c = c * a
| /= | 除法赋值运算符 | c /= a 等效于 c = c / a
| %= | 取模赋值运算符 | c %= a 等效于 c = c % a
| \*\*= | 幂赋值运算符 | c \*\*= a 等效于 c = c \*\* a
| //= | 取整除赋值运算符 | c //= a 等效于 c = c // a

### 位运算符
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
下表中变量 a 为 60，b 为 13，二进制格式如下：
```python
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011
```

| 运算符 | 描述 | 实例
| --- | --- | ---
| & | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100
| &#166; | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a &#166; b) 输出结果 61 ，二进制解释： 0011 1101
| ^ | 按位异或运算符：当两对应的二进位相异时，结果为1 | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
| ~ | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1 | (~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。
| << | 左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000
| \>\> | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，\>\> 右边的数字指定了移动的位数 | a \>\> 2 输出结果 15 ，二进制解释： 0000 1111

### 逻辑运算符
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:

| 运算符 | 逻辑表达式 | 描述 | 实例
| --- | --- | --- | ---
| and | x and y | 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 | (a and b) 返回 20。
| or | x or y | 布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。 | (a or b) 返回 10。
| not | not x | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False

### 成员运算符

| 运算符 | 描述 | 实例
| --- | --- | ---
| in | 如果在指定的序列中找到值返回 True，否则返回 False。 | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

### 身份运算符

| 运算符 | 描述 | 实例
| --- | --- | ---
| is | is 是判断两个标识符是不是引用自一个对象 | x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
| is not | is not 是判断两个标识符是不是引用自不同对象 | x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

### 运算符优先级

| 运算符 | 描述
| --- | ---
| ** | 指数 (最高优先级)
| ~ + - | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
| * / % // | 乘，除，取模和取整除
| + - | 加法减法
| \>\> << | 右移，左移运算符
| & | 位 'AND'
| ^ &#166; | 位运算符
| <= < \> \>= | 比较运算符
| <\> == != | 等于运算符
| = %= /= //= -= += `*=` **= | 赋值运算符
| is is not | 身份运算符
| in not in | 成员运算符
| not and or | 逻辑运算符

### 运算符重载
1. 所有运算符都是方法，也就是说都可以重载
2. 运算符重载的好处
    2.1 让自定义的类生成的对象（实例）可以使用运算符进行操作
    2.2 让程序简洁易读
    2.3 对自定义的对象，将运算符赋予新的运算规则

## 语句
### 赋值语句
1. 用于创建一个变量，并把变量绑定或关联在一个对象上
2. 赋值方法：
    2.1 `变量名 = 表达式`
    2.2 `变量名1 = 变量名2 = 表达式`
    2.3 `变量1, 变量2, ... = 对象1, 对象2, ... | (对象1, 对象2, ... | [对象1, 对象2, ...])`
3. 说明
    3.1 当变量不存在时，创建这个变量同时绑定在这个对象上
    3.2 当变量存在时，改变该变量绑定的对象
    3.3 一个变量只能绑定一个对象
    3.4 两个变量可以同时绑定一个对象

### 条件语句
1. 让程序根据条件选择性的执行某条/些语句
2. 语法

```python
if 真值表达式1:
    语句1
elif 真值表达式2:
    语句2
elif 真值表达式3:
    语句3
...
else:
    最终语句
```

### 空语句
1. `pass`：用来填充语法空白

### 循环语句
#### while
1. 根据一定的条件，重复的执行一条或多条语句，直到条件不成立则退出循环
2. 语法

```python
while 真值表达式:
    语句块
else:
    语句块
```

### for
1. 用来遍历可迭代对象的数据元素
2. 语法

```python
for 变量列表 in 可迭代对象:
    语句1
else:
    语句2
```

### break
1. 只能用于循环语句（`while、for` 语句）中，用来终止当前循环语句的执行；
2. 当 `break` 语句执行后，此循环语句 `break` 之后的语句将不再执行
3. `break` 语句只能当前循环语句的执行，如果有循环嵌套时，不会跳出嵌套的外层循环

### continue
1. 用于循环语句（`while，for`）中，不再执行本次循环中 `continue` 后面的语句，重新开始一次新的循环
2. 在 `while` 语句中，执行 `continue` 语句将会直接跳转到 `while` 语句的真值表达式处重新判断循环条件
3. 在 `for` 语句中，执行 `continue` 语句，将会从可迭代对象中取下一个元素，绑定变量后再次进行循环

## 数据类型
### 可以直接处理的数据类型
#### 小整数对象池
`CPython` 中，`-5 至 256` 永远存在于小整数对象池中，不会释放并可重复使用

#### 整数
1. 包含正整数、负整数
2. 表示方法与数学上的写法一模一样
3. 整数与整数的计算结果是精确的，也是整数
4. 整数与浮点数的计算结果是浮点数
5. 非十进制数表示方式
    5.1 二进制：`0b前缀`
    5.2 八进制：`0o前缀`
    5.3 十六进制：`0x前缀`

#### 浮点
1. 也就是小数
2. 浮点数与浮点数计算的结果是浮点数
3. 浮点数的运算可能会有四舍五入的误差
4. **不能使用 == 或者 != 直接判断浮点数的相等和不相等（精度问题）**

#### 布尔
1. `True`：值为 1，其他为 `True` 的情况：非 0 数字，非空（字符串、元组、列表、字典、集合...）
2. `False`：值为 0，其他为 `False` 的情况：数字 0，空字符串、空元祖、空列表、空字典、空集合...，None
3. 短路计算法则：
    3.1 在计算 a and b 时，
    如果 a 为 False，根据运算法则，整个表达式结果必为 False，所以返回 a；
    如果 a 为 True，根据运算法则，整个表达式的结果取决于 b，所以返回 b
    3.2 在计算 a or b 时，
    如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；
    如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。

#### 空值
1. 一个特殊的值，用 `None` 表示，表示一个不存在的特殊对象
2. 作用：
    2.1 用来占位
    2.2 用来解除变量绑定
3. 判断一个值是否为 `None` 的方式：`object is None`

### 内建序列
#### 通用操作
##### 索引
1. 序列中的每一个元素都分配一个数字（从0开始），代表元素在序列中的位置
2. 可以使用索引来访问序列中的元素
3. 获取元素方式：变量名[索引]
4. 设置序列值方式：变量名[索引] = 值
5. 可以正向索引，也可以反向索引
    5.1 正向索引从 0 开始，然后依次递增
    5.2 反向索引从 -1 开始，然后依次递减

##### 切片
1. 对序列中一定范围内的元素进行访问
2. 切片方式：序列 [(开始索引b) : (结束索引e) : (步长s)]
3. 开始索引一定要小于结束索引，否则结果是空序列
4. 结束索引可以越界
5. 切片赋值语法
    5.1 可变序列[切片] = 可迭代对象
    5.2 步长不为 1 的切片赋值：
    赋值运算符右侧的可迭代对象提供元素的个数一定要等于切片切出的段数
    5.3 **切片赋值的右边一定是可迭代对象**

##### in/not in
1. 用于序列、字典、集合中，用于判断某个值是否存在于容器中
2. 存在返回 `True`，不存在返回 `False`
3. 用法：`对象 in 容器`

#### 不可变序列
##### str（字符串）
1. 在 **非注释中**，凡是用引号括起来的都是字符串
2. 引号有：单引号——`'`，双引号——`"`，三单引号——`'''`，三双引号——`"""`
3. 构造函数：`str(object='')`，用于将对象转换为字符串
4. 三引号字符串
    4.1 三引号字符串内的换行会自动转换为换行符：`\n`
    4.2 三引号字符串内可以包含单引号和双引号
5. 在电脑的命令行中输入：`man ascii` 这个命令，就可以打印出电脑上的 `ASCII` 码表
6. `raw（原始）字符串` ： 让转义字符无效，格式：`r'|"|'''|"""字符串'|"|'''|"""`
7. 运算
    8.1 `*`：用于生成重复字符串，`*` 后面只能用整数
    8.2 `+`：用于字符串连接
    8.3 `比较运算`：字符串的比较是比较 `ASCII` 码表中的编码值
8. 格式化字符串：`%`，用于生成一定格式的字符串：`格式字符串 % (参数1，参数2，...)`
9. 占位符

占位符 | 意义
- | -
%s | 字符串，使用 str 函数转换
%r | 字符串，使用 repr 函数转换
%c | 整数转换为单个字符
%d | 十进制数
%o | 八进制数
%x | 十六进制数（a-z小写）
%X | 十六进制数（A-Z大写）
%e | 指数型浮点数（e小写）
%E | 指数型浮点数（E大写）
%f，%F | 浮点十进制形式
%g，%G | 十进制形式浮点数或指数浮点数自动转换
%% | 等同于一个 %

> 占位符与类型码（s，r，d……）之间可以添加格式语法
1. `-` ： 左对齐
2. `+` ： 显示正号
3. `0` ： 补 0
4. 宽度（适用于整数）
5. 宽度.精度（适用于整数或浮点数）

转移字符表：

| 转义字符 | 意义
| --- | ---
| `\'` | 单引号
| `\"` | 双引号
| `\\` | 反斜杠
| `\n` | 换行
| `\r` | 返回光标至行首
| `\f` | 换页
| `\t` | 水平制表符
| `\v` | 垂直制表符
| `\b` | 退格
| `\0` | 空字符
| `\0oo` | oo 为两位 8 进制表示的字符
| `\xXX` | XX 为两位 16 进制表示的字符
| `\uXXXX` | Unicode16 的 16 进制表示的字符
| `\uXXXXXXXX` | Unicode32 的 16 进制表示的字符

##### tuple（元组）
1. 元组可以存放任何数据，一旦生成，不可改变
2. 用 () 括起来的元素集合
3. **为了区分是单个对象还是元组，单个元素括起来用逗号 (item,) 表示一个数据的元组**
4. 元组是不可变序列，所以不支持复制操作
5. 创建
    5.1 字面值：`t = 200,   t = (200,)   t = 100, 200   t = (100, 200)`
    5.2 构造函数：
    `tuple()`：生成一个空元组
    `tuple(iterable)`：用可迭代对象生成一个元组
6. 元组的 `+=` 操作：因为元组不可变，所以该操作符最终生成的新元组与原来两个元组的地址都不同，并且在生成新元组的同时，原来的两个旧元组都被自动销毁了

##### bytes（字节串）
1. 存储以字节为单位的数据
2. 字节是 0~255 之间的整数
3. 创建
    3.1 空字节串字面值：`b''`，`B''`
    3.2 非空字节串的字面值：`b'ABCD'`，`b'\x41\x41'`
4. 构造函数
    4.1 `bytes()`：生成一个空字节串
    4.2 `bytes(整形可迭代对象)`：用整形可迭代对象初始化一个字节串，整数不能大于 255
    4.3 `bytes(整数n)`：生成的字节串长度为 n，里面都是 0
    4.4 `bytes(字符串，encoding='utf-8')`：用字符串的转换编码生成一个字节串
5. bytes 与 str 的区别：
    5.1 bytes 存储字节（0~255）
    5.2 str 存储 Unicode 字符（0~65535）
6. bytes 与 str 转换：
    5.2 `b = s.encode('utf-8')`
    5.2 `s = b.decode('utf-8')`

#### 可变序列
##### list（列表）
1. 列表是由 `[]` 括起来的元素集合，元素和元素之间没有任何关联关系，但它们之间有先后顺序关系
2. 列表里的元素类型可以不同
3. 创建方式：`[]`，`list(iterable)`
4. 饮用方式：`列表[下标]`
5. 赋值方式：`列表[下标] = 值`
6. 删除元素：`del 列表[下标]`
7. 分片赋值：`列表[start:end] = 新值`，可用于字符替换、删除等
8. 列表推导式：
    8.1 使用可迭代对象依次生成带有多个元素的列表的表达式
    8.2 作用：用简易方法生成列表
    8.3 语法：`[表达式 for 变量 in 可迭代对象]` 或者 `[表达式 for 变量 in 可迭代对象 if 真值表达式]`
    8.4 嵌套：`[表达式1 for 变量1 in 可迭代对象1 if 真值表达式1 表达式2 for 变量2 in 可迭代对象2 if 真值表达式2]`
9. 列表与字符串相加，是先把字符串转换为列表，然后再进行拼接
10. 两个列表比较时，抽取响应位置上的元素依次比较，相同位置上的元素必须类型相同，否则会报错

##### dict（字典）
1. 可以存储任意类型的数据，每个数据都是用键进行索引，数据没有先后顺序
2. 字典的键不能重复，且只能使用不可变类型的数据
3. 创建：
    3.1 字面值：用 `{}` 括起来，以 `:` 分割键值对，各键值对用 `,` 分隔
    3.2 构造函数
    `dict()`：创建一个空字典，相当于 `{}`
    `dict(可迭代对象)`：用可迭代对象初始化一个字典
    `dict(**kwargs)`：关键字传参形式创建一个字典
4. 取值：`字典[键]`，如果获取值的键不存在于字典内，则会抛出错误
5. 添加/修改：`字典[键] = 表达式`
6. 删除：`del 字典[键]`
7. 字典是可迭代对象，但只能对键进行迭代访问
8. 推导式：
    8.1 用可迭代对象依次生成字典内元素的表达式
    8.2 `{键表达式 : 值表达式 for 变量 in 可迭代对象 [if 真值表达式]}`

##### 字典 VS 列表
1. 都是可变的容器
2. 索引方式不同（列表用整数索引，字典用键索引）
3. 字典的查找速度可能快于列表
4. 列表的存贮是有序的，字典的存储是无序的

##### set（集合）
1. 集合中的数据是唯一的
2. 集合是无序的存储结构
3. 集合内的元素必须是不可变对象
4. 集合是可迭代的
5. 集合相当于只有键没有值得字典
6. 创建
    6.1 构造函数
    `set()`：创建一个空集合
    `set(iterable)`：用可迭代对象创建一个新的集合对象。注意：如果使用字典生成集合，那么，只有键会被拿出来
    6.2 字面值：`{1, 2, 3}`
7. 运算
    7.1 交集：`s1 & s2` 两个集合中共有的那部分
    7.2 并集：`s1 | s2` 既存在于 s1 中有存在于 s2 中的所有对象的集合
    7.3 补集：`s1 - s2` 属于 s1 但不属于 s2 的所有元素的集合
    7.4 对称补集：`s1 ^ s2` 等同于 `(s1 - s2) | (s2 - s1)`
    7.5 子集：`<` 判断一个集合是另外一个集合的子集
    7.6 超集：`>` 判断一个集合是另外一个集合的超集
    7.7 判断相同/不相同：`== != >= <=` 是否相等只与集合中元素的个数与值有关，与元素的顺序无关
8. 推导式：`{表达式 for 变量 in 可迭代对象 [if 真值表达式]}`

###### 固定集合
1. 不可变的，无序的，含有唯一元素的集合
2. 可以作为字典的键，也可以作为集合的值（元素）
3. 创建
    3.1 构造函数
    `frozenset()`
    `forzenset(可迭代对象)`
4. 运算：等同于 set，但没有修改集合的方法

##### bytearray（字节串数组）

##### 经典 Bug

```python
s1 = {1, 2}
s2 = {3, 4}
s = s1
s1 = s1 | s2  # 这时，s1 | s2 会生成一个新的的对象，s 与 s1 不再指向同一对象
s1 |= s2  # 这时，并没有生成新的对象，只是修改了 s1 原来指向的对象
```

## 拷贝
### 浅拷贝
1. 是指在复制的过程中只复制一层变量，不会复制深层变量绑定的对象的复制过程
2. 方法：`对象.copy()`

### 深拷贝
1. 通常只对可变对象进行复制，不可变对象通常不变
2. 方法：

```python
import copy
obj1 = copy.deepcopy(obj2)
```

## 函数
1. 函数是可以重复执行的语句块，可以重复使用；少用全局变量，多用函数
2. 函数可以封装语句块，提高代码重用性

### 创建
```python
def 函数名(形参列表):
	语句块
```
> 函数名与变量名的命名方式完全一致

### 调用：
1. 语法：`函数名(实际调用传递参数列表，即实参)`
2. 函数调用是一个表达式
3. 如果没有 `return` 语句，函数执行完毕后返回 `None` 对象；如果函数需要返回其他的对象，需要 `return` 语句

### 文档字符串
1. 函数内部，第一个没有赋值给任何变量的字符串为文档字符串
2. 用三引号 `'''|"""` 可以让文档字符串保持原来的格式
3. 文档字符串可以用 `help(函数名称)` 的方式进行查看

### 说明
1. 函数的名字就是语句块的名称
2. 函数有自己的命名空间，在函数外部不可以访问函数内部的变量，在函数内部可以访问函数外部的变量，通常需要函数处理外部数据时，需要使用参数给函数传递一些数据
3. 函数的参数列表可以为空
4. 语句部分不能为空，如果为空需要填写 `pass` 语句

### return 语句
1. 语法：`return [表达式]`
2. 用于函数中，结束函数当前的执行，返回到调用该函数的地方，同时返回一个对象的引用关系
3. `return` 之后的表达是可以省略，相当于 `return None`
4. 如果函数没有 `return` 语句，则函数执行完最后一条语句后返回 `None`

### 参数传递
#### 位置传参
实参的对应关系与形参的对应关系是按照位置来依次对应的，实参和形参通过位置进行传递
```python
def myfun(a, b, c):
	pass

myfun(1, 2, 3) # 位置传参中，实参个数与形参个数必须相同
```
#### 序列传参
在函数调用过程中，用 * 将序列拆解后按位置传参的方式进行参数传递
```python
def myfun(a, b, c):
	pass

s = [1, 2, 3]
myfun(*s) # * 表示吧 s 拆开，下同
s2 = 'ABC'
myfun(*s2)
```
#### 关键字传参
指在参数传递时，按照形参的名称来给形参赋值，形参和实参按照名称进行匹配，和参数的位置没有任何关系
```python
def myfun(a, b, c):
	pass

myfun(b=32, c=22, a=11)
```
#### 字典关键字传参
指实参为字典，用 \*\* 将字典拆解后进行关键字传参。**注意：** 1. 字典的键名和形参名必须一致；2. 字典键名必须为字符串；字典的键名要在形参中存在
```python
def myfun(a, b, c):
	pass

d = {'c': 33, 'b': 22, 'a': 11}
myfun(**d) # 拆解字典后再传参
```
#### 综合传参
函数的传参方式，在确定形参能唯一匹配到相应实参的情况下可以任意组合。**注意：**传参时，先位置传参，后关键字传参
```python
def myfun(a, b, c):
	pass

myfun(100, *[200, 300]) # 正确
myfun(*'AB', 300) # 正确
myfun(100, c=300, b=200) # 正确
myfun(100, **{'c': 300, 'b': 200}) # 正确
myfun(**{'c': 3, 'b'： 2}， a=1) # 正确
myfun(b=2, c=3, 1) # 错误，不能确定 1 给谁
```
#### 缺省参数
带有默认值的形参。**注意：**如果一个参数有缺省参数，那它右边的参数都必须是缺省参数；一个函数可以有 0 个或多个缺省参数，也可以全部是缺省参数
```python
def myfun(a, b=1, c=2):
	pass

myfun(0) # 正确
myfun(0, 10) # 正确
myfun(0, 10, 20) # 正确
myfun() # 错误
myfun(0, 10, 20, 30) # 错误
```
#### 星号元组形参
收集多个位置参数，元组形参名通常用 `args`
```python
def myfun(*元组名称):
	pass

myfun(1) # 正确
myfun(1, 2, 3, 4, 5) # 正确
```
#### 命名关键字形参
必须使用关键字传参或者字典关键字传参。形参列表中如果有 `*`，那么 `*` 右边的参数必须全部是关键字参数；如果只有一个 `*`，那它只是一个占位符用来标识右边的全是关键字参数，如果 `*` 后面有变量名，那么它就是一个实际的星号元组形参，可以接受任意多个参数
```python
def myfun(*[args], a, b):
	pass

myfun(a=1, b=2) # 合法
myfun(1, 2) # 不合法，不能使用位置传参，需要使用关键字传参
```
#### 双星号字典形参
收集多个关键字传参，通常字典形参名为 `kwargs`
```python
def myfun(**kwargs):
	pass

myfun(a=1, b=2) # 合适
myfun() # 合适
```
#### 函数参数自左到右的顺序
位置形参，星号元组形参，命名关键字形参，双星号字典形参

#### 函数的不定长参数
可以接受任意的位置传参和关键字传参
```python
def myfun(*args, **kwargs):
	pass

myfun(1, 3, 5, a=1, b=2, c=3, d=4) # 合适
myfun(1) # 合适
myfun(a=1) # 合适
```
### 局部变量
定义在函数内部的变量
1. 局部变量只能在其被申明的函数内部使用
2. 局部变量在函数被调用时创建，在函数调用之后自动销毁
3. 在函数内首次对变量赋值是创建局部变量，再次为变量赋值是修改局部变量的绑定关系
4. 在函数内部的赋值语句不会对全局变量造成影响

### 全局变量
定义在函数外部，模块内部的变量
1. 所有的函数都可以直接访问全局变量
2. 函数内部不能直接为全局变量赋值

### `globals()`
返回当前全局作用域内变量的字典

### `locals()`
返回当前局部作用域内变量的字典

### `nonlocal` 申明语句
`nonlocal` 申明的变量不是局部变量，也不是全局变量，而是外部嵌套函数内的变量
1. 当有两层或两层以上的函数嵌套时，访问 `nonlocal` 变量只对最近一层的变量进行操作
2. `nonlocal` 语句的变量列表里的变量名，不能出现在次函数的参数列表中

### `global` 申明语句
`global` 语句只能在函数内部申明，用于在函数内部访问/申明全局变量
1. `global` 变量列表里的变量不能出现在此作用域范围内的形参列表里

### `lambda` 表达式：
1. 创建一个匿名函数对象，同 def 类似，但不提供函数名
2. 语法：`lambda [参数1，参数2, ...] : 表达式`
3. 它只是一个表达式，用于创建函数对象
4. 先执行 `:` 后面的表达式，并返回表达式结果的引用
5. 只能包含一条表达式

### `eval()`：
1. 语法：`eval(source, global=None, local=None)`
2. 作用：把一个字符串当成一个表达式来执行，返回表达式执行后的结果
3. `source` 参数永远都是字符串，是表达式的字符串形式

### `exec()`：
1. 语法：`exec(source, global=None, local=None)`
2. 语法：把一个函数当成程序来执行

### 闭包
将内嵌函数的语句和执行环境打印在一起时，得到的对象称为闭包（`closure`），闭包必须满足的三个条件：
1. 必须有一个内嵌函数
2. 内嵌函数必须引用外部函数中的变量
3. 外部函数返回值必须是内嵌函数

## 模块

1. 是一个包含有一系列数据、函数、类等组成的程序组
2. 是一个文件，文件名通常以 `.py` 结尾

### 分类

1. 内置模块（`builtins`），在解析器的内部可以直接使用

2. 标准库模块，安装 `Python` 时已安装可以直接使用（一般以 `.py` 结尾）

3. 第三方模块（通常为开源），需要自己安装

4. 用户自己的模块（可以作为其他人的第三方模块）

### `import`

1. 语法：`import 模块名1 [as 别名1， 模块名2 [as 别名2]]`

2. 将某模块整体导入到当前模块

### `from import`

1. 语法：`from 模块名 import import 属性名1 [as 新属性名1][, 属性名2 [as 新属性名2]]...`

2. 将某模块的一个或多个属性导入到当前模块的作用域中

### 搜索模块的路径顺序

1. 搜索程序运行时的路径（当前路径）

2. `sys.path` 提供的路径

3. 搜索内置模块

### `sys.path`

1. 是一个存储模块搜索路径的列表

2. 可以把自定义的模块放在相应的路径下用以导入

3. 可以把自己的模块路径添加在 `sys.path` 列表中

### 模块的加载过程

1. 在模块导入时，模块的所有语句会执行

2. 如果一个模块已经导入，再次导入时不会重新执行模块内的语句

### 模块的重新加载

```python
import mymode
import imp

imp.reload(mymode)
```

### 模块的导入和执行过程

1. 先搜索相关的路径找模块（`.py`）

2. 判断是否有此模块对应的 `.pyc` 文件，如果存在 `.pyc` 文件且比 `.py` 文件新，则直接加载 `.pyc` 文件

3. 否则用 `.py` 文件生成 `.pyc` 文件后再进行加载

### 模块内预置的属性

1. `__doc__` ：绑定模块的文档字符串。模块内第一个没有赋值给任何变量的字符串为模块的文档字符串

2. `__file___` ：绑定模块对应的文档路径名。对于内建模块，没有该属性

3. `__name__` ：绑定模块的自身名称。当模块为主模块时，绑定 `__main__`

### `__all__` 列表

1. 用来存放可以导出属性的字符串列表

2. 当使用 `from import * ` 语句导入时，只导入 `__all__` 列表内的属性

3. 在模块中定义一个 `__all__` 变量，该变量是列表类型，存入的是变量名的字符串，就可以限制使用 `from import *` 时模块导入的变量

### 隐藏属性
以 `_` 开头的属性，在使用 `from import *` 时，不被导入

## 包

### 定义

将模块以文件夹的组织形式进行分组管理的办法

### 作用

将一系列模块进行分类管理，有利于防止命名冲突。可以在需要时加载一个或部分模块，而不是全部模块

### \_\_init\_\_.py

1. 常规包内**必须存在**的文件
2. 会在包加载时自动调用

#### 作用

1. 编写此包的内容
2. 在内部填写文档字符串
3. 在该文件中可以加载此包依赖的其他模块

### 导入

包的导入规则同模块的导入规则

### \_\_all\_\_ 列表

用来记录此包中有哪些子包或模块在用 `from 包 import *` 语句时是否被导入

> `__all__` 列表只对 `from import *` 语句起作用

### 相对导入

指包内模块的相对导入

语法：`from 相对路径包或模块 import 属性或模块名` 或者 `from 相对路径包或模块 import *`

#### 相对路径

```
.   代表当前路径
..  代表上一级目录
... 代表上两级目录
.... 以此类推
注意：相对导入时不能超出包的外部
```

### 加载路径

同模块的加载路径相同：

1. 当前文件夹

2. `sys.path` 给出的路径

## 异常

### 错误

由于逻辑或语法导致一个程序无法正常执行的问题

> 有些错误是未知的

### 定义

1. 程序出错时标识的一种状态
2. 当异常发生时，程序不会再向下执行，而转去调用该函数的地方，等待处理此错误并恢复到正常的状态

### 作用

1. 通知上层调用者有错误产生需要处理
2. 用作信号

### try-except

```python
try:
  可能触发异常的语句
except 错误类型1 [as 变量1]:
  异常处理语句1
except 错误类型2 [as 变量2]:
  异常处理语句2
except 错误类型3 [as 变量3]:
  异常处理语句3
...
except: # 可以捕获任何错误类型
  异常处理语句 other
else:
  未发生异常时执行的语句
finally:
  最终执行语句
```

> 最简单的形式可以没有 else、finally 语句

说明：

1. `as` 语句是用于绑定错误对象的变量，可以省略不写
2. `except` 子句可以有一个或多个，但至少要有一个
3. `else` 子句最多只能有一个，也可以省略不写
4. `finally` 子句最多只能有一个，也可以省略不写

### try-finally

```python
try:
  可能触发异常的语句
finally:
  最终语句
```

> finally 子句不可省略
>
> 一定不存在 except 子句
>
> 该语句不会改变程序的 正常/异常 状态

作用：通常用该语句来做触发异常时必须要处理的事情，无论异常是否发生，`finally` 子句都会被执行

### raise

触发一个错误，让程序进入异常状态

语法：

```python
raise 异常类型
或者
raise 异常对象
```

### assert

断言语句，当真值表达式为 `False` 时，用错误数据创建一个 `AssertionError` 类型的错误，并进入异常状态

```python
assert 真值表达式，错误数据（通常是字符串）
```

它的作用类似于：

```python
if 真值表达式 == False:
  raise AssertionError(错误数据)
```

### 使用异常机制的原因

在程序调用层数较深时，向主调函数传递错误信息需要用 `return` 语句层层传递比较麻烦，用异常机制处理简单

## 迭代器

用 `iter`（可迭代对象）函数返回的对象（实例），迭代器可以用 next(it) 函数获取可迭代对象的数据

### 迭代器函数

`iter(iterable)` 从可迭代对象中返回一个迭代器，`iterable` 必须是一个能提供迭代器的可迭代对象。

`next(iterator)` 从迭代器 `iterator` 中获取下一条记录，如果无法获取下一条记录，则触发 `StopIteration` 异常

### 说明

1. 迭代器是访问可迭代对象的一种方式
2. 迭代器只能向前取值，不能后退
3. 用 `iter` 函数可以返回一个可迭代对象的迭代器

### 用途

迭代器对象能使用 `next` 函数获取下一个元素

### 迭代工具函数

用于生成个性化的可迭代对象

#### zip 函数

`zip(iter1 [, iter2, iter3, ...])`

该函数返回一个 `zip` 对象，此对象用于生成一个元组，此元组的个数由最小的可迭代对象决定

```python
names = ['中国电信', '中国移动', '中国联通']
phones = [10000, 10086, 10010]

for n,p in zip(names, phones):
  print(n, '的客服电话是：', p)

# 以下是打印结果
# 中国电信 的客服电话是： 10000
# 中国移动 的客服电话是： 10086
# 中国联通 的客服电话是： 10010
```

#### enumerate 函数

`enumerate(iterable [, start])`

生成带索引的枚举对象，返回迭代类型为：索引-值对（`index, value`）默认索引从 0 开始，也可以使用 `start` 绑定

```python
names = ['中国电信', '中国移动', '中国联通']

for n in enumerate(names):
  print(n)

# 以下是打印结果
# (0, '中国电信')
# (1, '中国移动')
# (2, '中国联通')
```

### 高级
可以通过 `next(it)` 函数取值的对象就是迭代器

#### 迭代器协议
指对象能够使用 `next` 函数获取下一项数据，在没有下一项数据时触发一个 `StopIteration` 来终止迭代的约定

#### 实现方式
类里面需要有 `__next__(self)` 方法来实现迭代器协议

#### 语法

```python
class MyIterator():
	def __next__(self):
		迭代器协议的实现
		return 数据
```

## 生成器

能够动态提供数据的对象，生成器对象也是可迭代对象（实例）

### 生成器函数

含有 `yield` 语句的函数是生成器函数，此函数被调用时将返回一个生成器对象

```python
yield 表达式
```

#### 说明

1. `yield` 用于 `def` 函数中，目的是将此函数作为生成器函数使用
2. `yield` 用来生成数据，供迭代器 `next(it)` 函数使用
3. 生成器函数的调用将返回一个生成器对象，生成器对象是一个可迭代对象
4. 在生成器函数调用 `return` 时会生出一个 `StopIteration` 异常来通知 `next(it)` 函数不能在提供数据

## 文件

### 定义

1. 文件是存储数据的单位
2. 文件通常用来长期存储数据
3. 文件中的数据是以**字节**为单位**顺序存储**的

### 操作流程

#### 打开文件

`open(filepath, mode='rt')`

打开一个文件，返回此文件对应的文件流对象，如果打开失败，则会触发 `OSError` 错误

**mode 说明**

| 字符 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| 'r'  | 以只读方式打开（默认）                                       |
| 'w'  | 以只写方式打开，删除原有文件内容（如果文件不存在，则创建改文件并以只写方式打开） |
| 'x'  | 创建一个新文件，并以写模式打开这个文件，如果文件存在则会产生 FileExistsError 错误 |
| 'a'  | 以只写方式打开一个文件，如果有原文件则追加到文件末尾         |
| 'b'  | 用二进制模式打开                                             |
| 't'  | 文本文件模式打开（默认）                                     |
| '+'  | 为更新内容打开一个磁盘文件（可读可写）                       |

> 1. 缺省模式是 'rt'
> 2. 'w+b' 可以实现二进制随机读写，当打开文件时，文件内容将被清零
> 3. 'r+b' 以二进制读和更新模式打开文件，打开文件时不会清空文件内容
> 4. 'r+' 以文本模式读和更新模式打开文件，打开文件时不会清空文件内容

#### 读写文件

`python` 文件读写的类型有两种：

1. 文本文件（`text file`）
2. 二进制文件（`binary file`）

##### 文本文件的操作

默认文件中存储的都是字符数据，以行为单位进行分割，在 `python` 内部统一用 `\n` 作为换行符进行分隔

##### 各种操作系统的换行符

1. `Linux` 换行符：`\n`
2. `Windows` 换行符：`\r\n`
3. 旧的 `Macintosh` 换行符：`\r`
4. 新的 `Mac OS` 换行符：`\n`

#### 关闭文件

`File.close()`

关闭文件，释放系统资源

### 标准输入输出文件

`sys.stdin` ：默认为标准键盘输入设备

`sys.stdout` ：默认为屏幕终端

`sys.stderr` ：默认为屏幕终端

标准输入输出文件不需要打开和关闭就可以使用

### 汉字编码

#### 国标系列

`GB18030` ：二字节或四字节编码（最迟的，2005年，2 万 7 千多个汉字）

`GBK`         ：二字节编码（次早的，1995年，2 万 1 千多个汉字）

`GB2312`   ：二字节编码（最早的，1980年，6000 多个汉字）

> windows 常用

#### 国际标准

`Unicode`    <--->   `UTF-8`

> Linux、Mac OS X、IOS、Android 常用

#### python 编码字符串

`gb2312` 、`gbk` 、`gb18030` 、`utf-8`、`ascii` ……

### 编码注释

在源文件的第一行或第二行写下如下内容为编码注释：

`# -*- coding:utf-8 -\*-`


## 类

拥有相同属性和行为的对象分为一组，即为一个类。类是用来描述对象的工具，用类可以创建同类对象。

### 创建

```python
class 类名(继承列表):
  '''类的文档字符串'''
  实例方法定义（类内的行数称为方法 method）
  类变量定义
  类方法定义
  静态方法定义
```

> 类如果没有继承可以不写继承列表

### 构造函数

创建这个类的实例对象，并返回此实例对象的引用关系。

### 实例（对象）说明

1. 实例有自己的作用域和命名空间，可以为该实例添加实例变量（属性）
2. 实例可以调用类方法和实例方法
3. 实例可以访问类变量和实例变量

### 实例方法

```python
class 类名(继承列表):
  def 实例方法名(self, 参数1, 参数2, ...):
    '''实例方法的文档字符串'''
    语句块
```

#### 说明

1. 实例方法实质是函数，是定义在类内的函数
2. 实例方法至少有一个形参，第一个形参代表调用这个方法的实例，一般命名为：`self`

#### 调用语法

`实例.实例方法名(调用传参)` 或者

`类名.实例方法名(实例, 调用传参)`

### 属性（实例变量）

每个实例都可以有自己的变量，此变量称为实例变量（也叫属性）

#### 赋值规则

1. 首次为属性赋值则创建此属性
2. 再次为属性赋值则改变属性的绑定关系

#### 作用

用来记录对象自身的数据

#### 删除属性

`del 对象.实例变量名`

使用 `del` 语句可以删除一个对象的实例变量

### 初始化方法

对新创建的对象添加实例变量（属性）或相应的资源

```python
class 类名(继承列表):
  def __init__(self [, 形参列表]):
    语句块
```

> 1. 初始化方法必须为 `__init__ `，不可改变
> 2. 初始化方法会在构造函数创建实例后自动调用，且此实例自身通过第一个参数 `self` 传入 `__init__` 方法中
> 3. 构造函数的实参将通过 `__init__` 方法的形参列表传入 `__init__` 方法中
> 4. 初始化方法内部如果需要返回则只能返回 None

### 析构方法

```python
class 类名(继承列表):
  def __del__(self):
    语句块
```

1. 析构方法不需要手动调用，在对象销毁时自动调用
2. 用于清理此对象所占用的资源

> 不建议在析构方法内做任何事情，因为对象销毁的时间难以确定

### 预置实例属性

#### \_\_dict\_\_ 属性

此属性绑定一个存储此实例自身变量的字典，也就是说，实例的该属性里面，存放的是属于该实例的所有属性的字典

#### \_\_class\_\_ 属性

用于绑定创建此实例的类，可以借助此属性来访问创建此实例的类

### 属性管理函数

`getattr(obj, name[, default])` ：

1. 从一个对象得到对象的属性；`getattr(x, 'y')` 等同于 `x.y`

2. 当对象的属性不存在时，如果给出 `default` 参数，则返回 `default`；如果没有给出 `default` 参数，则产生一个 `AttributeError` 错误

`hasattr(obj, name)` ：

1. 用给定的 `name` 返回对象 `obj` 是否有此属性
2. 这种做法可以避免在 `getattr(obj, name)` 时引发错误

`setattr(obj, name, value)` ：

1. 给对象 `obj` 的名为 `name` 的属性设置相应的值 `value`；`setattr(x, 'y', v)` 相当于 `x.y = v`

`delattr(obj, name)` ：

1. 删除对象 `obj` 中的 `name` 属性，`delattr(x, 'y')` 等同于 `del x.y`

### 类变量

类变量是类的属性，此属性属于类，

#### 作用

用来记录类相关的数据

#### 说明

1. 类变量可以通过类直接访问
2. 类变量可以通过类的实例直接访问
3. 类变量可以通过此类实例的 `__class__` 属性间接访问

### 文档字符串

类内第一个没有赋值给任何变量的字符串是类的文档字符串

类的文档字符串可以使用 `help()` 函数查看

### \_\_slots\_\_ 列表

限定一个类的实例只能有固定的属性（实例变量），通常为防止错写属性名而发生运行时错误

```python
class Student:
  __slots__ = ['name', 'score']
  def __init__(self, name, score):
    self.name = name
    self.score = score

stu1 = Student('zhangsan', '90')
stu1.socre = 98  # 编译时会报错
```

> 含有 `__slots__` 列表的类创建的实例对象没有 `__dict__` 属性，即此类实例的变量不用字典来保存对象的属性（实例变量）

### 类方法

`@classmethod`

类方法是描述类的行为的方法，类方法属于类

> 1. 类方法需要使用 `@classmethod` 装饰器定义
> 2. 类方法至少有一个形参，第一个形参用于绑定类，约定写为 `cls`
> 3. 类和该类的实例都可以调用类方法
> 4. 类方法不能访问此类创建的实例的属性，只能访问类变量

### 静态方法

`@staticmethod`

静态方法不属于类，也不属于类的实例，它相当于定义在类内的普通函数，只是它的作用域属于类

### 继承 / 派生

#### 定义

1. 继承是指从已有的类衍生出新类，新类具有原类的行为，并能扩展新的行为
2. 派生就是从一个已有类中衍生（创建）新类，在新类上可以添加新的属性和行为

#### 目的

1. 继承是延续旧类的功能
2. 派生是为了在旧类的基础上添加新的功能

#### 名词

基类：`base class`

超类：`super class`

父类：`father class`

派生类：`derived class`

子类：`child class`

#### 作用

1. 用继承派生机制，可以将一些共有功能加载基类中，实现代码的共享
2. 在不改变基类的基础上改变原有功能

```python
class 类名(基类名):
  语句块

# 单继承是指派生类有一个基类衍生出来的类
```

#### 说明

1. 任何类都直接或间接的继承自 `object` 类

2. `object` 类是一切类的超类（祖类）

3. 子类如果重写了 `__init__` 方法，父类的初始化方法就不会再被调用了，如果还想调用，这样写：

   ```python
   class MyList(list):
     def __init__(self, *args):
       self.__init__(*args) # 保证父类的初始化方法被正确的调用
       # 下面就可以写子类自己初始化方法中的一些操作了
   ```

### 覆盖

在有继承关系的类中，子类实现了与基类同名的方法，在子类实例调用该方法时，实例调用的是子类中覆盖版本的方法，这种现象叫做覆盖

#### 调用父类的方法

`super(type, obj)` 返回绑定超类的实例

### 常用函数

#### `issubclass(cls, clas_or_tuple)`

判断一个类是否继承自其他的类，如果此 `cls` 是 `class` 或 `tuple` 中的一个派生子类则返回 `True`，否则返回 `False`

#### 查看 python 中内建类的继承关系

`help(_builtins__)`

### 封装

封装指隐藏类的实现细节，让使用者不用关心这些细节；

封装的目的是让这些使用者尽可能少的进行实例变量（属性）的操作

### 私有属性

`python` 类中，以双下划线 `__` 开头，不以双下划线结尾的标识符为私有成员，在类的外部无法直接访问

#### 扩展

1. `_xxx` ：不能用于 `from import *`；表示的是 `protected` 类型的变量，即该变量只能本身与子类访问
2. `__xxx` ：表示私有类型的变量或方法，只能允许这个类本身访问，连子类也不可以
3. `__xxx__` ：系统的特殊方法，不建议使用这样的命名方式

### 多态

只在继承、派生关系的类中，调用基类对象的方法，实际能调用子类的覆盖版本方法的现象叫多态

#### 说明

1. 多态调用的方法与对象相关，不与类型相关
2. `python` 的全部对象都只有”运行时状态（动态）“，没有 `C++/Java` 里的编译时状态（静态）

### 多继承

指一个子类继承自两个或两个以上的基类

```python
class 类名(基类名1, 基类名2, ...):
  语句块
```

#### 说明

1. 一个子类同时继承自多个父类，父类中的方法可以被同时继承下来
2. 如果两个父类中有同名的方法，而在子类中有没有覆盖此方法时，调用结果难以确定

> 使用多继承可能会出现标识符（名字空间冲突）的问题，要谨慎使用；
>
> 一般来说，继承列表中先写哪个类，先使用哪个类的方法

### 继承的 MRO（Method Resolution Order）问题

类里面用 `__mro__` 属性来记录继承方法的查找顺序

> 在多继承里面，super() 的调用，不是按照继承关系调用的，而是按照 `__mro__` 里面的顺序调用的

### 重写

在自定义的类内添加相应的方法，让自定义的类生成的对象（实例）像内建对象一样进行内建的函数操作

#### 对象转字符串函数重写

`repr(obj)` ：返回一个能代表此对象的**表达式**字符串，通常：`eval(repr(obj)) == obj`

```python
def __repr__(self):
  return 能够表达 self 内容的字符串
```

`str(obj) ` ：使给定的对象返回一个字符串（这个字符串通常是给人看的）

```python
def __str__(self):
  return 人能看懂的字符串
```

> 1. str(obj) 函数有限调用 `obj.__str__()` 方法返回字符串
> 2. 如果 obj 没有 `__str__()` 方法，则调用 `obj.__repr__()` 方法返回的字符串
> 3. 如果 obj 没有 `__repr__()` 方法，则调用 object 类的 `__repr__()` 实例方法显示 `<xxxx>` 格式的字符串

## with 语句

```python
with 表达式1 [as 变量1], 表达式2 [as 变量2]:
  语句块
```

### 作用

使用与对资源进行访问的场合，确保使用过程中不管是否发生异常，都会执行必须的清理操作，并释放资源

适用的场景：

1. 文件使用后自动关闭
2. 线程中锁的自动获取和释放

> 能够用 with 语句管理的对象必须是环境管理器

## 环境管理器

1. 类里面有 `__enter__` 和 `__exit__` 实例方法的类被称为环境管理器
2. 能够用 `with` 语句管理的对象必须是环境管理器
3. `__enter__` 方法将在进入 `with` 语句时被调用，并返回有 `as` 变量管理的对象
4. `__exit__` 将在离开 `with` 语句时被调用，且可以用参数来判断在离开 `with` 语句时是否有异常发生并作出相应的处理

```python
class A:
  def __enter__(self):
    print('已经进入 with 语句')
    return self # 返回的对象将有 as 绑定

  def __exit__(self, exc_type, exc_val, exc_tb):
    '''
    exc_type：在没有异常时为 None，在出现异常时为异常类型
    exc_val：在没有异常时为 None，在出现异常时绑定错误对象
    exc_tb：在没有异常时为 None，在出现异常时绑定 traceback 对象
    '''
    print('已经离开 with 语句')
```
## 小细节

### 空格的使用

1. 各种右括号前不用加空格
2. 逗号、冒号、分号前不要加空格
3. 函数的左括号前不要加空格
4. 序列的左括号前不要加空格
5. 操作符左右各加一个空格，不要为了对齐增加空格
6. 函数默认参数使用的赋值符左右省略空格
7. 不要讲多余语句写在同一行，尽管使用 ; 允许
8. `if/for/while` 语句中，即使执行语句只有一句，也必须另起一行