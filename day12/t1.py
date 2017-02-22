#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('mysql+pymysql://root:123456@192.168.100.10/test', echo=True)
Base = declarative_base()

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    add_ress = Column(String(64))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    b_addr = Column(Integer, ForeignKey('address.id'))
    r_addr = Column(Integer, ForeignKey('address.id'))
    b_address = relationship("Address", foreign_keys=[b_addr,])
    r_address = relationship("Address", foreign_keys=[r_addr,])

Base.metadata.create_all(engine)