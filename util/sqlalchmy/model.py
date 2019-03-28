# coding: utf-8

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import Base
from setting import ENGINE


class Model(Base):
    """
    モデルクラス
    """
    __tablename__ = 'model'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    age = Column('age', Integer)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
