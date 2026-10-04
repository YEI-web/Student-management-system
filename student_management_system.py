student_list=[{'id':1,'name':'小明','age':18}]


def add():           #添加学生信息
    print("\n====  添加学生信息  ====")
    ex=input("退出请按n/N，继续请按任意键：")
    if ex=="n" or ex=="N":
        return
    while True:
        id=input("学号:").strip()   #输入学生信息
        name=input("姓名:").strip()
        age=input("年龄:").strip()
        if id=="n" or id=="N":
            break
        if name=="n" or name=="N":
            break
        if age=="n" or age=="N":
            break
        for stu_id in student_list:
            if int(stu_id['id'])==int(id):
                print("id重复，请换一个id")
            else:
                student_list.append({'id':int(id),'name':name,'age':int(age)})
                return
def delete():        #删除学生信息
    stu_id = int(input("输入需要删除学生的学号："))
    for stu in student_list:
        if stu['id'] == stu_id:
            print("\n=====   学生信息   =====")
            print("学号  姓名  年龄")
            print(stu['id'], stu['name'], stu['age'], sep="   ")
            confirm=input("是否删除该学生(Y/N)").strip()
            if confirm=="Y" or "y":
                student_list.remove(stu)
                print(f"学号为{stu_id}的学生已被删除")
            else:
                return
            return
    print("你要删除的学生不存在！")
def modify():
    print("修改学生信息")
def query():         #查询学生信息
    stu_id=int(input("输入查询学生的学号："))
    for stu in student_list:
        if stu['id'] == stu_id:
            print("\n=====   学生信息   =====")
            print("学号  姓名  年龄")
            print(stu['id'], stu['name'], stu['age'], sep="   ")
            return
    print("你查找的学生不存在！")
def show():          #显示所有学生
    print("\n=====   学生信息   =====")
    print("学号  姓名  年龄")
    for stu in student_list:
        print(stu['id'],stu['name'],stu['age'],sep= "   ")


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