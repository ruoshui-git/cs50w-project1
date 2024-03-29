from os import getenv
import psycopg2
from sqlalchemy import create_engine
import csv

# local test database 
# engine = create_engine('postgresql://postgres:postgres@localhost:5432/project1')

if not getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# actual database
engine = create_engine(getenv("DATABASE_URL"))

db = engine.connect()

fin = open("books.csv")
reader = csv.reader(fin)

db.execute("""CREATE TABLE books_lower (
    id SERIAL PRIMARY KEY,
    isbn CITEXT NOT NULL,
    title CITEXT NOT NULL,
    author CITEXT NOT NULL,
    year INTEGER NOT NULL
    );""")

next(reader)  # get rid of title line

for info in reader:
    db.execute("""INSERT INTO books_lower 
                    (isbn, title, author, year)
                    VALUES (%s, %s, %s, %s)""", info)

db.commit()
