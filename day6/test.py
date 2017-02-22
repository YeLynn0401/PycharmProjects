#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import pickle


class Teacher:
    # 教室类
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.money = 0


class Course:
    # 课程类
    def __init__(self, name, course_time, course_money, course_teacher):
        self.name = name
        self.course_time = course_time
        self.course_money = course_money
        self.course_teacher = course_teacher


class Students:
    # 学生类
    def __init__(self, name, pwd, sex, age, course_list, course_record):
        self.name = name
        self.pwd = pwd
        self.sex = sex
        self.age = age
        self.course_list = course_list
        self.course_record = course_record

# obj1 = Teacher('name1', 'M', 22)
# obj2 = Teacher('name2', 'M', 23)  # 创建老师
# obj3 = Teacher('name3', 'M', 25)  # 创建老师
# obj4 = Teacher('name4', 'M', 26)  # 创建老师
# pickle.dump([obj1, obj2, obj3, obj4], open('db', 'wb'))
#
# course1 = Course('cour1', '11-11', 20, obj1)  # 创建课程
# course2 = Course('cour2', '11-11', 20, obj1)
# course3 = Course('cour3', '11-11', 20, obj1)
# pickle.dump([course1, course2, course3], open('teacher', 'wb'))
# stu1 = Students('name1', 'pwd', 'M', 14, [course1, course2, course3], {course1: [1, 3, 5], })  # 创建学生
#
# pickle.dump(stu1, open('sb_stu', 'wb'))
