#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
多对多

'''

from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
enging = create_engine('mysql+pymysql://root:123456@192.168.100.5/test?charset=utf8', encoding='utf-8', echo=False)

class Auther(Base):
    __tablename__ = 'auther'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    age = Column(Integer)
    def __repr__(self):
        return self.name

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    text = Column(String(128))
    authers = relationship('Auther', secondary='books_m2m_auther', backref='books')
    def __repr__(self):
        return self.name


books_m2m_auther = Table('books_m2m_auther', Base.metadata,
                         Column('book_id', Integer, ForeignKey('books.id')),
                         Column('auther_id', Integer, ForeignKey('auther.id'))
                         )

Base.metadata.create_all(enging)

session_class = sessionmaker(bind=enging)
session = session_class()

# b1 = Books(name='b1', text='this is b1')
# b2 = Books(name='b2', text='this is b2')
# b3 = Books(name='b3', text='this is b3')
#
#
# a1 = Auther(name='a1', age=18)
# a2 = Auther(name='a2', age=18)
# a3 = Auther(name='a3', age=18)
#
# b1.authers = [a1]
# b2.authers = [a1, a3]
# b3.authers = [a1, a2, a3]
#
# session.add_all([a1, a2, a3, b1, b2, b3,])
# session.commit()

data = session.query(Auther).filter_by(name='a1').first()
print(data.books)
