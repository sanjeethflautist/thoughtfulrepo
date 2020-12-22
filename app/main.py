from fastapi import FastAPI
import sqlite3
import random
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
dbfilepath = os.path.join(THIS_FOLDER, 'my_data.db')


app = FastAPI()

@app.get("/getathought")
def getathought():
    id = random.randrange(1000)
    conn = sqlite3.connect(dbfilepath)
    c = conn.cursor()
    content = c.execute("SELECT QUOTE,AUTHOR FROM QUOTES WHERE ID=" + str(id) + "").fetchall()[0]
    return {content}

'''x
@app.get("/")
def read_root():
    return "Not supported URL"


if __name__ == '__main__':
    read_root()
'''