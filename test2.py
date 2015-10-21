from flask import Flask
from flask import render_template
import collections

app = Flask(__name__)
import sqlite3

db = sqlite3.connect('photos.db')
draw = sqlite3.connect('drawings.db')


class Photo(object):
    path = ""
    title = ""
    desc = ""
    tags = ""
    year = 0

    # Class "constructor" / initializer.
    def __init__(self, path, title, desc, tags, year):
        self.path = path
        self.title = title
        self.desc = desc
        self.tags = tags
        self.year = year

def make_photo(path, title, desc, tags, year):
    photo = Photo(path, title, desc, tags, year)
    return student

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

@app.route('/photography/')
def hello_photography():
    c = db.cursor()
    c.execute("SELECT * FROM photography")
    allRows = c.fetchall()
    photoList = []
    for row in allRows:
        path = row[0]
        title = row[1]
        desc = row[2]
        tags = row[3]
        year = row[4]
        p = Photo(path,title,desc,tags,year)
        photoList.append(p)

    for x in photoList:
        print(x.title)
        
    return render_template('photography.html', photos=photoList)

@app.route('/drawings/')
def hello_drawings():
    c = draw.cursor()
    c.execute("SELECT * FROM drawings")
    allRows = c.fetchall()
    photoList = []
    for row in allRows:
        path = row[0]
        title = row[1]
        desc = row[2]
        tags = row[3]
        year = row[4]
        p = Photo(path,title,desc,tags,year)
        photoList.append(p)

    for x in photoList:
        print(x.title)
        
    return render_template('drawings.html', photos=photoList)

@app.route('/contact/')
def hello_pigeon():
    return render_template('contact.html')

@app.route('/about/')
def hello_brain():
    return render_template('about.html')
    
@app.route('/yahtzee/')
def hello_yahtzee():
    return render_template('yahtzee.html')

@app.route('/web/')
def hello_developer():
    return render_template('web.html')

if __name__ == '__main__':
    app.run()







