# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class UOpenapplyIntegration(Base):
    __tablename__ = 'u_openapply_integration'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    whocreated = Column(String(100))
    whencreated = Column(DateTime)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    ps_student_number = Column(String(10))
    status = Column(String(40), server_default="_")
    passport_id = Column(String(40), server_default="")
    first_name = Column(String(40))
    last_name = Column(String(40))
    address = Column(String(40), server_default="")
    address_ii = Column(String(40), server_default="")
    full_address = Column(String(40), server_default="")
