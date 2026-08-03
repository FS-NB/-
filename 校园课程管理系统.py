"""

### 题目背景

某学校需要开发一个课程管理系统，用于管理教师、学生以及课程之间的关联关系。请使用面向对象思想完成以下设计。

"""


# todo **（一）人员类 `Person`（父类）**
#   属性：
#  `name`：姓名（由外部传入，私有属性）
#   age`：年龄（私有属性，由外部传入）
#   `__role`：角色（私有属性，默认 `"普通人员"`）

class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__role = '普通人员'

    # get_name()`：获取姓名
    def get_name(self):
        return self.__name

    # `set_age(age)`：设置年龄，限制 `18~65` 岁之间
    def set_age(self, age):
        if 18 <= age <= 65:
            self.__age = age
        else:
            print('你out了')

    # `get_age()`：获取年龄
    def get_age(self):
        return self.__age

    # `get_role()`：获取角色
    def get_role(self):
        return self.__role

    # `__str__()`：返回 `"姓名：{name}，年龄：{age}，角色：{role}"`
    def __str__(self):
        return f"姓名：{self.__name}，年龄：{self.__age}，角色：{self.__role}"


# todo **（二）子类 `Teacher`（继承 `Person`）**
#   - 在 `__init__` 中将 `__role` 设置为 `"教师"`
#   - 新增属性 `course`：所教课程（由外部传入）
#   - 新增方法 `teach()`：打印 `"{name} 正在讲授 {course} 课程"`
#   - 新增方法 `grade_student(student_name, score)`：打印 `"{name} 给 {student_name} 打分为 {score} 分"`
class Teacher(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
        self.__role = '教师'

    def teach(self):
        print(f'{self.get_name()} 正在讲授 {self.course} 课程')

    def grade_student(self, student_name, score):
        print(f"{self.get_name()} 给 {student_name} 打分为 {score} 分")


# todo - 在 `__init__` 中将 `__role` 设置为 `"学生"`
#   - 新增属性 `scores`：成绩字典（默认为空，键为课程名，值为分数）
#   - 新增方法 `add_score(course, score)`：添加或更新某门课程的成绩
#   - 新增方法 `get_average()`：计算所有课程的平均分，如果没有成绩返回 `0`
#   - 新增方法 `is_passed()`：所有课程都 `>= 60` 返回 `True`，否则返回 `False`
#   - 重写 `__str__()`：在父类基础上追加 `"，成绩：{scores}"`
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.scores = {}
        self.__role = '学生'

    def add_score(self, course, score):
        self.scores[course] = score

    average = 0
    def get_average(self, scores):
        total = 0
        count = 0
        if scores:
            for k in self.scores:
                total += self.scores[k]
                count += 1
                Student.average = total / count
        else:
            return 0

    def is_passed(self):
        if Student.average >= 60:
            return True
        else:
            return False

    def __str__(self):
        return f"姓名：{self.get_name()}，年龄：{self.get_age()}，角色：{self.__role}，成绩{self.scores}"


# todo 属性：
#  - `name`：课程名称（由外部传入）
#  - `teacher`：任课教师（由外部传入，`Teacher` 对象）
#  - `students`：选课学生列表（默认为空列表）
#  - `__max_students`：最大容纳人数（私有属性，默认 `30`）
#  方法：
#  - `add_student(student)`：添加学生到选课列表，超过最大人数时提示 `"课程已满"`
#  - `remove_student(name)`：根据姓名移除学生
#  - `get_student_count()`：返回当前选课人数
#  - `show_info()`：打印课程信息（课程名、任课教师姓名、选课人数）
#  - `__str__()`：返回课程完整信息
class Course(object):
    # 类属性 `total_courses`：记录创建的课程总数
    total_courses = 0

    def __init__(self, name, teacher):
        Course.total_courses += 1
        self.name = name
        self.teacher = teacher
        self.students = []
        self.__max_students = 30

    def add_student(self, student):
        if len(self.students) <= 30:
            self.students.append(student)
        else:
            print("课程已满")

    def remove_student(self, name):
        self.students.remove(name)

    def get_student_count(self):
        return len(self.students)

    def show_info(self):
        print(f'课程名{self.name}、任课教师姓名{self.teacher}、选课人数{len(self.students)}')

    def __str__(self):
        return Course.show_info(self)

    # 类方法 `show_total()`：打印 `"学校共开设了 {total_courses} 门课程"`
    @classmethod
    def show_total(cls):
        print(f"学校共开设了 {cls.total_courses} 门课程")

    # 静态方法 `is_valid_score(score)`：判断分数是否在 `0~100` 之间，返回 `True/False`
    @staticmethod
    def is_valid_score(score):
        if 0 <= score <= 100:
            return True
        else:
            return False


# 1. 创建两个 `Teacher` 对象：
#
#   - `"张老师"`，`35` 岁，教 `"Python编程"`
#   - `"李老师"`，`42` 岁，教 `"数据结构"`
teacher1 = Teacher("张老师", 35, "Python编程")
teacher2 = Teacher("李老师", 42, "数据结构")

# 2. 创建三个 `Student` 对象：
#
#   - `"小明"`，`20` 岁
#   - `"小红"`，`19` 岁
#   - `"小刚"`，`21` 岁
student1 = Student("小明", 20)
student2 = Student("小红", 20)
student3 = Student("小刚", 20)

# 3. 创建两个 `Course` 对象：
#
#   - `"Python编程"`，任课教师为张老师
#   - `"数据结构"`，任课教师为李老师
course1 = Course("Python编程",'任课教师为张老师')
course2 = Course("数据结构",'任课教师为李老师')

# 将小明、小红选入 `"Python编程"` 课程
course1.add_student(student1)
course1.add_student(student2)

# 将小红、小刚选入 `"数据结构"` 课程
course2.add_student(student2)
course2.add_student(student3)

# 打印两门课程的信息（调用 `show_info()`)
course1.show_info()
course2.show_info()

# 张老师给小明打分 `95`，给小红打分 `82`
teacher1.grade_student('小明','95')
teacher1.grade_student('小红','82')

# 李老师给小刚打分 `58`，给小红打分 `90`
teacher2.grade_student('小刚','58')
teacher2.grade_student('小红','90')

student1.add_score('Python编程',95)
student2.add_score('Python编程',82)
student2.add_score('数据结构',90)
student3.add_score('数据结构',58)

# 分别打印三位学生的完整信息（调用 `__str__`）
print(student1)
print(student2)
print(student3)

# 计算并打印小明的平均分和是否及格
student1.get_average(student1)
print(f'小明的平均分{Student.average},是否及格{Student.is_passed(student1.scores)}')
student2.get_average(student2)
print(f'小明的平均分{Student.average},是否及格{Student.is_passed(student2.scores)}')

# 调用 `Course.show_total()` 查看课程总数
course1.show_total()
# 调用 `Course.is_valid_score(105)` 测试静态方法
print(course2.is_valid_score(105))




