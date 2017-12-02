# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class UOpenapplyIntegration(Base):
    __tablename__ = 'u_openapply_integration'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    oa_id = Column(Numeric(25, 10))
    oa_name = Column(String(40))
    whocreated = Column(String(100))
    whencreated = Column(DateTime)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    ps_student_number = Column(String(10))
