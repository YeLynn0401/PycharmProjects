#!/usr/bin/env python
# -*- coding: utf-8 -*-

import t_1
from sqlalchemy.orm import sessionmaker


Session_class = sessionmaker(bind=t_1.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
s = Session_class()  # 生成session实例
while True:
    print('1、学生 \n2、教师')
    choose = input(':').strip()
    if choose == '1':
        name = input('name:').strip()
        date = s.query(t_1.Student).filter_by(name=name).first()
        if date:
            pwd = input('pwd:').strip()
            if date.pwd == pwd:
                print('Welcome')
                # 关系表
                # for i in date.stu_class:
                #     print(i.id)
                # print(date.id, date.name, date.qq)
                print('1、提交作业\n2、查看排名')
                choose = input(':').strip()
                if choose == '1':
                    c_id = None
                    student_class = s.query(t_1.Student_class_relationship).filter_by(stu_id=date.id).all()
                    for i in student_class:
                        print(i.id, i.student_class.class_name)
                    c = input('请输入ID：:').strip()
                    for i in student_class:
                        if i.id == int(c):
                            c_id = i.id
                    if c_id:
                        ss = s.query(t_1.Study_recording).filter_by(r_id=c_id).all()
                        print('id, 课程，作业，分数')
                        for i in ss:
                            print('id:{}, 课程:{}，作业是否提交:{}，分数:{}'.format(i.id, i.content, i.record, i.score))
                        choose = input('输入要交作业的ID').strip()
                        if choose.isdigit():
                            for i in ss:
                                if i.id == int(choose):
                                    if i.record:
                                        print('已经交过了')
                                    else:
                                        i.record = True
                                        s.commit()
                                        print('作业提交成功')
                        else:
                            print('输入有误。')
                    else:
                        print('输入有误')

                elif choose == '2':
                    for i in date.studentclass:
                        print(i.id, i.class_name)
                    id = input('请选择班级ID：').strip()
                    q = s.query(t_1.Student_class_relationship).filter_by(class_id=id).order_by(t_1.Student_class_relationship.results.desc())
                    assert q
                    for i in enumerate(q):
                        if i[1].stu_id == date.id:
                            print('班里共{}人，你在排名是第：{}位，作业总分{}分'.format(q.count(), i[1].stu_id, i[1].results))

            else:
                print('密码错误')
        else:
            print('用户名不存在')
    elif choose == '2':
        print('1、班级添加\n2、上课记录\n3、学员分班\n4、上课\n5、批改作业\n6、成绩修正')
        choose = input(':').strip()
        if choose == '1':

            print('请输入班级名称')
            c_name = input(':').strip()
            if c_name:
                c = t_1.Student_class(class_name=c_name)
                s.add(c)
                s.commit()
                print('添加成功')
                date = s.query(t_1.Student_class).filter_by().all()
                for i in date:
                    print(i.id, i.class_name)
            else:
                print('班级名称不能为空')

        elif choose == '2':
            pass
        elif choose == '3':
            class_list = []
            date = s.query(t_1.Student_class).filter_by().all()
            for i in date:
                class_list.append(i.id)
                print(i.id, i.class_name)
            print(class_list)
            print('请选择要管理的班级id：')
            class_id  = input(':').strip()
            try:
                if int(class_id) in class_list:
                    while True:
                        print('请输入学生QQ号：')
                        qq = input(':').strip()
                        if qq == 'q':
                            break
                        date = s.query(t_1.Student).filter_by(qq=qq).first()
                        if date:
                            stu_r = t_1.Student_class_relationship(stu_id=date.id, class_id=int(class_id))
                            s.add(stu_r)
                            s.commit()
                            print('添加成功')
                        else:
                            print('查无此人')
                else:
                    print('输入有误。')
            except:
                print('输入有误。')
        elif choose == '4':
            class_list = []
            date = s.query(t_1.Student_class).filter_by().all()
            for i in date:
                class_list.append(i.id)
                print(i.id, i.class_name)
            print('请选择上课班级：')
            class_id = input(':').strip()
            try:
                class_id = int(class_id)
                if class_id in class_list:
                    print('请输入课程主题：')
                    class_content = input(':').strip()
                    if class_content:
                        date = s.query(t_1.Student_class_relationship).filter_by(class_id=class_id).all()
                        for i in date:
                            o = t_1.Study_recording(r_id=i.id, content=class_content, score=None, record=False)
                            s.add(o)
                            s.commit()
                        print('上课完成。')
                    else:
                        raise Exception('课程内容为空')
                else:
                    raise Exception('输入有误')
            except:
                print('输入有误')
        elif choose == '5':
            class_list = []
            date = s.query(t_1.Student_class).all()
            #  打印班级列表
            for i in date:
                class_list.append(i.id)
                print(i.id, i.class_name)
            print('请选择需要批改的班级：')
            class_id = input(':').strip()
            try:

                date = s.query(t_1.Student_class_relationship).filter_by(class_id=int(class_id)).all()
                # 查询到所有学生，逐个批改
                for i in date:
                    recording_date = s.query(t_1.Study_recording).filter_by(r_id=i.id).all()
                    if recording_date:
                        for k in recording_date:
                            # print(k.record, type(k.record), k.score, type(k.score))
                            if k.record and not k.score:  # 作业交了，而且没有评分
                                print(i.student.name, k.content)
                                print('请输入成绩')
                                score = input(':').strip()
                                if score.isdigit():
                                    k.score = int(score)
                                    i.results = i.results+int(score) if i.results else int(score)
                                    s.commit()
                                else:
                                    print('输入有误')

                    else:
                        print('没有上课记录')
                print('已交作业全部批改完成。')
            except:
                print('输入有误')
        elif choose == '6':
            # 成绩修正
            data = s.query(t_1.Student_class).all()
            # 打印班级列表
            for c in data:
                print(c.id, c.class_name)
            id = input('请选择班级ID：').strip()
            try:
                stu = s.query(t_1.Student_class_relationship).filter_by(class_id=int(id)).all()
                # 查询班里的所有同学
                for i in stu:
                    # 查询单个同学的所有成绩
                    co = s.query(t_1.Study_recording).filter_by(r_id=i.id).all()
                    # 遍历上课记录
                    results = 0
                    # 计算成绩
                    for x in co:
                        if x.record:
                            results += x.score
                            print(x.score, x.content)
                    i.results = results
                    print(results)
                    s.commit()
                    print('修正成功')
            except:
                print('输入输入有误。')
