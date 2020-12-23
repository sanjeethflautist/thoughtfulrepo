from fastapi import FastAPI
import sqlite3
import random
import os
import json

json_data = json.dumps({})



THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
dbfilepath = os.path.join(THIS_FOLDER, 'my_data.db')


app = FastAPI()

@app.get("/getathought")
def getathought():
    id = random.randrange(1000)
    connection_obj = sqlite3.connect(dbfilepath)
    cursor_obj = connection_obj.cursor()
    content = cursor_obj.execute("SELECT QUOTE,AUTHOR FROM QUOTES WHERE ID=" + str(id) + "").fetchall()[0]
    json_data = json.dumps({'Quote': content[0], 'By':  content[1]})
    return json_data


@app.get("/")
def read_root():
    return "Not supported URL"

'''
if __name__ == '__main__':
    print(getathought())
'''

