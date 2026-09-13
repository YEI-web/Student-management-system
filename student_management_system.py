def add():
    print("添加学生信息")
def delete():
    print("删除学生信息")
def modify():
    print("修改学生信息")
def query():
    print("查询学生信息")
def show():
    print("显示学生信息")


def main():
    while True:
        print('''
                =====学生管理系统=====
                1. 添加学生信息
                2. 删除学生信息
                3. 修改学生信息
                4. 查询学生信息
                5. 显示所有学生
                0. 退出操作系统
                ''')

        option=int(input("请输入你选择的操作："))
        if option==1:
            add()
        elif option==2:
            delete()
        elif option==3:
            modify()
        elif option==4:
            query()
        elif option==5:
            show()
        elif option==0:
            break
        else:
            print("输入错误，请重新输入")



if __name__=='__main__':
    main()