# student_list=[{'id':1,'name':'小明','age':18}]
import json
#数据文件路径
STUDENT_FILE="students.json"
def load_students():
    """从文件加载学生数据"""
    try:
        with open(STUDENT_FILE,'r',encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        return []


def save_students(students):
    """保存学生数据到文件"""
    with open(STUDENT_FILE,'w',encoding='utf-8') as f:
        json.dump(students,f,ensure_ascii=False,indent=4)

student_list=load_students()

def add():           #添加学生信息
    print("\n====  添加学生信息  ====")
    ex=input("退出请按n/N，继续请按任意键：")
    if ex=="n" or ex=="N":
        return
    while True:
        stu_id=input("学号:").strip()   #输入学生信息
        name=input("姓名:").strip()
        age=input("年龄:").strip()
        if stu_id=="n" or stu_id=="N":
            break
        if name=="n" or name=="N":
            break
        if age=="n" or age=="N":
            break
        is_duplicate=False
        for stu in student_list:
            if int(stu['id'])==int(stu_id):
                print("id重复，请换一个id")
                is_duplicate=True
                break
        if not is_duplicate:
            student_list.append({'id':int(stu_id),'name':name,'age':int(age)})
            save_students(student_list)
            print("添加成功！")
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
                save_students(student_list)
                print(f"学号为{stu_id}的学生已被删除")
            else:
                return
            return
    print("你要删除的学生不存在！")

def modify():        #修改学生信息
    stu_id=int(input("请输入想修改的学生的学号："))
    for stu in student_list:
        if stu['id'] == stu_id:
            print("\n=====   学生信息   =====")
            print("学号  姓名  年龄")
            print(stu['id'], stu['name'], stu['age'], sep="   ")
            confirm=input(f"你确定修改{stu['name']}同学的信息吗？(Y/N)")
            if confirm=="Y" or "y":
                stu['id']=int(input("请输入学号："))
                stu['name']=input("请输入姓名：")
                stu['age']=int(input('请输入年龄；'))
                save_students(student_list)
                return
    print("你查找的学生不存在！")

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