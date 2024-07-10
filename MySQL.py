import mysql.connector

msql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SamTheGreat@2005",
    database="python",
)
def create_user(name):
    sql = "Insert into user(name) VALUES(%s)"
    val= name,
    cursor= msql.cursor()
    cursor.execute(sql,val)
    msql.commit()
    print("Done")

def update_user(id, name):
    sql = "update user SET name=%s WHERE id=%s"
    val= (name,id)
    cursor= msql.cursor()
    cursor.execute(sql,val)
    msql.commit()
    print("Done")

def delete_user(id):
    sql = "delete from user WHERE id=%s"
    val= id,
    cursor= msql.cursor()
    cursor.execute(sql,val)
    msql.commit()
    print("Done")

delete_user(3)
if msql.is_connected:
    print("Connected")
    cursor= msql.cursor()
    cursor.execute("select * from user")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    msql.close
else:
    print("Not Connected")