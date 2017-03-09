#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(20)),
             )

color = Table('color', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(20)),
              )
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test", max_overflow=5, echo=True)

metadata.create_all(engine)