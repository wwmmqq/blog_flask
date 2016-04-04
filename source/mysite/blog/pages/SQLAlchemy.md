title: SQLAlchemy + sqlite3
date: Monday, April 4, 2016
time: 2016_04_04
summary: ORM的作用就是把数据库表的一行记录与一个对象互相做自动转换。
tags: python

# <center>Object-Relational Mapping (ORM)</center>

ORM的作用就是把数据库表的一行记录与一个对象互相做自动转换。


## SQLite

	1. 表是数据库中存放关系数据的集合
	2. 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为connection；
	3. 连接到数据库后，需要打开游标，称之为cursor，通过cursor执行SQL语句，然后，获得执行结果。
	4. Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
	5. 由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

### 使用cursor执行insert, update, delete时, 由rowcount返回执行结果(影响的行数)
	
	sql语句传参:
		cursor.execute('select * from user where id=?', '51')
		?个数应于后面参数个相对应

### 使用cursor执行select时, 由fetchall()返回结果(结果集是一个list, 每个元素是一个tuple, 对应一行记录)


### eg.

	import sqlite3
	conn = sqlite3.connect('example.db')
	cursor = conn.cursor()

	try:
		# create table
		cursor.execute('''
			CREATE TABLE person
        	(id INTEGER PRIMARY KEY, name varchar(250) NOT NULL)
          	''')

        c.execute('''
			CREATE TABLE address
			(id INTEGER PRIMARY KEY, street_name varchar(250), street_number varchar(250),
			post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
			FOREIGN KEY(person_id) REFERENCES person(id))
			''')

		cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')


		# insert table
		c.execute('''
			INSERT INTO person VALUES(1, 'wwmmqq')
			''')
		c.execute('''
			INSERT INTO address VALUES(1, 'ecnu', '500', '200241', 1)
			''')

		cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

		cursor.rowcount
		cursor.close()
		conn.commit()

		# select table

		cursor.execute('SELECT * FROM person')
		print cursor.fetchall()
		cursor.execute('SELECT * FROM address')
		print cursor.fetchall()
	except:
		print "failed"
	finally:
		conn.close()

## SQLAlchemy
	SQLAlchemy是Python中的ORM框架
	There are three most important components in writing SQLAlchemy code:
	1. A Table that represents a table in a database.
	2. A mapper that maps a Python class to a table in a database.
	3. A class object that defines how a database record maps to a normal Python object.

### eg1:
	# creat.py
	from sqlalchemy import Column, ForeignKey, Integer, String
	from sqlalchemy.ext.declarative import declarative_base
	from sqlalchemy.orm import relationship
	from sqlalchemy import create_engine

	Base = declarative_base()

	class Person(Base):
		__tablename__ = 'person'
		id = Column(Integer, primary_key=True)
		name = Column(String, nullable=False)

	class Address(Base):
		__tablename__ = 'address'
		id = Column(Integer, primary_key=True)
		stress_name = Column(String(250))
		stress_number = Column(String(250))
		post_code = Column(String(250), nullable=False)
		person_id = (Integer, ForignKey('person.id'))
		person = relationship(Person)

	engine = create_engine('sqlite:///example.db')
	Base.metadata.create_all(engine)


### eg2:
	#flush之后你才能在这个session中看到效果，而commit之后你才能从其它session中看到效果
	# flush就是把客户端尚未发送到数据库服务器的SQL语句发送过去,commit就是告诉数据库服务器提交事务
	#insert.py
	from sqlalchemy import create_engine
	from sqlalchemy.orm import sessionmaker
	 
	from creat import Address, Base, Person
	engine = create_engine('sqlite:///example.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()


	# Insert a Person in the person table
	new_person = Person(name='wwmmqq2')
	session.add(new_person)
	p1 = Person(name='Tom')
	p2 = Person(name='Jack')
	session.addall([p1, p2])
	session.flush()
	 
	# Insert an Address in the address table
	new_address = Address(post_code='00000', person=new_person)
	session.add(new_address)
	session.flush()

	# Make a query to find all Persons in the database
	session.query(Person).all()
	person = session.query(Person).first()
	print person.name

	# Find all Address whose person field is pointing to the person object
	session.query(Address).filter(Address.person == person).all()
	address = session.query(Address).filter(Address.person == person).one()
	print address.stress_name

	#update table
	q = session.query(Person).filter(Person.name=='Tom')
	q.one().name = 'Uncle Tom'
	session.commit()




