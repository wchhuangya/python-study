# 局部变量
## 案例一
```phtyon
L = [1, 2, 3]
def f1():
    L = L + [4, 5, 6]

f1() # 报错

def f2():
    L += [4, 5, 6]

f2() # 正确
```
> 原因：
> 1. f1() 方法中是赋值操作，在赋值操作之前，需要确定 L 到底是全局变量还是局部变量，系统会把 L 当成局部变量；但是作为局部变量的 L 在操作之前还没有被赋值，因此报错
> 2. f2() 方法中是 += 操作，实质上是调用 L 对象的 `__iadd__()` 方法，这时，就不存在 L 是局部变量的问题了


_f1() 方法修改如下就好了_

```python
L = [1, 2, 3]
def f1():
    global L
    L = L + [4, 5, 6]
f1()
```