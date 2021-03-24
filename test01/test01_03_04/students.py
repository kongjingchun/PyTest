# coding:utf-8
# @Create time: 2021/2/25 4:51 下午
# @Author: KongJingchun
# @remark:实现学生信息库

students = {
    1: {
        'name': '孔敬淳',
        'age': 30,
        'sex': "boy",
        'class_name': '测试'
    },
    2: {
        'name': '王  野',
        'age': 25,
        'sex': 'boy',
        'class_name': "测试"
    },
    3: {
        'name': '卢晓倩',
        'age': 18,
        'sex': 'girl',
        'class_name': '测试'
    },
    4: {
        'name': '焦宇威',
        'age': 29,
        'sex': 'boy',
        'class_name': '开发'
    },
    5: {
        'name': '刘  丹',
        'age': 20,
        'sex': 'girl',
        'class_name': '开发'
    }
}


def check(**kwargs):
    if 'name' not in kwargs:
        return '请输入正确的姓名'
    if 'age' not in kwargs:
        return '请输入正确的年龄'
    if 'sex' not in kwargs:
        return '请输入正确的性别'
    if 'class_name' not in kwargs:
        return '请输入正确的工作'
    return True


def get_all_stasuts():
    for key, value in students.items():
        print(
            '学号：{}、姓名：{}、年龄：{}、性别：{}、工作：{}'.format(key, value['name'], value['age'], value['sex'], value['class_name']))


def del_studen(id):
    if id in students:
        user = students.pop(id)
        print('已删除学号为{}的学生，姓名：{}、年龄：{}、性别：{}、工作：{}'.format(id, user["name"], user["age"], user["sex"],
                                                           user["class_name"]))
    else:
        print('不存在该学生')


def add_student(**kwargs):
    message = check(**kwargs)
    if message != True:
        print(message)
    else:
        id = max(students) + 1
        students[id] = {
            'name': kwargs['name'],
            'age': kwargs['age'],
            'sex': kwargs['sex'],
            'class_name': kwargs['class_name']
        }
        get_all_stasuts()


def update_student(**kwargs):
    if kwargs['id'] not in students:
        print('请输入正确的id')
        return
    message = check(**kwargs)
    if message != True:
        print(message)
    else:
        students[kwargs['id']] = {
            'name': kwargs['name'],
            'age': kwargs['age'],
            'sex': kwargs['sex'],
            'class_name': kwargs['class_name']
        }
        print('已更改学生信息为：姓名：{}、年龄：{}、性别：{}、工作：{}'.format(kwargs['id'], kwargs['name'], kwargs['age'], kwargs['sex'],
                                                        kwargs['class_name']))


get_all_stasuts()
del_studen(1)
add_student(name='孔敬淳', age=30, sex='boy')
update_student(id=4, name='jiaoyuwei', age=29, sex='boy', class_name='开发')
