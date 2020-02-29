#! /usr/bin/env python3
# -^- coding:  utf-8 -^-
# @Time:  2020/2/29 11:45
# @Author:  yang


def haveornot(no, path, number):
    """
    no在文件路径为path的文件中有没有出现过
    :param no: 要对应的值
    :param path: 文件路径
    :param number: 在文本每行中的第几个数（列数）
    :return: 有：True，无：False
    """
    with open(path, "r") as f:
        content_line = f.readline()
        while content_line:
            list_line = content_line.split()
            if no == list_line[number]:
                return True
            content_line = f.readline()
    return False


def display_menu():  # 主菜单
    print("-----Choose the Function-----")
    print("1. Query")
    print("2. Maintenance")
    print("#. Exit System")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def display_query_menu():  # 查询子菜单
    print("-----Choose the Function-----")
    print("1. Projects in Beijing")
    print("2. Red Parts Prepared for Projects in Beijing")
    print("#. Return")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def display_maintenance_menu():  # 维护子菜单
    print("-----Choose the Function-----")
    print("1. Add")
    print("2. Delete")
    print("#. Return")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def display_addordelete(num):  # 修改的是哪个表
    if num == 1:
        print("-----Choose the file(Add)-----")
    else:
        print("-----Choose the file(Delete)-----")
    print("1. Supplier")
    print("2. Project")
    print("3. Part")
    print("#. Return")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def query1():
    """
    查询北京的所有工程的工程名称 工程号
    列表re中有一堆元组，每个元组记录着北京工程的工程名称和工程号
    :return:/
    """
    re = []
    with open(r"./Data/project.txt", "r") as f:
        pro_line = f.readline()
        while pro_line:
            pro_list = pro_line.split()
            need = pro_list[2]
            if need == "Beijing":
                tuple_beijing = {pro_list[0], pro_list[1]}
                re.append(tuple_beijing)
            pro_line = f.readline()
    for i in re:
        print(i)


def query2():
    """
    供应红色零件给北京工程的供应商的供应商名，供应商号，供应商所在城市
    :return:
    """
    with open(r"./Data/part.txt", "r") as fl:  # Data文件 一行行寻找红色零件
        part_line = fl.readline()
        while part_line:
            part_list = part_line.split(' ')
            color = part_list[2]
            if color == "red":  # 一旦找到红色零件 便记录下该零件运送给什么工程（工程号jno）
                jno = part_list[3]
                with open(r"./Data/project.txt", "r") as fpro:  # 工程文件中寻找 是北京的且工程号和零件运送的工程相匹配的
                    pro_line = fpro.readline()
                    while pro_line:
                        pro_list = pro_line.split()
                        if (pro_list[2] == "Beijing") & (pro_list[1] + '\n' == jno):  # 如果匹配 记录下该工程的供应商号
                            sno = pro_list[3]
                            with open(r"./Data/supplier.txt", "r")as fsup:  # 找到该供应商 打印结果
                                sup_line = fsup.readline()
                                while sup_line:
                                    sup_list = sup_line.split()
                                    if sup_list[1] == sno:
                                        print(sup_line)
                                    sup_line = fsup.readline()
                        pro_line = fpro.readline()
            part_line = fl.readline()


def query():
    while True:
        display_query_menu()
        query_choose = input()
        if query_choose == '1':
            query1()
        elif query_choose == '2':
            query2()
        elif query_choose == '#':
            break
        else:
            print("Plz Input Again.")


def add_supplier():
    global sno
    print("supplier name:")
    sname = input()

    flag = True  # 看supplier no输入的是否合理，有没有和以前的值重复
    while flag:
        print("supplier no:")
        sno = input()
        flag = haveornot(sno, "./Data/supplier.txt", 1)
        if flag:
            print("Invalid supplier no,plz input again.")

    print("supplier city:")
    city = input()
    with open(r"./Data/supplier.txt", "a") as f:
        string = '\n' + sname + " " + sno + " " + city
        f.write(string)


def add_project():
    global jno, sno
    print("project name:")
    jname = input()

    flag = True  # 看工程号是否合理，有没有和之前的工程号重复
    while flag:
        print("project no:")
        jno = input()
        flag = haveornot(jno, "./Data/project.txt", 1)
        if flag:
            print("Invalid project no,plz input again.")

    print("project city:")
    city = input()

    flag = False  # 看供应商是否存在 供应商不存在的情况不能发生噢
    while not flag:
        print("supplier no:")
        sno = input()
        flag = haveornot(sno, "./Data/supplier.txt", 1)
        if not flag:
            print("Invalid supplier no,plz input again.")
    flag = haveornot(sno, "./Data/part.txt", 3)  # 该供应商手里有零件不 没零件不能供应工程
    if not flag:
        print("This supplier cannot provide enough part")
    else:
        with open(r"./Data/project.txt", "a") as f:
            string = "\n" + jname + " " + jno + " " + city + " " + sno
            f.write(string)


