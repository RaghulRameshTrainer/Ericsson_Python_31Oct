import sqlite3

dbh=sqlite3.connect("ericsson.db")
c=dbh.cursor()

def create_table():
    c.execute("CREATE TABLE employee(empname TEXT, exp REAL, tech TEXT)")

def load_data():
    e_name=input("Enter your name: ")
    e_exp=int(input("Enter your experience: "))
    e_tech=input("Enter your technology: ")
    c.execute("INSERT INTO employee VALUES(?,?,?)",(e_name,e_exp,e_tech))
    #c.execute("INSERT INTO employee VALUES('Bala',25,'Python')")
    #c.execute("INSERT INTO employee VALUES('Saran',20,'Java')")

def update_data():
    c.execute("UPDATE employee SET tech='Python' WHERE empname='Karthik'")

def delete_data():
    c.execute("DELETE FROM employee WHERE tech='Selenium'")
    dbh.commit()
    c.close()
    dbh.close()

def fetch_data():
    c.execute("SELECT * FROM employee")
    #fetchone, fetchmany, fetchall
    #print(c.fetchone())
    #print(c.fetchmany(5))
    for rec in c.fetchall():
        if rec[1] >= 20:
            print(f"{rec[0]} - {rec[1]} - {rec[2]}")
#create_table()
# for x in range(5):
#     load_data()
#update_data()
#delete_data()
fetch_data()