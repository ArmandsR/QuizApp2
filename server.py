from flask import Flask
from flask import request
from flask import render_template

app = Flask(_name_)
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

@app.route('/health')
def health():
    return "OK"

if _name_ == '__main__':
    app.run(debug="true")