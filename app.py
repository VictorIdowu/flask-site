from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>This is the Home Page<h1> <a href="/profile/John">John</a>'

@app.route('/admin')
def welcome_admin():
  return '<h1>Welcome Admin<h1> <a href="/">Home</a>'

@app.route('/guest/<guest>')
def welcome_guest(guest):
  return '<h1>Welcome %s</h1> <a href="/">Home</a>' % guest

@app.route('/user/<name>')
def welcome_user(name):
  if name == 'admin':
    return redirect(url_for('welcome_admin'))
  else:
    return redirect(url_for('welcome_guest',guest=name))




app.run(debug=True)