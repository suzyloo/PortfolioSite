from flask import Flask
app = Flask(__name__)

films = {}
films['Drive']              = '2011'
films['Donnie Darko']       = '2001'
films['Django Unchained']   = '2012'
films['Die Hard']           = '1998'
films['Dumbo']              = '1941' 

@app.route('/')
def hello_world():
    return 'Welcome!'

@app.route('/films/')
def hello_films():
    A = "Movies"
    for key in sorted(films.keys()):
        A = A + "<br>" + key + " " + films[key]
        
    return A

@app.route('/films/<name>')
def user(name):
    title = name
    for key in sorted(films.keys()):
        if key == title:
            return key + " " + films[key]
    

if __name__ == '__main__':
    app.run()
