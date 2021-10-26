from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()
class Newresult(Base):
    __tablename__ = 'Newresults'
    id = Column('id', Integer, primary_key=True)
    a = Column('a', Integer)
    b = Column('b', Integer)
    res = Column('res', Integer)
engine = create_engine('sqlite:///newresults.db', echo=True)
    #engine = create_engine('sqlite:///memory', echo=True)
Base.metadata.create_all(bind=engine)

Session=sessionmaker(bind=engine)
session=Session()
newresults=session.query(Newresult).all()
for newresult in newresults:
    print('calc with a=%d and b=%d'%(newresult.a, newresult.b,))
session.close()