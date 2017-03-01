#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:123456@192.168.100.5/test",
                       encoding='utf-8', echo=True)
Base = declarative_base()  # 生成orm基类


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    ip = Column(String(15), unique=True, nullable=False)
    port = Column(Integer, default=22)
    name = Column(String(64), default='host')


class HostGroup(Base):
    __tablename__ = 'hostgroup'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))


class HostUser(Base):
    __tablename__ = 'hostuser'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pwd = Column(String(64))
    key = Column(String(128))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pwd = Column(String(64))


class Host_m2m_Hostuser(Base):
    __tablename__ = 'host_m2m_hostuser'
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


class UserPermission(Base):
    __tablename__ = 'userpermission'
    id = Column(Integer, primary_key=True)
    host_user_id = Column(Integer, ForeignKey('host_m2m_hostuser.id'))



Base.metadata.create_all(engine)