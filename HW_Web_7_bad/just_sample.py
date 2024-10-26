# from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
# from sqlalchemy import MetaData
# from sqlalchemy.sql import select
#
#
# engine = create_engine('sqlite:///:memory:', echo=True)
#
# metadata = MetaData()
#
# users = Table('users', metadata,
#               Column('id', Integer, primary_key=True),
#               Column('name', String),
#               Column('fullname', String),
#               )
#
# addresses = Table('addresses', metadata,
#                   Column('id', Integer, primary_key=True),
#                   Column('user_id', Integer, ForeignKey('users.id')),
#                   Column('email_address', String, nullable=False)
#                   )
#
# metadata.create_all(engine)
#
#
# with engine.connect() as conn:
#     ins = users.insert().values(name='jack', fullname='Jack Jones')
#     print(str(ins))
#     result = conn.execute(ins)
#
#     s = select(users)
#     result = conn.execute(s)
#     for row in result:
#         print(row)
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = sqlalchemy.orm.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)

Base.metadata.create_all(engine)
Base.metadata.bind = engine

# new_person = Person(name="Bill")
# session.add(new_person)
#
# session.commit()
#
# new_address = Address(post_code='00000', person=new_person)
# session.add(new_address)
# session.commit()

for person in session.query(Person).all():
    print(person.name)