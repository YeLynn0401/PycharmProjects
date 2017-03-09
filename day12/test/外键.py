#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:123456@localhost/test",
                       encoding='utf-8', echo=True)
Base = declarative_base()  # 生成orm基类



class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    register_date = Column(String(64))

    def __repr__(self):
        return '{} {}'.format(self.id, self.name)


class StudyRecord(Base):
    __tablename__ = 'studentrecord'  # 表名
    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'))
    student = relationship("Student", backref="address")

    def __repr__(self):
        return '{} {} {}'.format(self.student.name, self.day, self.status)

Base.metadata.create_all(engine)  # 创建表结构
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# s1 = Student(name='alex', register_date='2014-05-21')
# s2 = Student(name='Jack', register_date='2014-05-21')
# s3 = Student(name='Rain', register_date='2014-05-21')
# study_obj1 = StudyRecord(day=1, status='yes', stu_id=2)
# study_obj2 = StudyRecord(day=2, status='yes', stu_id=3)
# study_obj3 = StudyRecord(day=3, status='yes', stu_id=1)
# Session.add_all([study_obj1,study_obj2])
# Session.commit()
# obj1 = Session.query(Student).filter(Student.name == 'alex').first()
# # print(obj1.student)
# print(obj1.address)
a = Session.query(Student).join(StudyRecord).all()
for j in a:
    print(j.id, j.name, j.register_date)
    for i in j.address:
        print(i.day, i.status)