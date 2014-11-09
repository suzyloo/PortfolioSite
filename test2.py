from flask import Flask
from flask import render_template
import collections

app = Flask(__name__)
import sqlite3

#films = {}
#films['Drive']              = '2011'
#films['Donnie Darko']       = '2001'
#films['Django Unchained']   = '2012'
#films['Die Hard']           = '1998'
#films['Dumbo']              = '1941' 

db = sqlite3.connect('movies.db')

@app.route('/')
def hello_world():
    return render_template('movieWelcome.html')

@app.route('/films/')
def hello_films():
    c = db.cursor()
    c.execute("SELECT * FROM movies")
    list = c.fetchall()
    map = dict(list)
    sortedKeys = sorted(map)
    return render_template('filmList.html', movies=map, sortedKeys=sortedKeys)

@app.route('/films/<name>')
def user(name):
    title = name
    c = db.cursor()
    c.execute("SELECT * FROM movies WHERE name='" + title + "'")        
    list = c.fetchall()
    map = dict(list)
    return render_template('specFilm.html', movies=map, title=title) 


if __name__ == '__main__':
    app.run()