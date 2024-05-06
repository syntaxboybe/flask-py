from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hello World</h1>"

@app.route('/animal')
def animal():
    return """<h1>Hello Animals</h1>
<p>animals on animals dont go</p> """