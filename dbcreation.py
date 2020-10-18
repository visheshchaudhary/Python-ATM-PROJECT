import sqlite3
c=sqlite3.connect("info.db")
c.execute('''create table userinfo
            (name text not null,
            pin int primary key not null,
            balance real not null);''')
print("table created")


