from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'This is the Home Page- <a href="/new">New</a>'

@app.route('/new')
def new():
  return 'This is a new page <a href="/">Home</a>'


app.run()