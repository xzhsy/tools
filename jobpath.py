import  sqlite3


data_base = sqlite3.connect('db.sqlite3')

b=[]
cursor=data_base.cursor()
# cur=cursor.execute('SELECT * FROM jenkinsjob_jenkinsjob;')
# print(cur.fetchall())
with open('job.txt','r') as f:
    for i in f:
        a=tuple(i.strip('\n').split(','))
        b.append(a)

cursor.executemany('INSERT INTO jenkinsjob_jenkinsjob(business_name,module_name,project_name,fullname,deploy_order,create_time) VALUES (?,?,?,?,?,?);',b)
cur=cursor.execute('SELECT * FROM jenkinsjob_jenkinsjob;')
print(cur.fetchall())
cursor.close()
data_base.commit()