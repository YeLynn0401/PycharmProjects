#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@192.168.100.5/test?charset=utf8", encoding='utf8', echo=False)
Base = declarative_base()


class Student(Base):  # 学生表
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pwd = Column(String(64))
    qq = Column(String(64), unique=True)
    # authors = relationship('Author', secondary=book_m2m_author,backref='books')
    studentclass = relationship("Student_class", secondary='student_class_relationship', backref="student")
    stu_class = relationship("Student_class_relationship")
    #
    # def __repr__(self):
    #     return self.name


class Student_class(Base):  # 班级表
    __tablename__ = 'student_class'
    id = Column(Integer, primary_key=True)
    class_name = Column(String(32))
    def __repr__(self):
        return self.class_name


class Student_class_relationship(Base):  # 学生班级
    __tablename__= 'student_class_relationship'
    id = Column(Integer, primary_key=True)
    stu_id = Column(Integer, ForeignKey('student.id'))
    class_id = Column(Integer, ForeignKey('student_class.id'))
    results = Column(Integer, default=0)  # 记录总成绩，方便排序
    student = relationship("Student", backref="cla")
    student_class = relationship("Student_class", backref="cla_rrr")
    record = relationship("Study_recording", backref="cla")


class Study_recording(Base):  # 上课记录
    __tablename__ = 'study_recording'
    id = Column(Integer, primary_key=True)
    r_id = Column(Integer, ForeignKey('student_class_relationship.id'))
    content = Column(String(64))
    score = Column(Integer)
    record = Column(Boolean)
    r = relationship("Student_class_relationship", backref="ad")


Base.metadata.create_all(engine)
