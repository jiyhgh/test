"""
*_* coding: utf-8 *_*
author:ymy
time:2023/2/22 16:46
file :学生管理手册.py
"""
def menu():
    print("------菜单选项------")
    print("1.添加功能")
    print("2.删除功能")
    print("3.查询功能")
    print("4.展示功能")
    print('5.修改功能')
    print("------------------")
# menu()
list1 = []
def add():
    print("欢迎进入学生信息添加页面")
    name = input("请输入你的名字")
    age = int(input('请输入你的年龄'))
    gender = input('请输入你的性别')
    # print("添加成功")
    for i in list1:
        if i['name'] == name and i['age'] == age and i['gender'] == gender:
            print('学生信息已存在，请重新输入')
            return
    dict1 = {}
    dict1['name'] = name
    dict1['age'] = age
    dict1['gender'] = gender
    print("添加成功")
    list1.append(dict1)
    print(list1)
def delete():
    num = int(input('请输入你要删除的序号'))
    if 0 <= num <= len(list1) - 1:
        delete_num = input('你确定要删除？（yes/no）')
        if delete_num == 'yes' or delete_num == 'y':
            # 列表删除：del 列表[下标]
            del list1[num]
            print('删除成功')
        else:
            print('请输入正确的序号')
    # if name:
    #     d_name = input("你确定要删除吗？(y/n)")
    #     if d_name == 'y' or d_name == 'n':
    #         if 0 <= len(d_name) <= 1:
    #             print('删除成功')
    #         else:
    #             print('请重新输入！！！')
        # if d_name == 'y':
        #     if d_name == 'n':
        #             print('ok')
        #     print('删除成功')
        # else:
        #     print('确定不删除')
def find():
    print("-------欢迎进入查询学生页面-------")
    name = input("请输入你想查询的名字")
    for i in list1:
        if i["name"] == name:
            print(i)
        else:
            print("请确认你输入的是否正确")
def show():
    for i, j in enumerate(list1):
        print('序号%d 姓名%s  年龄%d  性别%s' % (i, j['name'], j['age'], j['gender']))
def update():
    print("-------欢迎进入修改学生信息页面-------")
    show()
    update_num = int(input("请输入你要修改的学生信息序号："))
    if 0 <= update_num <= len(list1) - 1:
        list1[update_num]['name'] = input("请输入修改后的学生姓名：")
        list1[update_num]['age'] = int(input("请输入修改后的学生年龄："))
        list1[update_num]['gender'] = input("请输入修改后的学生性别：")
        print("学生信息修改成功")
        print(list1[update_num])
    else:
        print("该学生序号不存在")
def main():
    while True:
        menu()
        num = int(input('请输入你需要的功能：'))
        if num == 1:
            add()
        elif num == 2:
            delete()
        elif num == 3:
            find()
        elif num == 4:
            show()
        elif num == 5:
            update()
        else:
            print("你输入的序号错误！！！")
if __name__ == '__main__':
    main()
