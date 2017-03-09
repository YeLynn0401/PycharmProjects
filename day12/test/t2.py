#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


from sqlalchemy.orm import sessionmaker

from day12.test import t1

session_class = sessionmaker(bind=t1.engine)
session = session_class()

addr1 = t1.Address(add_ress='bj')
addr2 = t1.Address(add_ress='sh')
addr3 = t1.Address(add_ress='gz')
addr4 = t1.Address(add_ress='sz')
session.add_all([addr1, addr2, addr3, addr4])
o1 = t1.User(name='fan', b_address=addr1, r_address=addr2)
o2 = t1.User(name='sun', b_address=addr3, r_address=addr4)
session.add_all([o1,o2])
session.commit()