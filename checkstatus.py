import  sqlite3


data_base = sqlite3.connect('db.sqlite3')

b=[]
cursor=data_base.cursor()
# cur=cursor.execute('SELECT * FROM jenkinsjob_jenkinsjob;')
# print(cur.fetchall())
with open('check.txt','r') as f:
    for i in f:
        a=tuple(i.strip('\n').split(','))
        b.append(a)

cursor.executemany('INSERT INTO workorder_projectcheck(business_name,module_title,project_title,hostip,port,check_url) VALUES (?,?,?,?,?,?);',b)
cur=cursor.execute('SELECT * FROM workorder_projectcheck;')
print(cur.fetchall())
cursor.close()
data_base.commit()