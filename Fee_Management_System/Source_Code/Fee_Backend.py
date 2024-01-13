import sqlite3

def connect():
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY, receipt integer, name text, admission text, date integer, \
                    branch text, sem text, total integer, paid integer, due integer)')

       con.commit()
       con.close()

def insert(receipt = ' ', name = ' ', admission = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('INSERT INTO fee VALUES (NULL,?,?,?,?,?,?,?,?,?)',(receipt,name,admission,date,branch,sem,total,paid,due))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM fee')
       row = cur.fetchall()
       return row

       con.commit()
       

def delete(id):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('DELETE FROM fee WHERE id = ?',(id,))

       con.commit()
       con.close()

def update(id,receipt = ' ', name = ' ', admission = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('UPDATE fee SET receipt = ? OR name = ? OR admission = ? OR date = ? OR branch = ? OR sem = ? OR total = ? OR \
                    paid = ? OR due = ?',(receipt,name,admission,date,branch,sem,total,paid,due))


       con.commit()
       con.close()

def search(receipt = ' ', name = ' ', admission = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM fee WHERE  receipt = ? OR name = ? OR admission = ? OR date = ? OR branch = ? OR sem = ? OR total = ? OR paid = ? OR due = ?',(receipt,name,admission,date,branch,sem,total,paid,due))
       row = cur.fetchall()
       return row

       con.commit()
       
connect()


