# Python and Databases Project

## Overview
Welcome to the Python and Databases project! This project aims to bridge the gap between two fascinating worlds: Databases and Python. In the first part, we will explore connecting to a MySQL database and executing SQL queries using the `MySQLdb` module. In the second part, we'll dive into the world of Object Relational Mapping (ORM) with the powerful `SQLAlchemy` module.

The primary goal of using an ORM like SQLAlchemy is to abstract the storage details, allowing you to focus on working with Python objects rather than writing explicit SQL queries. This not only enhances code readability but also makes your project storage-agnostic, enabling you to switch databases effortlessly without rewriting the entire codebase.

## Code Comparison
Let's illustrate the difference between traditional SQL queries and ORM usage:

**Without ORM:**
```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

**With ORM (using SQLAlchemy):**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, State  # Assuming you have a State model defined

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Embrace the power of ORM and enjoy coding with Python!

## Learning Objectives
Upon completing this project, you should be able to:

- Understand why Python programming is awesome.
- Connect to a MySQL database from a Python script.
- Perform SELECT and INSERT operations in a MySQL table using Python.
- Grasp the concept of Object Relational Mapping (ORM).
- Map a Python Class to a MySQL table using SQLAlchemy.
- Create a Python Virtual Environment for project-specific dependencies.

## Resources
Explore the following resources to enhance your understanding:

- [Object-relational mappers](link-to-orm-resources)
- [mysqlclient/MySQLdb documentation](link-to-mysqldb-doc)
- [MySQLdb tutorial](link-to-mysqldb-tutorial)
- [SQLAlchemy tutorial](link-to-sqlalchemy-tutorial)
- [SQLAlchemy](link-to-sqlalchemy)
- [Python Virtual Environments: A primer](link-to-venv-tutorial)

## Requirements
Ensure your project adheres to the following guidelines:

- Use editors: vi, vim, emacs.
- Interpret/compile on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- Execute with MySQLdb version 2.0.x and SQLAlchemy version 1.4.x.
- End all files with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- Include a mandatory README.md file at the root of the project folder.
- Utilize pycodestyle (version 2.8.*) for code formatting.
- All files must be executable.
- Ensure proper documentation for modules, classes, and functions.
- Avoid using `execute` with SQLAlchemy.

## Installation and Activation
Follow these steps to create a Python Virtual Environment and install the required modules:

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
$ sudo pip3 install mysqlclient
$ sudo pip3 install SQLAlchemy
```

