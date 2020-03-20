from menu import print_info
from student_info import *

def main():
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
        elif s == '7':
            save_info(l)
        elif s == '8':
            read_info(l)
        elif s == 'q':
            print('感谢使用本系统，再见！')
            break
        else:
            print('操作选择错误，请重新输入！')
            continue

if __name__ == '__main__':
    main()