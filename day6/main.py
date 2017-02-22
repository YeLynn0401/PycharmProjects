#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# from test import Teacher
from test import Teacher, Course, Students
import pickle


def insert_teacher():
    # 添加老师
    try:
        teacher_list = pickle.load(open('teacher', 'rb'))
    except:
        teacher_list = []
    name = input('输入老师名称：')
    sex = input('输入老师性别：')
    age = input('输入老师年龄：')
    teacher = Teacher(name, sex, age)
    teacher_list.append(teacher)
    pickle.dump(teacher_list, open('teacher', 'wb'))


def insert_course():
    # 添加课程
    try:
        course_list = pickle.load(open('course', 'rb'))
    except:
        course_list = []
    try:
        teacher_list = list(enumerate(pickle.load(open('teacher', 'rb'))))
    except:
        print('请先添加授课老师')
        return
    course_name = input('name').strip()
    course_time = input('time').strip()
    course_money = input('money').strip()
    for x in teacher_list:
        print(x[0], x[1].name)
    c = input('选择老师：').strip()
    course_teacher = []
    if c.isdigit():
        if int(c) < len(teacher_list):
            course_teacher = teacher_list[int(c)][1]
            print(course_teacher.name)
    course = Course(course_name, course_time, course_money, course_teacher)
    print(course)
    course_list.append(course)
    print(course_list)
    pickle.dump(course_list, open('course', 'wb'))


def insert_student():
    try:
        student_list = pickle.load(open('student', 'rb'))
    except:
        student_list = []
    # try:
    #     course_list = list(enumerate(pickle.load(open('course', 'rb')))
    # except:
    #     print('请联系管理员添加课程')
    #     return
    # try:
    #     teacher_list = list(enumerate(pickle.load(open('teacher', 'rb'))))
    # except:
    #     print('请联系管理员添加授课老师')
    #     return
    name = input('name').strip()
    pwd = input('pwd').strip()
    sex = input('sex').strip()
    age = input('age').strip()
    course_list = []
    course_record = []
    student = Students(name, pwd, sex, age, course_list, course_record)
    student_list.append(student)
    print(student_list)
    pickle.dump(student_list, open('student', 'wb'))
    print('添加成功')


def print_course_list():
    # 打印课程列表
    try:
        course_list = pickle.load(open('course', 'rb'))
    except:
        course_list = []
    print('现在共有课程数量：', len(course_list))
    print('课程名称，上课时间，课时费，授课老师')
    for i in course_list:
        print(i.name, i.course_time, i.course_money, i.course_teacher.name)


def print_student_list():
    # 打印学生列表
    try:
        student_list = pickle.load(open('student', 'rb'))
    except:
        student_list = []
    print('现在共有学生数量：', len(student_list))
    print('学生姓名，性别，年龄')
    for i in student_list:
        print(i.name, i.sex, i.age)


def print_teacher_list():
    # 打印老师列表
    try:
        teacher_list = pickle.load(open('teacher', 'rb'))
    except:
        teacher_list = []
    print('现在共有老师数量：', len(teacher_list))
    print('姓名，年龄')
    for i in teacher_list:
        print(i.name, i.age)




while True:
    print('1管理员2学生')
    c = input().strip()
    if c == '1':  # 进入管理员菜单
        i = input('1、添加老师2、添加课程3、打印课程列表 4、 打印教师列表5、添加学生6、打印学生列表').strip()
        if i == '1':  # 添加老师
            insert_teacher()
        elif i == '2':  # 添加课程
            insert_course()
        elif i == '3':   # 打印课程列表
            print_course_list()
        elif i == '4':  # 打印老师列表
            print_teacher_list()
        elif i == '5':
            insert_student()
        elif i == '6':
            print_student_list()
    elif c == '2':  # 进入学生菜单
        pass

    elif c == '4':
        pass

    else:
        print('input error ')

