import sqlite3
c=sqlite3.connect("info.db")
c.execute("insert into userinfo (name,pin,balance) \
          values('Vishesh',1234,100)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Vivek',2345,200)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Vidya',3456,300)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Sandeep',4567,400)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Nishant',5678,500)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Aniket',6789,600)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Abhishek',7891,700)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Virat',8910,800)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Ram',9101,900)");
c.execute("insert into userinfo (name,pin,balance) \
          values('Ajay',1011,1000)");
c.commit()