def add_part():
    global pno, sno
    print("part name: ")
    pname = input()

    flag = True  # 看零件号是否与之前的零件重复
    while flag:
        print("part no:")
        pno = input()
        flag = haveornot(pno, "./Data/part.txt", 1)
        if flag:
            print("Invalid part no,plz input again.")

    print("part color:")
    city = input()

    flag = False  # 看零件供应的工程商是否存在 不存在就重输供应商号
    while not flag:
        print("project no:")
        sno = input()
        flag = haveornot(jno, "./Data/supplier.txt", 1)
        if not flag:
            print("Invalid supplier no,plz input again.")

    with open(r"./Data/part.txt", "a") as f:
        string = '\n' + pname + " " + pno + " " + city + " " + sno
        f.write(string)


def delete_supplier():
    print("supplier no:")  # 根据供应商号 确定删哪个
    sno = input()
    flag = haveornot(sno, "./Data/supplier.txt",1)
    if not flag:  # 如果该供应商不存在
        print("(does not exist)Invalid supplier no.")
    else:  # 若存在
        flag1 = haveornot(sno, "./Data/project.txt", 3)  # 若该供应商手里有零件 并且还在支持工程 就不能删
        flag2 = haveornot(sno, "./Data/part.txt", 3)
        if flag1 or flag2:
            print("(dependency)Invalid supplier no.")
        else:  # 否则删除
            with open(r"./Data/temp.txt", "w") as f:
                with open(r"./Data/supplier.txt", "r") as fsup:
                    sup_line = fsup.readline()
                    while sup_line:
                        sup_list = sup_line.split()
                        if sup_list[1] == sno:
                            pass
                        else:
                            f.write(sup_line)
                        sup_line = fsup.readline()
            with open(r"./Data/temp.txt", "r") as f:
                content = f.readlines()
            with open(r"./Data/supplier.txt", "w") as fsup:
                fsup.writelines(content)


def delete_project():
    print("project no:")  # 根据工程号删除工程
    jno = input()
    flag = haveornot(jno, "./Data/project.txt",1)  # 工程号存在吗？
    if not flag:  # 不存在
        print("(does not exist)Invalid project no.")
    else:  # 存在
        with open(r"./Data/temp.txt","w") as f:
            with open(r"./Data/project.txt","r") as fpro:
                pro_line = fpro.readline()
                while pro_line:
                    pro_list = pro_line.split()
                    if pro_list[1] == jno:
                        pass
                    else:
                        f.write(pro_line)
                    pro_line = fpro.readline()
        with open(r"./Data/temp.txt", "r") as f:
            content = f.readlines()
        with open(r"./Data/project.txt","w") as fpro:
            fpro.writelines(content)


def delete_part():
    global sno
    print("part no:")  # 根据零件号删除
    pno = input()

    flag = haveornot(pno, "./Data/part.txt", 1)  # 零件号存在吗
    if not flag:  # 不存在
        print("(does not exist)Invalid part no.")
    else:  # 存在
        with open(r"./Data/part.txt") as f:  # 求零件号对应的供应商号
            part_line = f.readline()
            while part_line:
                part_list = part_line.split()
                if part_list[1] == pno:
                    sno = part_list[3]  # 得到供应商号
                    break
                part_line = f.readline()
        flag = haveornot(sno, "./Data/project.txt", 3)  # 该供应商号在搞工程吗
        if flag:  # 在搞工程 不能删
            print("(dependency)Invalid part no.")
        else:  # 没弄工程 可删
            with open(r"./Data/temp.txt", "w") as f:
                with open(r"./Data/part.txt", "r") as fpart:
                    part_line = fpart.readline()
                    while part_line:
                        part_list = part_line.split()
                        if part_list[1] == pno:
                            pass
                        else:
                            f.write(part_line)
                        part_line = fpart.readline()
            with open(r"./Data/temp.txt", "r") as f:
                content = f.readlines()
            with open(r"./Data/part.txt", "w") as fpart:
                fpart.writelines(content)


def maint1():  # 维护添加
    while True:
        display_addordelete(1)
        choose = input()
        if choose == '1':
            add_supplier()  # 写了
        elif choose == '2':
            add_project()  # 写了
        elif choose == '3':
            add_part()  # 写了
        elif choose == '#':
            break
        else:
            print("Plz Input Again.")


def maint2():  # 维护删除
    while True:
        display_addordelete(0)
        choose = input()
        if choose == '1':
            delete_supplier()  # 写了
        elif choose == '2':
            delete_project()  # 写了
        elif choose == '3':
            delete_part()  # 写了
        elif choose == '#':
            break
        else:
            print("Plz Input Again.")


def maintenance():
    while True:
        display_maintenance_menu()
        maintenance_choose = input()
        if maintenance_choose == '1':
            maint1()
        elif maintenance_choose == '2':
            maint2()
        elif maintenance_choose == '#':
            break
        else:
            print("Plz Input Again.")


if __name__ == '__main__':
    while True:
        display_menu()
        op = input()
        if op == '1':  # 查询
            query()
        elif op == '2':  # 维护
            maintenance()
        elif op == '#':  # 退出
            break
        else:
            print("Plz Input Again.")
    print("Exit Successfully!")
