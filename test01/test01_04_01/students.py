# coding:utf-8
# @Create time: 2021/2/25 4:51 下午
# @Author: KongJingchun
# @remark:实现学生信息库面向对象并增加批量功能

class StudentInfo(object):
    def __init__(self, students):
        self.students = students

    def get_all(self):
        print(len(students))
        for key, value in self.students.items():
            print(
                '学号：{}、姓名：{}、年龄：{}、性别：{}、工作：{}'.format(key, value['name'], value['age'], value['sex'],
                                                       value['class_name']))

    def check(self, **kwargs):
        if 'name' not in kwargs:
            return '请输入正确的姓名'
        if 'age' not in kwargs:
            return '请输入正确的年龄'
        if 'sex' not in kwargs:
            return '请输入正确的性别'
        if 'class_name' not in kwargs:
            return '请输入正确的工作'
        return True

    def delete(self, id):
        if id in self.students:
            user = self.students.pop(id)
            print('已删除学号为{}的学生，姓名：{}、年龄：{}、性别：{}、工作：{}'.format(id, user["name"], user["age"], user["sex"],
                                                               user["class_name"]))
        else:
            print('不存在该学生')

    def adds(self, students):
        for student in students:
            message = self.check(**student)
            if message != True:
                print(message)
            else:
                self.__add(student)

    def deletes(self, ids):
        for id_ in ids:
            self.delete(id_)

    def add_student(self, **student):
        message = self.check(**student)
        if message != True:
            print(message)
        else:
            self.__add(student)

    def __add(self, student):
        id = max(self.students) + 1
        self.students[id] = {
            'name': student['name'],
            'age': student['age'],
            'sex': student['sex'],
            'class_name': student['class_name']
        }

    def update(self, **kwargs):
        if kwargs['id'] not in self.students:
            print('请输入正确的id')
            return
        message = self.check(**kwargs)
        if message != True:
            print(message)
        else:
            self.students[kwargs['id']] = {
                'name': kwargs['name'],
                'age': kwargs['age'],
                'sex': kwargs['sex'],
                'class_name': kwargs['class_name']
            }
            print('已更改学生信息为：学号：{}、姓名：{}、年龄：{}、性别：{}、工作：{}'.format(kwargs['id'], kwargs['name'], kwargs['age'],
                                                                  kwargs['sex'],
                                                                  kwargs['class_name']))

    def updates(self, update_students):
        for student in update_students:
            id_ = list(student.keys())[0]
            if id_ not in self.students:
                print('ID: {} 不存在'.format(id_))
                continue
            user_info = student.get(id_)
            message = self.check(**user_info)
            if message != True:
                print(message)
                continue
            self.students[id_] = user_info
            print('所有信息更新完成')

    def find_user(self, **kwargs):
        values = list(students.values())
        # key = None
        # value = None
        result = []
        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs[key]
        elif 'class_name' in kwargs:
            key = 'class_name'
            value = kwargs
        else:
            print('没有发现可搜索的关键字')
            return
        for user in values:
            if value in user[key]:
                result.append(user)
        return result


if __name__ == '__main__':
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

    student_info = StudentInfo(students)
    student_info.get_all()
    student_info.add_student(name='曹雅杰', age=27, sex='girl', class_name='家庭主妇')
    student_info.delete(6)
    student_info.update(id=1, name='kjc', age=27, sex='boy', class_name='开发测试')
    users = [
        {'name': '批量添加1', 'age': 1, 'sex': 'boy', 'class_name': '批量测试'},
        {'name': '批量添加2', 'age': 2, 'sex': 'boy', 'class_name': '批量测试'}
    ]
    student_info.adds(users)
    student_info.get_all()
    student_info.deletes([1, 2])
    student_info.updates([
        {60: {'name': '批量添加10', "age": 10, 'sex': "boy1", 'class_name': '批量修改1'}},
        {7: {'name': '批量添加20', "age": 20, 'sex': "boy2", 'class_name': '批量修改2'}},
    ])
    student_info.get_all()
    st = student_info.find_user(name='倩')
    print(st)
