from flask import Flask,render_template

application = Flask(__name__)

@application.route('/helloworld')
def hello_world():
    return {"message":"Hello World!"}

@application.route('/')
def index():
    return render_template("index.html")