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

if __name__=='__main__':
    main()