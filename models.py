from distutils import command
import sqlite3
import mysql.connector 

def create_post(name, content):

    con = mysql.connector.connect(host='localhost',user='root', password='', db='posts')
    cursor = con.cursor()
    command_sql = f"INSERT INTO posts (name, content) VALUES ('{name}', '{content}')"
    cursor.execute(command_sql)
    con.commit()
    con.close()


def get_posts():
    con = mysql.connector.connect(host='localhost',user='root', password='', db='posts')
    cursor = con.cursor()
    command_sql = 'SELECT * FROM posts'
    cursor.execute(command_sql)
    posts = cursor.fetchall()
    con.close()
    return posts