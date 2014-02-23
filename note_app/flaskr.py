from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session,g,redirect,url_for, \
abort, render_template,flash
import flask
import urllib2
import requests
from contextlib import closing
app=Flask(__name__)
app.config.update(dict(
DATABASE='/tmp/flaskr.db',
DEBUG=True,
SECRET_KEY='development key',
USERNAME='admin',
PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
     with app.open_resource('schema.sql',mode='r') as f:
        db.cursor().executescript(f.read())
     db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
  db = getattr(g, 'db', None)
  if db is not None:
     db.close()


@app.route('/')
def show_entries():
  cur=g.db.execute('select id,title,text,password from entries order by id desc')
  entries=[dict(id=row[0],title=row[1],text=row[2],password=row[3])for row in cur.fetchall()]
  return render_template('show_entries.html',entries=entries)
@app.route('/post',methods=['GET','POST'])
def post():
  cur2=g.db.execute('select id,title , text,password from entries order by id desc')
  texts=[dict(id=row[0],title=row[1],text=row[2],password=row[3]) for row in cur2.fetchall()]
  b=len(texts)
  passwrd=flask.request.form["passwrd"]
  post_id=flask.request.form["id"]
  a=int(post_id)
  text=(texts[b-a]["text"])
  title=(texts[b-a]["title"])
  if(texts[b-a]["password"]==passwrd):
     return render_template('post.html',text=text, title=title)
  else:
     text="The password given is invalid . You cannot read the post"
  return render_template('post.html',text=text,title=title)
@app.route('/add',methods=['GET','POST'])
def add_entry():
  if not session.get('logged_in'):
     abort(401)
  g.db.execute('insert into entries (title,text,password) values (?,?,?)',[request.form['title'],
request.form['text'],
request.form['password']])
  g.db.commit()
  flash(" New entry successfully posted")
  return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        cur1=g.db.execute('select user1,enter_password from users order by id desc')
        users=[dict(user1=row[0],enter_password=row[1])for row in cur1.fetchall()]
        username=flask.request.form['username']
        passwd=flask.request.form['password']
        c=0
        for x in users:
            if username == x['user1'] and x['enter_password'] == passwd:
                 flask.session['username'] = username
                 session['logged_in'] = True
                 flash('You were logged in')
                 c=1
                 return redirect(url_for('show_entries'))
            #else:
                # flask.flash("username does not exist or password is incorrect")
                # error = 'Invalid username or password'    
            if c==0:
                flash('wrong username OR password.Please check your username OR password')  
    return render_template('login.html', error=error)
@app.route('/signup', methods=['GET','POST'])
def signup():
    g.db.execute('insert into users(user1,enter_password) values(?,?)',[request.form['user'],
    request.form['enter_password']])
    g.db.commit()
    flash("You are now registered.Please login in.")
    cur1=g.db.execute('select user1,enter_password from users order by id desc')
    users=[dict(user1=row[0],enter_password=row[1])for row in cur1.fetchall()]
    return redirect(url_for('login'))
@app.route('/logout')
def logout():
  session.pop('logged_in',None)   
  return redirect(url_for('login'))   

if __name__=='__main__':
  init_db()
  app.run(debug=True)
  
