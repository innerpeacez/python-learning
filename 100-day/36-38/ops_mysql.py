import pymysql
from pymysql.cursors import DictCursor


def add_department():
    no = int(input('编号：'))
    name = str(input('名字：'))
    address = str(input('所在地：'))

    conn = pymysql.connect(host='192.168.10.76', port=30859, database='hrs', charset='utf8', user='root',
                           password='GetL6Etqhe')

    try:
        with conn.cursor() as cursor:
            result = cursor.execute('insert into tb_dept values (%s, %s, %s)', (no, name, address))
            if result == 1:
                print('添加成功')
            conn.commit()
    finally:
        conn.close()


def delete_department():
    no = int(input('编号: '))
    con = pymysql.connect(host='192.168.10.76', port=30859, database='hrs', charset='utf8', user='root',
                          password='GetL6Etqhe', autocommit=True)
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'delete from tb_dept where dno=%s',
                (no,)
            )
        if result == 1:
            print('删除成功!')
    finally:
        con.close()


def update_department():
    no = int(input('编号: '))
    name = input('名字: ')
    loc = input('所在地: ')
    con = pymysql.connect(host='192.168.10.76', port=30859, database='hrs', charset='utf8', user='root',
                          password='GetL6Etqhe', autocommit=True)
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'update tb_dept set dname=%s, dloc=%s where dno=%s',
                (name, loc, no)
            )
        if result == 1:
            print('更新成功!')
    finally:
        con.close()


def list_department():
    con = pymysql.connect(host='192.168.10.76', port=30859, database='hrs', charset='utf8', user='root',
                          password='GetL6Etqhe')
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])
    finally:
        con.close()


def employees():
    page = int(input('页码: '))
    size = int(input('大小: '))
    con = pymysql.connect(host='192.168.10.76', port=30859, database='hrs', charset='utf8', user='root',
                          password='GetL6Etqhe')
    try:
        with con.cursor() as cursor:
            cursor.execute(
                'select eno as no, ename as name, job, sal from tb_emp limit %s,%s',
                ((page - 1) * size, size)
            )
            for emp_tuple in cursor.fetchall():
                emp = Emp(*emp_tuple)
                print(emp)
    finally:
        con.close()


class Emp(object):

    def __init__(self, no, name, job, sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'


def main():
    # add_department()
    # delete_department()
    # update_department()
    list_department()
    print('-----------------------')
    employees()
    pass


if __name__ == '__main__':
    main()
