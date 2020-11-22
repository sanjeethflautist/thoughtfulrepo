from fastapi import FastAPI
import sqlite3
import random
app = FastAPI()

@app.get("/getathought")
def read_root():
    id = random.randrange(1000)
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()
    content = c.execute("SELECT QUOTE,AUTHOR FROM QUOTES WHERE ID=" + str(id) + "").fetchall()[0]
    return {content}


@app.get("/")
def read_root():
    return {"URL not supported"}