#!/usr/bin/env python3
from flask import Flask
from flask import request
import storage

conn = storage.connect()

app = Flask(__name__)

@app.route('/getTotalFromIngredient')
def getTotalFromIngredient():
    #Get parameter from request
    ingredient = request.args.get('ingredient')

    #Query
    cursor = conn.cursor()
    cursor.execute("select ingredient,total from fooddata where ingredient = %s;", (ingredient,))

    #Filter query result
    rows = cursor.fetchall()
    rows = str(rows[0][1])
    return rows
                                            
if __name__ == '__main__':
    app.run()
