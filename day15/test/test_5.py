#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://51cto:51cto@192.168.100.5/article?charset=utf8",encoding='utf-8', echo=False)
Base = declarative_base()  # 生成orm基类


class article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    user = Column(String(64),)
    article = Column(String(128),)
Base.metadata.create_all(engine)
# session_class = sessionmaker(bind=engine)
# session = session_class()
#
# a1 = article(user='alex', article='day1')
# a2 = article(user='alex', article='day2')
# session.add_all([a1, a2])
# session.commit()
