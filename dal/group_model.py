"""
This code was generated by a tool. Don't modify it manually.
http://sqldalmaker.sourceforge.net
"""

from sqlalchemy import *

from .data_store import *


class GroupModel(Base):
    __tablename__ = 'groups'

    g_id = Column('g_id', Integer, primary_key=True, autoincrement=True)
    g_name = Column('g_name', String)
